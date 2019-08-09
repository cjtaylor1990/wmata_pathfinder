from metro_classes import Station, Metro
from find_metro_path import find_metro_path
import pickle

#Loading in the WMATA metro pickle file
wmata = pickle.load(open("wmata.p", "rb"))

#Asking for user input for starting point and destination
start_station = input("Where will you be starting?: ")
end_station = input("Where do you want to go? ")

#Finding the path between the starting point and destination
metro_path = find_metro_path(wmata,start_station,end_station)

#Defining current linee and the point where they got on that line
current_line = metro_path[1][0]
current_get_on = start_station

#Creating the output string to print to user with directions
path_string = "A possible path:\nStarting at {}, go on the {} line.\n".format(start_station, metro_path[1][0])
for i in range(1, len(metro_path)):
    if metro_path[i][0] != current_line:
        path_string += "\n{} --- {} ---> {} \n".format(current_get_on, current_line, metro_path[i-1][1])
        current_get_on = metro_path[i-1][1]
        current_line = metro_path[i][0]

path_string += "\n{} --- {} ---> {} \n".format(current_get_on, current_line, metro_path[-1][1])
print(path_string)
