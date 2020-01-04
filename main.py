from pathfinderGraph import *

if __name__ == '__main__':
    cities, roads, destination, networkInfo = read_network_file('graph_testdata/graph_ADS2018_10_1.txt')
    for i in range(1, cities+1):
        add_city(i)
    add_roads(networkInfo)
    print(kruskal(), 'finished')


