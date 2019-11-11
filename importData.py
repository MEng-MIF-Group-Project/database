from pymongo import MongoClient
import argparse

parser = argparse.ArgumentParser(description='Database buider for the MIF group project')
parser.add_argument("--ip", default="127.0.0.1", type=str, help="The IP Address for the MongoDB server you are using")
parser.add_argument("--port", required=True, type=str, help="The port to connect on")
args = parser.parse_args()

# CHANGE THIS TO BE YOUR LOCAL URI
mongoURI = "mongodb://" + (args.ip).strip() + ":" + (args.port).strip() + "/admin"
client = MongoClient(mongoURI)

db = client.ElementData

path1 = './data/element_data.txt'
data1 = open(path1,'r')

path2 = './data/oxidation_states.txt'
data2 = open(path2,'r')

# Strip header
line = data1.readline()
while line != "#\n":
	line = data1.readline()
	pass

# Header line
headers = data1.readline().split()
headers[0] = headers[0].replace('#', '')

# Drop old collection
db.data.drop() 

# Grab all oxidation data for later searching
data2Lines = data2.readlines()

# Read element data line by line, format it, then insert into DB
for line in data1.readlines():
	eleData = line.split()

	# A really quite bad search for the matching oxidation state data
	for line in data2Lines:
		oxidationStates = line.split()

		if oxidationStates[0] == eleData[0]:
			eleData.append(oxidationStates[1:])

	# Structure data for DB insertion
	element = {
		headers[0] : eleData[0],
		headers[1] : eleData[1],
		headers[2] : eleData[2],
		headers[3] : eleData[3],
		headers[4] : eleData[4],
		headers[5] : eleData[5],
		headers[6] : eleData[6],
		headers[7] : eleData[7],
		headers[8] : eleData[8],
		headers[9] : eleData[9],
		headers[10] : eleData[10],
		headers[11] : eleData[11],
		"OxidationStates" : eleData[12]
	}

	# Insert into database
	result = db.data.insert_one(element)