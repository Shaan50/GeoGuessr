import requests
import json
import os
import random
from PIL import Image

file_path=os.path.join(os.path.dirname(__file__))

def find_coordinates():

    #rand_lat,rand_long=random.randint(-900000,900000)/10000,random.randint(-900000,900000)/10000
    
    continent=random.randint(1,6)
    if continent==1:
        rand_lat=random.randint(82794,598063)/10000
        rand_long=random.randint(-1349433,-802109)/10000
    if continent==2:
        rand_lat=random.randint(-556772,124376)/10000
        rand_long=random.randint(-813191,-348088)/10000
    if continent==3:
        rand_lat=random.randint(252048,534808)/10000
        rand_long=random.randint(-91393,376173)/10000
    if continent==4:
        rand_lat=random.randint(-84595,320589)/10000
        rand_long=random.randint(751449,1232173)/10000
    if continent==5:
        rand_lat=random.randint(-321123,-237773)/10000
        rand_long=random.randint(242578,315528)/10000
    if continent==6:
        rand_lat=random.randint(-426395,-228832)/10000
        rand_long=random.randint(1327466,1766040)/10000


    print(rand_lat,rand_long)
    
    if len(str(rand_lat)[3:])!=4:
        rand_lat=str(rand_lat)
        for i in range(4-len(str(rand_lat[3:]))):
            rand_lat+="0"
    if len(str(rand_long)[3:])!=4:
        rand_long=str(rand_long)
        for i in range(4-len(str(rand_long[3:]))):
            rand_long+="0"

    # Define the URL with your API key and query parameters
    api_key="YOUR API KEY"
    #url="https://www.google.com/maps/embed/v1/place?key="+api_key+"&q=Space+Needle,Seattle+WA"
    url=f'https://maps.googleapis.com/maps/api/streetview?size=400x400&location={rand_lat},{rand_long}&key={api_key}'



    #jsonData=requests.get(url).json()
    response=requests.get(url)

    #print(response.content)
    #print(response.content.decode('utf-8'))

    with open('streetview_image.jpg', 'wb') as file:
        file.write(response.content)

    '''data = json.loads(response.content)

    with open(file_path+"\\street_view_data.json",'w') as outfile:
        json.dump(data,outfile)'''

    image=Image.open("streetview_image.jpg","r")
    width,height=image.size
    pixel_values=list(image.getdata())
    if pixel_values[0]==(228, 227, 223):
        return "INVALID"
    else:
        return (rand_lat,rand_long)

#find_coordinates()
