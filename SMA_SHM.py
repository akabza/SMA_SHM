#!/usr/bin/python3
# -*- coding: utf-8 -*-

# SMA_speedwire.py, based on https://gist.github.com/mitchese/afd823c3c5036c5b0e5394625f1a81e4
# created by Alexander Kabza, 2022-01-20
# 2022-01-20    first version
# 2022-01-21    getvalue() added

import socket
import struct

MULTICAST_IP = "239.12.255.254"
MULTICAST_PORT = 9522

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("", MULTICAST_PORT))

mreq = struct.pack("4sl", socket.inet_aton(MULTICAST_IP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)


def getvalue(hexStr, search, length):
    pos = hexStr.find(search)
    if (pos != -1):
        pos = pos + len(search)
        value = hexStr[pos:pos + length]
        try:
            floatvalue = float(int(value, 16))
        except:
            floatvalue = 0.0
        return floatvalue
    else:
        floatvalue = 0.0
        return floatvalue


# --- def getvalue


def decode_speedwire(data):

    SMA = data[0:3]  # This is just the identifier of the packet, should start with "SMA\0"
    sysUid = data[4:7]
    serialNumber = data[20:24]
    #print("SMA: " + str(SMA) + " sysUid: " + str(sysUid) + " Serial: " + str(serialNumber.hex()))

    hexStr = ""
    for onebyte in data: hexStr += f"{onebyte:02x}"
    #print(hexStr)

    print("SerialNo " + str(int(hexStr[40:48], 16)) + "\n")

    P_pos = getvalue(hexStr, "010400", 8) / 10
    P_neg = getvalue(hexStr, "020400", 8) / 10
    E_pos = getvalue(hexStr, "010800", 16) / 3600000
    E_neg = getvalue(hexStr, "020800", 16) / 3600000
    Pb_pos = getvalue(hexStr, "030400", 8) / 10
    Pb_neg = getvalue(hexStr, "040400", 8) / 10
    Eb_pos = getvalue(hexStr, "030800", 16) / 3600000
    Eb_neg = getvalue(hexStr, "040800", 16) / 3600000
    Ps_pos = getvalue(hexStr, "090400", 8) / 10
    Ps_neg = getvalue(hexStr, "0a0400", 8) / 10
    Es_pos = getvalue(hexStr, "090800", 16) / 3600000
    Es_neg = getvalue(hexStr, "0a0800", 16) / 3600000
    phi = getvalue(hexStr, "0d0400", 8) / 10

    print("Leistung  --- positiv ---  --- negativ ---")
    print("Wirk      {0:6.1f}  (1.4.0)  {1:6.1f}  (2.4.0) W".format(P_pos, P_neg))
    print("Blind     {0:6.1f}  (3.4.0)  {1:6.1f}  (4.4.0) W".format(Pb_pos, Pb_neg))
    print("Schein    {0:6.1f}  (9.4.0)  {1:6.1f} (10.4.0) W".format(Ps_pos, Ps_neg))
    print("L-Faktor  {0:6.1f} (13.4.0) %\n".format(phi))

    print("Arbeit    ---- positiv ----  ---- negativ -----")
    print("Wirk      {0:9.3f} (1.8.0)  {1:9.3f}  (2.8.0) kWh".format(E_pos, E_neg))
    print("Blind     {0:9.3f} (3.8.0)  {1:9.3f}  (4.8.0) kWh".format(Eb_pos, Eb_neg))
    print("Schein    {0:9.3f} (9.8.0)  {1:9.3f} (10.8.0) kWh\n".format(Es_pos, Es_neg))

    P1_pos = getvalue(hexStr, "150400", 8) / 10
    P1_neg = getvalue(hexStr, "160400", 8) / 10
    P2_pos = getvalue(hexStr, "290400", 8) / 10
    P2_neg = getvalue(hexStr, "2a0400", 8) / 10
    P3_pos = getvalue(hexStr, "3d0400", 8) / 10
    P3_neg = getvalue(hexStr, "3e0400", 8) / 10
    I1 = getvalue(hexStr, "1f0400", 8) / 100
    I2 = getvalue(hexStr, "330400", 8) / 100
    I3 = getvalue(hexStr, "470400", 8) / 100
    U1 = getvalue(hexStr, "200400", 8) / 1000
    U2 = getvalue(hexStr, "340400", 8) / 1000
    U3 = getvalue(hexStr, "480400", 8) / 1000
    phi1 = getvalue(hexStr, "210400", 8) / 10
    phi2 = getvalue(hexStr, "350400", 8) / 10
    phi3 = getvalue(hexStr, "490400", 8) / 10

    print("Phasen           ------- L1 ------ ------- L2 ------ ------- L3 ------")
    print("positiv         {0:7.1f} (21.4.0)  {1:7.1f} (41.4.0)  {2:7.1f} (61.4.0) W".format(P1_pos, P2_pos, P3_pos))
    print("negativ         {0:7.1f} (22.4.0)  {1:7.1f} (42.4.0)  {2:7.1f} (62.4.0) W".format(P1_neg, P2_neg, P3_neg))
    print("Strom            {0:7.2f} (31.4.0)  {1:7.2f} (51.4.0)  {2:7.2f} (71.4.0) A".format(I1, I2, I3))
    print("Spannung          {0:7.3f} (32.4.0)  {1:7.3f} (52.4.0)  {2:7.3f} (72.4.0) V".format(U1, U2, U3))
    print("Leistungsfaktor {0:7.1f} (33.4.0)  {0:7.1f} (53.4.0)  {0:7.1f} (73.4.0) %".format(phi1, phi2, phi3))

# --- main -------------------------------------------
if __name__ == "__main__":
    decode_speedwire(sock.recv(10240))
