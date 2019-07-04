from metro_classes import Station, Metro
from metro_lines import line_dict

def build_metro(metro_dict):
    metro_to_build = Metro()
    for line in metro_dict.keys():
        metro_to_build.add_station((metro_dict[line])[0])
        for i in range(1,len(metro_dict[line])):
            metro_to_build.add_station((metro_dict[line])[i])
            metro_to_build.add_connection(line, (metro_dict[line])[i-1], (metro_dict[line])[i])
    return metro_to_build
