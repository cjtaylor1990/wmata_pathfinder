class Station:
    def __init__(self, station_name):
        self.station_name = station_name
        self.connections = {}

    def add_connection(self, line_to_connection, connection):
        if line_to_connection in self.connections.keys():
            self.connections[line_to_connection] += [connection]
        else:
            self.connections[line_to_connection] = [connection]

    def print_connections(self):
        connection_string = ""
        for line in self.connections.keys():
            connection_string += "{} : {}, ".format(line, self.connections[line])
        print(connection_string)

class Metro:
    def __init__(self):
        self.all_stations = {}

    def add_station(self, station_name):
        if station_name not in self.all_stations.keys():
            self.all_stations[station_name] = Station(station_name)
        else:
            pass#raise KeyError("{} is already in the metro system!".format(station_name))

    def add_connection(self, line, station1, station2):
        if (station1 != station2):
                self.all_stations[station1].add_connection(line, station2)
                self.all_stations[station2].add_connection(line, station1)
        else:
            raise KeyError("The first and second station must be different!")

"""
wmata = Metro()
wmata.add_station(red_line[0])
for i in range(1,len(red_line)):
    wmata.add_station(red_line[i])
    wmata.add_connection('Red', red_line[i-1], red_line[i])
    wmata.all_stations[red_line[i-1]].print_connections()

print(type(wmata))
wmata.add_station('Glenmont')
"""
