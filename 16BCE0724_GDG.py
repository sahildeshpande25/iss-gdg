import json
import turtle as tr
import urllib.request
import time

#To get the names of the people on the ISS
api1='http://api.open-notify.org/astros.json'
response=urllib.request.urlopen(api1)
result=json.loads(response.read())
print('\nThere are ',result['number'],' people in space right now')
print('The names of the people in space right now are: \n')
iss_people=result['people']
for i in iss_people:
	print(i['name'])

#To get the geogrophical coordinates of the ISS
api2="http://api.open-notify.org/iss-now.json"
response=urllib.request.urlopen(api2)
result=json.loads(response.read())
location=result['iss_position']
latitude=float(location['latitude'])
longitude=float(location['longitude'])
print('\nLatitude: ',latitude)
print('Longitude: ',longitude,'\n')

#Setting up the display on the screen
display=tr.Screen()

#Fitting the screen according to the image dimensions
display.setup(850,533)

#Setting latitudes and longitudes on the map
display.setworldcoordinates(-180,-90,180,90)

#Setting World Map as the background image
display.bgpic('world_map.gif')
display.register_shape('marker.gif')
iss_tur=tr.Turtle()
iss_tur.shape('marker.gif')
iss_tur.setheading(90)
iss_tur.penup()
iss_tur.goto(longitude,latitude)
style=('Times New Roman',15,'bold')

#Display date and time
iss_tur.write(time.ctime(),font=style)

#Random input taken to prevent map from closing immediately
i=input()
