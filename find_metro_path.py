from metro_classes import Station, Metro
from build_metro import wmata
import math

def find_metro_path(metro, start_station, end_station):
    """
    Takes in a Metro object and the names of the starting and destination stations. Will output an array
    with the stations that are transversed along each line, along with the corresponding line used.
    """
    #Checks to see if both the intial and destination stations are in the metro object. If they aren't raise a ValueError
    if start_station not in metro.all_stations.keys():
        raise ValueError("There is not a station named {} in the WMATA system.".format(start_station))
    if end_station not in metro.all_stations.keys():
        raise ValueError("There is not a station named {} in the WMATA system.".format(end_station))

    #Defining a list that will be the main output
    path = [start_station]

    #Setting up distance metric for graph search optimization
    current_path_length = 0

    #Creating the queue for the graph search
    bs_queue = []

    #Adding in the first stations connections (will need them to do weighting calculations)
    for line in metro.all_stations[start_station].connections.keys():
        for station in metro.all_stations[start_station].connections[line]:
            bs_queue += [[station, path + [[line, station]]]]

    #Creating a set that will store the names of the stations visited (to make sure there is no repeats)
    stations_visited = set()
    stations_visited.add(start_station)

    #While the queue isn't empty
    while len(bs_queue) != 0:
        #De-queue the front of the queue 
        print(bs_queue[-1])
        current_station, path = bs_queue.pop()
        if current_station == end_station:
            return path

        #Finding current line from last entry in path
        current_line = path[-1][0]
        print(current_line)

        #Finding the corresponding Station object from the Metro object
        current_station_object = metro.all_stations[current_station]

        #Adding the current station to the set of those visited
        stations_visited.add(current_station)

        #Getting lines connected to station
        lines_connected = list(current_station_object.connections.keys())
        lines_connected.remove(current_line)
        lines_connected = lines_connected + [current_line]
        print(lines_connected)

        #For each line that the current station is connected to (i.e. has as a key in its connections dictionary)
        for line in lines_connected:#current_station_object.connections.keys():

            #if line == current_line:
            #    current_weight = 0
            #else:
            #    current_weight = 1

            #For each station directly connected along the current line
            for station in current_station_object.connections[line]:

                #If that station hasn't been visited (if it has, do nothing)
                if station not in stations_visited:
                    """
                    #If the current station is equal to the station that is being searched for
                    if station == end_station:
                        return path + [[line,station]]
                        #Return the path used to reach the destination
                        #iff current_path_distance + current_weight < current_min_length:
                        #    current_min_length = current_path_distance + current_weight
                        #    current_min_path = path + [[line,station]]
                    else:
                        #If it's not the end station, add it to the queue"""
                    bs_queue += [[station, path + [[line, station]]]]

    return current_min_path
