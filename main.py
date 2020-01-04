from pathfinderGraph import *
import time
import os

if __name__ == '__main__':
    for filename in os.listdir('graph_large_testdata/'):
        start = time.time()
        print(filename)
        cities, roads, destination, networkInfo = read_network_file('graph_large_testdata/'+filename)
        for i in range(1, cities+1):
            add_city(i)
        add_roads(networkInfo)
        mst = kruskal()
        path = breadth_first(mst, destination)
        max_altitude = get_max_altitude(mst, path)
        print("best path: ", path, "\npath's altitude: ", max_altitude)
        end = time.time()
        print("elapsed: ", end - start, "\n\n\n")

