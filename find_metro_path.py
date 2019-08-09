from metro_classes import Station, Metro
from build_metro import wmata

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

    #Creating the queue for the graph search
    bs_queue = [[start_station, path]]

    #Creating a set that will store the names of the stations visited (to make sure there is no repeats)
    stations_visited = set()

    #While the queue isn't empty
    while len(bs_queue) != 0:
        #De-queue the front of the queue 
        current_station, path = bs_queue.pop(0)

        #Finding the corresponding Station object from the Metro object
        current_station_object = metro.all_stations[current_station]

        #Adding the current station to the set of those visited
        stations_visited.add(current_station)

        #For each line that the current station is connected to (i.e. has as a key in its connections dictionary)
        for line in current_station_object.connections.keys():

            #For each station directly connected along the current line
            for station in current_station_object.connections[line]:

                #If that station hasn't been visited (if it has, do nothing)
                if station not in stations_visited:

                    #If the current station is equal to the station that is being searched for
                    if station == end_station:
                        #Return the path used to reach the destination
                        return path + [[line, station]]
                    else:
                        #If it's not the end station, add it to the queue
                        bs_queue += [[station, path + [[line, station]]]]
