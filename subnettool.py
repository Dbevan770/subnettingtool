def determineClass(ip):
    ipList = ip.split(".")
    defaultCidr = 0
    ipList [0] = int(ipList[0])

    if ipList[0] <= 127:
        defaultCidr = 8
    elif ipList[0] <= 191:
        defaultCidr = 16
    elif ipList[0] <= 223:
        defaultCidr = 24

    return defaultCidr


def lastNetwork(ip, octIncr):
    ipList = ip.split(".")
    ipList[3] = str(int(ipList[3]) - 1)
    ip = "."

    return ip.join(ipList)


def broadcastNetwork(ip, octIncr, ooi, cidr):
    ipList = ip.split(".")

    if ooi == 3:
        ipList[ooi] = str(octIncr + (cidr - 1))
    elif ooi == 2:
        ipList[ooi] = str(octIncr + (cidr - 1))
        ipList[3] = str(255)
    elif ooi == 1:
        ipList[ooi] = str(octIncr + (cidr - 1))
        ipList[2] = str(255)
        ipList[3] = str(255)
    elif ooi == 0:
        ipList[ooi] = str(octIncr + (cidr - 1))
        ipList[1] = str(255)
        ipList[2] = str(255)
        ipList[3] = str(255)
    ip = "."

    return ip.join(ipList)


def firstNetwork(ip):
    ipList = ip.split(".")
    ipList[3] = str(int(ipList[3]) + 1)
    ip = "."

    return ip.join(ipList)


def cidrIncr(step):
    netval = 256
    val = 0
    while val < (step % 8):
        netval = netval / 2
        val += 1

    step = netval
    return int(step)


def main():
    while True:
        ipAddr = input("Enter IP Address to subnet: ")
        if ipAddr.lower() in ["q", "quit"]:
            break
        userCidr = input("Enter the CIDR notation of the network: ")
        if userCidr.lower() in ["q", "quit"]:
            break

        userCidr = int(userCidr)
        ooi = 0

        ipAddrList = ipAddr.split(".")

        if userCidr >= 24:
            ooi = 3
        elif userCidr >= 16:
            ooi = 2
        elif userCidr >= 8:
            ooi = 1
        else:
            ooi = 0

        octInt = int(ipAddrList[ooi])

        octIncr = 0

        cidr = cidrIncr(userCidr)
        # print(cidr)

        if ooi == 0:
            while octIncr < octInt:
                if (octIncr + cidr) > octInt:
                    break
                else:
                    octIncr += cidr
            ipAddr = str(octIncr) + ".0.0.0"
            # print(ipAddr)
        elif ooi == 1:
            while octIncr < octInt:
                if (octIncr + cidr) > octInt:
                    break
                else:
                    octIncr += cidr
            ipAddr = ipAddrList[0] + "." + str(octIncr) + ".0.0"
            # print(ipAddr)
        elif ooi == 2:
            while octIncr < octInt:
                if (octIncr + cidr) > octInt:
                    break
                else:
                    octIncr += cidr
            ipAddr = ipAddrList[0] + "." + ipAddrList[1] + "." + str(octIncr) + ".0"
            # print(ipAddr)
        elif ooi == 3:
            while octIncr < octInt:
                if (octIncr + cidr) > octInt:
                    break
                else:
                    octIncr += cidr
            ipAddr = ipAddrList[0] + "." + ipAddrList[1] + "." + ipAddrList[2] + "." + str(octIncr)
            # print(ipAddr)

        firstNetIP = firstNetwork(ipAddr)
        broadNetIP = broadcastNetwork(ipAddr, octIncr, ooi, cidr)
        lastNetIP = lastNetwork(broadNetIP, octIncr)
        defaultCidr = determineClass(ipAddr)
        hostCount = 2**(32-userCidr) - 2
        netCount = 2**(userCidr - defaultCidr)

        print("Network IP Address: " + ipAddr)
        print("First Network IP Address: " + firstNetIP)
        print("Last Network IP Address: " + lastNetIP)
        print("Broadcast Network IP Address: " + broadNetIP)
        print("Number of Hosts on the Network: " + str(hostCount))
        print("Number of Networks: " + str(netCount))


main()
