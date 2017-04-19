import socket
import os
import json

host = ""
UDP_port = 8001

def relax(sourc,dest,RoutingTable,Nodes,Dist):
    UDP_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDP_s.bind((host, UDP_port))
    pid = os.fork()
    if pid == 0:
        message, clientAddress = UDP_s.recvfrom(1024)
        data = json.dumps(RoutingTable[dest])
        UDP_s.sendto(data, clientAddress)
        UDP_s.close()
        os._exit(0)
    else:
        receive_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        receive_s.sendto("handshake",(host, UDP_port))
        data, serverAddress = receive_s.recvfrom(1024)
        datalist = json.loads(data)
        receive_s.close()

    for i in range(Nodes):
        if i == sourc:
            continue
        if datalist[i][0] > 0:
            if RoutingTable[sourc][i][0] < 0 or RoutingTable[sourc][i][0] > datalist[i][0] + Dist[dest][sourc]:
                RoutingTable[sourc][i][0] = datalist[i][0] + Dist[dest][sourc]
                RoutingTable[sourc][i][1] = dest

def Bellman_Ford(Nodes, Dist, RoutingTable):
    for i in range(Nodes):
        for j in range(Nodes):
            if Dist[i][j] > 0:
                relax(i,j,RoutingTable,Nodes,Dist)