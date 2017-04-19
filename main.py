import socket
import os
import json
import SSPAlgo


def input_data():
    global Nodes,Dist,RoutingTable
    Nodes = input()
    Dist = [[ -10**8 for i in range(Nodes) ] for j in range(Nodes)]

    # Routing Table is storing content as
    # cost, node(Next hop node)
    RoutingTable = [[ [-10**8,i] for i in range(Nodes) ] for j in range(Nodes)]
    
    for i in range(Nodes):
        in_string = raw_input()

        # adjStr contains the (node, cost) in string
        # form for inputs
        adjStr = in_string.split()
        adjStr.pop(0)
        while len(adjStr)>0:
            
            a = int(adjStr.pop(0))-1
            if a >= Nodes:
                print "node number exceeded\n"
                return -1
            
            b = int(adjStr.pop(0))
            
            Dist[i][a] = b
            Dist[a][i] = b
            
            RoutingTable[i][a][0] = b
            RoutingTable[i][a][1] = a
    return 1

def Display():
    
    for i in range(Nodes):   
        adjStr = ''
        print '\nFor Node #' + str(i+1) + ':'
        
        for j in range(Nodes):
            if RoutingTable[i][j][0]>0:
                adjStr = adjStr + '(' + str(i+1) + '->' + str(j+1) + ' = ' + str(RoutingTable[i][j][0]) + ') '
        print adjStr 

Nodes = 0
Dist = []
RoutingTable = []

x = input_data()
while x < 0:
    x = input_data()
SSSPAlgo.Bellman_Ford(Nodes, Dist, RoutingTable)
Display()
