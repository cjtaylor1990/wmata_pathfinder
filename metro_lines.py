#Lists filled with names of the stations along each line
red_line = ['Glenmont', 'Wheaton', 'Forest Glen', 'Silver Spring', 'Takoma Park',
'Fort Totten', 'Brookland-CUA', 'Rhode Island Ave', 'NoMa-Gallaudet U',
'Union Station', 'Judiciary Sq', 'Gallery Place', 'Metro Central', 'Farragut North',
'Dupoint Circle', 'Woodley Park', 'Cleveland Park', 'Van Ness-UDC', 'Tenleytown-AU',
'Friendship Heights', 'Bethesda', 'Medical Center', 'Grosvenor-Strathmore', 'White Flint',
'Twinbrook', 'Rockville', 'Shady Grove']

orange_line = ['Vienna', 'Dunn Lorring', 'West Falls Church', 'East Falls Church',
'Ballston-MU', 'Virginia Sq-GMU', 'Clarendon', 'Court House', 'Rosslyn', 'Foggy Bottom-GWU',
'Farragut West', 'McPherson Sq', 'Metro Center', 'Federal Triangle', 'Smithsonian',
'LEnfant Plaza', 'Federal Center SW', 'Capitol South', 'Eastern Market', 'Potomac Ave',
'Stadium-Armory', 'Minnesota Ave', 'Deanwood', 'Cheverly', 'Landover', 'New Carrollton']

blue_line = ['Franconia-Springfield', 'Van Dorn St', 'King St-Old Town', 'Braddock Rd',
'Ronald Reagan Washington National Airport', 'Crystal City', 'Pentagon City',
'Arlington Cemetary', 'Rosslyn', 'Foggy Bottom-GWU','Farragut West', 'McPherson Sq',
'Metro Center', 'Federal Triangle', 'Smithsonian','LEnfant Plaza', 'Federal Center SW',
'Capitol South', 'Eastern Market', 'Potomac Ave', 'Stadium-Armory', 'Benning Rd',
'Capitol Heights', 'Addison Rd', 'Morgan Blvd', 'Largo Town Center']

green_line = ['Greenbelt', 'College Park-U of Md',
'Prince Georges Plaza','West Hyattsville', 'Fort Totten', 'Georgia Ave-Petworth',
'Columbia', 'U St','Shaw-Howard U', 'Mt Vernon Sq', 'Gallery Place', 'Archives', 'LEnfant Plaza',
'Waterfront', 'Navy Yard-Ballpark', 'Anacostia', 'Congress Heights', 'Southern Ave',
'Naylor Rd', 'Suitland', 'Branch Ave']

yellow_line = ['Greenbelt', 'College Park-U of Md',
'Prince Georges Plaza','West Hyattsville', 'Fort Totten', 'Georgia Ave-Petworth',
'Columbia', 'U St','Shaw-Howard U', 'Mt Vernon Sq', 'Gallery Place', 'Archives', 'LEnfant Plaza',
'Pentagon City', 'Crystal City', 'Ronald Reagon Washington National Airport', 'Braddock Rd'
'King St-Old Town']

silver_line = ['Wiehle-Reston East', 'Spring Hill', 'Greensboro', 'Tyson Corner',
'McLean', 'East Falls Church','Ballston-MU', 'Virginia Sq-GMU', 'Clarendon',
'Court House', 'Rosslyn', 'Foggy Bottom-GWU','Farragut West', 'McPherson Sq',
'Metro Center', 'Federal Triangle', 'Smithsonian','LEnfant Plaza', 'Federal Center SW',
'Capitol South', 'Eastern Market', 'Potomac Ave', 'Stadium-Armory', 'Benning Rd',
'Capitol Heights', 'Addison Rd', 'Morgan Blvd', 'Largo Town Center']

#Creating arrays of the metro color names and a list filled with the corresponding line station lists
line_name = ['Red', 'Orange', 'Blue', 'Green', 'Yellow', 'Silver']
line_list = [red_line, orange_line, blue_line, green_line, yellow_line, silver_line]

#Using the line names and their corresponding station lists and creating a dictionary
line_dict = {line_name[i] : line_list[i] for i in range(len(line_name))}
