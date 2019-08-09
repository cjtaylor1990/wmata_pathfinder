# wmata_pathfinder
This is a fun side project where I'm going to use a graph structure to represent the WMATA metro system in Washington,DC. 
I will use graph searches to then find a path between stations. 
Currently uses a slightly tailored depth-first search algorithm that is biased against switching train lines, as you would want in a tool like this.

This repository uses Python 3.6.5

First, you must build the metro graph object which will be stored in a pickle (wmata.p):
python build_metro.py

After that, the program can be used:
python pathfinder.py

It will then ask you where you are going and where you are headed. It will then give you start and end locations for each line
until you reach the designated destination.
