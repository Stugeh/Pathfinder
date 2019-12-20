class City:
    def __init__(self, atrCity):
        self.id = atrCity
        self.adjacent = {}

    def add_neighbor(self, neighbor, elevation=0):
        self.adjacent[neighbor] = elevation


class Graph:
    def __init__(self):
        self.cities = {}
        self.num_cities = 0

    def add_city(self, atrCity):
        self.num_cities = self.num_cities + 1
        new_city = City(atrCity)
        self.cities[atrCity] = new_city
        return new_city

    def add_road(self, frm, to, elevation = 0):
        if frm not in self.cities:
            self.add_city(frm)
        if to not in self.cities:
            self.add_city(to)
        self.cities[frm].add_neighbor(self.cities[to], elevation)
        self.cities[to].add_neighbor(self.cities[frm], elevation)

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])


def read_network_file(path):
    """
    Reads a formatted .txt file, appends it to a list called networkInfo, gets the number of cities and roads as
    well as the destination city from the first and last lines of the document respectively. After this it
    slices them away and returns the remaining list to create the network itself.
    """
    networkInfo = []
    if path.endswith(".txt"):
        file = open(path, "r")
        for line in file:
            line = line.rstrip()
            networkInfo.append(line.split(' '))
        cities = int(networkInfo[0][0])
        roads = int(networkInfo[0][1])
        destination = int(networkInfo[roads+1][0])
        networkInfo = networkInfo[1:-1]
#       debugging info
        print("roads: ", networkInfo, "\n# of roads:  ", roads, "\n# of cities: ", cities, "\ndestination: ", destination)
        return cities, roads, destination, networkInfo
    else: print("Not a .txt file")



