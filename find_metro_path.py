from metro_classes import Station, Metro
from build_metro import wmata
import math

def find_metro_path(metro, start_station, end_station):
    """
    Takes in a Metro object and the names of the starting and destination stations. Will output an array
    with the stations that are transversed along each line, along with the corresponding line used.

    Currently uses a DFS algorithm and manually puts stations on the current line after the rest, thus
    ensuring they pop first. This was chosen given the nature of the subway system and wanting to minimize
    line switching.
    """
    
    #Checks to see if both the intial and destination stations are in the metro object. If they aren't raise a ValueError
    if start_station not in metro.all_stations.keys():
        raise ValueError("There is not a station named {} in the WMATA system.".format(start_station))
    if end_station not in metro.all_stations.keys():
        raise ValueError("There is not a station named {} in the WMATA system.".format(end_station))

    #Defining a list that will be the main output
    path = [start_station]

    #Creating the stack for the DFS graph search
    dfs_stack = []

    #Adding in the first stations connections to the stack
    for line in metro.all_stations[start_station].connections.keys():
        for station in metro.all_stations[start_station].connections[line]:
           dfs_stack += [[station, path + [[line, station]]]]

    #Creating a set that will store the names of the stations visited (to make sure there is no repeats). Adding starting station to it.
    stations_visited = set([start_station])

    #While the stack isn't empty (or until the destination is found)
    while len(dfs_stack) != 0:
        
        #Popping the top entry of stack
        current_station, path = dfs_stack.pop()
        
        #Checking if current station is end station. If it is, returns the path
        if current_station == end_station:
            return path

        #Finding current line from last entry in path
        current_line = path[-1][0]

        #Finding the corresponding Station object from the Metro object
        current_station_object = metro.all_stations[current_station]

        #Adding the current station to the set of those visited
        stations_visited.add(current_station)

        #Getting lines connected to station
        lines_connected = list(current_station_object.connections.keys())
        lines_connected.remove(current_line)
        lines_connected = lines_connected + [current_line]

        #For each line that the current station is connected to (i.e. has as a key in its connections dictionary)
        for line in lines_connected:

            #For each connected station in current line
            for station in current_station_object.connections[line]:

                #If that station hasn't been visited (if it has, do nothing)
                if station not in stations_visited:
                    #Add to the top of the stack
                    dfs_stack += [[station, path + [[line, station]]]]

