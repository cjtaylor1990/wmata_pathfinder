class Station:
    """
    This is a class that represents a single station. It is initialized
    with a station name (station_name) and initially given an empty dictionary
    map for its connections to other stations.

    The connections dictionary has keys equal to the different line names, each
    with an array that contains the nearest locations along that line (two stations
    per line key, unless of course you are at the end of a line).
    """
    def __init__(self, station_name):
        #Initialization the class object with station_name as input
        self.station_name = station_name
        self.connections = {}

    def add_connection(self, line_to_connection, connection):
        #Adds connection between one existing station to another
        if line_to_connection in self.connections.keys(): #checks to see if the line key already exists in connections dictionary
            #if it does, append the connecting station to array that is keyed by the line name
            self.connections[line_to_connection] += [connection]
        else:
            #if not, then create a new key and map it to an array containing the current connection
            self.connections[line_to_connection] = [connection] #

    def print_connections(self):
        #Prints the sring representation of the different lines/connections
        connection_string = "" #output string
        #For each line
        for line in self.connections.keys():
            connection_string += "{} : {}, ".format(line, self.connections[line]) #append the line+connections to output string
        print(connection_string) #print the string

class Metro:
    """
    This is a class made to contain all of the information about the stations and interfaces with them.
    It's effectively a graph structure that initializes containing an empty dictionary. The graph is
    bidirectional.

    The main way it does this is via the all_stations dictionary, which has the station names as keys that
    map to a Station object with said name.

    From there, you can add stations to the Metro object (add_stations) and connect them (add_connection).
    """
    def __init__(self):
        #Initilizes Metro object
        self.all_stations = {}

    def add_station(self, station_name):
        #Initializes a Station object and adds it to the all_stations dictionary if station isn't already in it
        if station_name not in self.all_stations.keys():
            self.all_stations[station_name] = Station(station_name)
        else:
            pass

    def add_connection(self, line, station1, station2):
        #Adds connections between station1 and station2 via specified line.
        if (station1 != station2) and (station1 in self.all_stations.keys()) and (station2 in self.all_stations.keys()):
                #Creating the bidirectional direction between the two Station objects using the add_connection Station method
                self.all_stations[station1].add_connection(line, station2)
                self.all_stations[station2].add_connection(line, station1)
        else:
            raise KeyError("Error: The first and second station must be different and both must be in the Metro system.")
