"""
This program creates a network out of a formatted text file and finds the path of least resistance
(lowest weight edges). To achieve this it uses Kruskal's minimum spanning tree algorithm.

NETWORK : contains the nodes or "cities" as well as the edges (roads).
PARENT : contains each node's parent node. Used for checking for cycles in the network.
RANK : contains each node's rank. Also used for checking for cycles.
"""
NETWORK = {
    'cities': []
}
PARENT = dict()
RANK = dict()


def create_adjacency_list(roads):
    """
    To make path finding easier this function gets the minimum spanning tree
    as an input and returns an an adjacency list.
    """
    adj_list = {}
    for road in roads:
        adj_list[road[0]] = []   # initializing the keys of the adjacency list
        adj_list[road[1]] = []
    for road in roads:          # adds all the adjacency's for each key
        adj_list[road[0]].append(road[1])
        adj_list[road[1]].append(road[0])
    return adj_list


def breadth_first(mst, destination):
    """
    This function gets as an input the minimum spanning tree constructed earlier,
    as well as the destination it we want to get to. It finds the path between
    city 1 and the destination by utilising the breadth first search algorithm.
    """
    adj_list = create_adjacency_list(mst)    # returns a reformatted version of the MST
    explored = []
    queue = [[1]]
    while queue:
        path = queue.pop(0)
        city = path[-1]
        if city not in explored:
            neighbours = adj_list[city]      # gets neighbouring nodes for each city
            for neighbour in neighbours:    # and loops through them while forming
                new_path = list(path)       # paths for each of them
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == destination:    # When the algorithm stumbles upon the
                    return new_path             # destination city it returns the shortest path
            explored.append(city)               
    return "There is no path to city: ", destination


def make_set(city):
    """This function is used to initialize each city's values in the PARENT and RANK dictionaries"""
    PARENT[city] = city
    RANK[city] = 0


def find(city):
    """Finds a city's parent and returns it"""
    if PARENT[city] != city:
        PARENT[city] = find(PARENT[city])
    return PARENT[city]


def union(city1, city2):
    """Combines the sets containing cities 1 and 2 if they don't have common parents"""
    root1 = find(city1)
    root2 = find(city2)
    if root1 != root2:
        if RANK[root1] > RANK[root2]:
            PARENT[root2] = root1
        else:
            PARENT[root1] = root2
        if RANK[root1] == RANK[root2]:
            RANK[root2] += 1


def kruskal():
    """
    Kruskal's MST algorithm. First it sorts the set NETWORK['roads'] by weight before utilizing the find()
    and union() functions to combine unconnected nodes until every possible node is connected.
    """
    roads = list(NETWORK['roads'])
    minimum_spanning_tree = set()
    for city in NETWORK['cities']:  # initializes every city's dictionary values
        make_set(city)
    roads.sort(key=lambda x: x[2])  # sorts roads by elevation

    for road in roads:
        city1, city2, altitude = road
        if find(city1) != find(city2):          # Checks if city1 and city2 have common parents.
            union(city1, city2)                 # If none found it does a union for their sets
            minimum_spanning_tree.add(road)     # before adding the road to the MST
    return sorted(minimum_spanning_tree)


def add_city(city):
    """
    adds a city to the NETWORK dictionary
    """
    NETWORK['cities'].append(city)


def add_roads(roads):
    """
    gets an array containing roads to be added to the NETWORK dictionary
    """
    roads_array = []
    for i in range(len(roads)):
        city1 = int(roads[i][0])                        # Gets the values from their predetermined
        city2 = int(roads[i][1])                        # indexes in each sub-array.
        altitude = int(roads[i][2])
        roads_array.append((city1, city2, altitude))    # And appends them to a temporary array before pushing
    NETWORK['roads'] = roads_array                      # it back up to the NETWORK dictionary.


def read_network_file(path):
    """
    Reads a formatted .txt file, appends it to a list called network_info, gets the number of cities and roads as
    well as the destination city from the first and last lines of the document respectively. After this it
    slices them away and returns the remaining list to create the network itself.
    """
    network_info = []    # useful info about the network
    if path.endswith(".txt"):
        file = open(path, "r")
        for line in file:
            line = line.rstrip()    # strips trailing newlines
            network_info.append(line.split(' '))     # splits the line into chunks,
        cities = int(network_info[0][0])             # so it can add it into network_info for later access.
        roads = int(network_info[0][1])
        destination = int(network_info[roads + 1][0])
        network_info = network_info[1:-1]                 # Now that the useful info has been extracted we can slice it
        return cities, roads, destination, network_info  # off only the roads remain.
    else:
        print("Not a .txt file")
