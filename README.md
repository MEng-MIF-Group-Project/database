# Group Project Database
This repo contains all default data for the database with python setup scripts so you can quickly rebuild a broken DB or setup your own dev enviroment.

## Setup
I did this on MacOS but it should be fairly portable, if its not working for you give me an email/message.

1. Install Docker for your OS (~~Sorry Cristian~~)

2. Install Python 3.2 or later

3. Install MongoDB via Docker `docker pull mongo`

4. Run `python3 -m pip install pymongo` for the mongo python library

5. Start a local MongoDB instance `docker run -P --name mongo-dev -d mongo`
	- `-P` to expose ports for you to connect to
	- `--name` sets the Docker container name to something memorable instead of a hex string
	- `-d mongo` uses the mongo container we pulled in step 2
	
6. Run `docker ps -a` and note the port number your mongo instance is running on

7. Run `python3 -m pip install pymongo` for the mongo python library

8. `python3 installData.py --port <PORT NUMBER>` to build database

	Note: the script **will** drop the ElementData.data collection, do not run it if you do not want to completely reset your local ElementData