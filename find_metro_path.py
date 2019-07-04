from metro_classes import Station, Metro
from build_metro import wmata

def find_metro_path(metro, start_station, end_station):
    if start_station not in metro.all_stations.keys():
        raise ValueError("There is not a station named {} in the WMATA system.".format(start_station))
    if end_station not in metro.all_stations.keys():
        raise ValueError("There is not a station named {} in the WMATA system.".format(end_station))

    path = [start_station]
    bs_queue = [[start_station, path]]

    stations_visited = set()

    while len(bs_queue) != 0:
        current_station, path = bs_queue.pop(0)
        current_station_object = metro.all_stations[current_station]

        stations_visited.add(current_station)

        for line in current_station_object.connections.keys():

            for station in current_station_object.connections[line]:

                if station not in stations_visited:

                    if station == end_station:
                        return path + [[line, station]]
                    else:
                        #print(bs_queue)
                        bs_queue += [[station, path + [[line, station]]]]
