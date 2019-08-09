from metro_classes import Station, Metro
from metro_lines import line_dict
import pickle

def build_metro(metro_dict):
	"""
	This function builds the Metro object using the line information provided to it via a
	dictionary. The keys of the dictionary have to be the name of the line and the values
	are arrays of different station names along said line
	"""
	#Initiating the Metro object
    metro_to_build = Metro()
    for line in metro_dict.keys(): #For each line key in the input dictionary
    	#Add the first station of the line to the Metro object
        metro_to_build.add_station((metro_dict[line])[0])
        for i in range(1,len(metro_dict[line])): #For each station after the first
            #Add the station fot he Metro object and connect it to the previous station along line
            metro_to_build.add_station((metro_dict[line])[i])
            metro_to_build.add_connection(line, (metro_dict[line])[i-1], (metro_dict[line])[i])
    return metro_to_build #Return finished Metro object

#Building the metro object (wmata) using the metro line information in line_dict and saving it to a pickle file to be loaded later
wmata = build_metro(line_dict)
pickle.dump(wmata, open("wmata.p", "wb"))
