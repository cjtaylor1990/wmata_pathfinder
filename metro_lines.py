red_line = ['Glenmont', 'Wheaton', 'Forest Glen', 'Silver Spring', 'Takoma Park',
'Fort Totten', 'Brookland-CUA', 'Rhode Island Ave', 'NoMa-Gallaudet U',
'Union Station', 'Judiciary Sq', 'Gallery Place', 'Metro Central', 'Farragut North',
'Dupoint Circle', 'Woodley Park', 'Cleveland Park', 'Van Ness-UDC', 'Tenleytown-AU',
'Friendship Heights', 'Bethesda', 'Medical Center', 'Grosvenor-Strathmore', 'White Flint',
'Twinbrook', 'Rockville', 'Shady Grove']

green_line = ['Greenbelt', 'College Park-U of Md',
'Prince Georges Plaza','West Hyattsville', 'Fort Totten', 'Georgia Ave-Petworth',
'Columbia', 'U St','Shaw-Howard U', 'Mt Vernon Sq', 'Gallery Place', 'Archives', 'LEfant Plaza',
'Waterfront', 'Navy Yard-Ballpark', 'Anacostia', 'Congress Heights', 'Southern Ave',
'Naylor Rd', 'Suitland', 'Branch Ave']

line_name = ['Red', 'Green']
line_list = [red_line, green_line]

line_dict = {line_name[i] : line_list[i] for i in range(len(line_name))}
