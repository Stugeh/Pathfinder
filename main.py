from pathfinderGraph import *

if __name__ == '__main__':
    cities, roads, destination, networkInfo = read_network_file('graph_testdata/graph_ADS2018_10_1.txt')
    network = Graph()
    for i in range(cities-1):
        network.add_city(str(i))
    for line in range(len(networkInfo)):
        network.add_road(int(networkInfo[line][0]), int(networkInfo[line][1]), int(networkInfo[line][2]))
    #network.find_MST()
