# ELVA AI Test
## This repository was made as part of a technical interview process, below you will find how to run the script and the goal of each step + thought process behind the solution.
### Author: Juan Martin Uribe

## 1. "Geocoding" : calculate the coordinate location given an address
For this step refer the `GoogleMapsController.py` file.

This step was done using the Google Maps API provided by google, if you want to run the script make sure to get an api key 
https://github.com/googlemaps/google-maps-services-python

Working with google maps API was very straightforward and easy to implement, once the package was installed and imported, I created a class that initiates the client and has a method to go from an address to latitude/longitude. It receives an address as parameter and returns a length 2 array with the longitude and latitude.

![image](https://github.com/JuanMartinUribe/ELVATest/assets/53051383/ec1a9fc6-1549-478d-be36-96e5fe327d12)

**_I did not have any problems working with this API, it is properly documented and has a variety of examples on different technologies._**
## 2. Using ArcGis REST services in order to go from coordinates to neighborhood
For this step refer the `ArcController.py` file.

This step was done using the ArcGis API provided in the test's instructions. 
https://www.portlandmaps.com/arcgis/rest/services/Public/COP_OpenData/MapServer/125/query

This was the toughest step in the whole process, Arc's API documentation is extensive but in my experience it was hard to understand and implement certain requests to get the information needed.

After a long hour of going trough it's documentation I could only come up with one solution: 

**Send a request to receive all neighborhoods in the respective region and check each neighborhood's ring vortices in order to determine if the coordinates are inside it**

According to Arc's documentation, each neighborhood is represented as a shape, in this case a polygon. After sending a request to the endpoint, I was able to get each neighborhood's "ring" as two dimensional array of vortices. Finally, I used a third party library in order to determine if the coordinates gotten from google maps API lied within a neighborhood.

![image](https://github.com/JuanMartinUribe/ELVATest/assets/53051383/8a5954e0-9be0-4fe7-ba20-bb6cf66610fc)

**_This step took me the longest, I did not find Arc's API to be easy to understand/work with but they did have a lot of documentation_**

## 3. The neighborhood
For this step refer lines 11-18 in the `main.py` file

This step is a combination of the two steps above, given the address "1300 SE Stark Street, Portland, OR 97214":
1. I used google maps API to convert the address to coordinates
2. Use Arc's API to get a list of the neighborhoods and their "rings", then check if the coordinates lie within one of the neighborhoods.
This was the outcome:
![image](https://github.com/JuanMartinUribe/ELVATest/assets/53051383/793d83fa-34f4-4e69-888d-9a5c39ad2d96)
### The coordinates I got from google maps API were **lng:-122.652102, lat:45.5189567**,
### These coordinates lied within one of the neighborhood's "ring" gotten from Arc's API : **BUCKMAN**

## 4. Recursive function that finds the next neighborhood
For this step refer the `main.py` file

This step was interesting because it was not hard to solve but I found it hard to make the code readable/organized.

The import aspect to keep in mind is that the recursive method references the `Gmaps` and `Arc` instances in order to get the coordinates + neighborhood each time the method is called. 

![image](https://github.com/JuanMartinUribe/ELVATest/assets/53051383/72c7a9ec-9882-40ef-903c-9650602d6db4)

_The method adds 100 to the street in the address and calculates the new address's coordinates, then the neighborhood of those coordinates and :_

`If the new neighborhood != initial neighborhood : return new neighborhood,`

`else : return recursive(initial neighborhood, new address)`

## 5. First different neighborhood
For this step refer the `main.py` file

**If we combine all of the previous steps in order to calculate the first address that belongs to a different neighborhood by adding 100 recursively to it's street number :**

![image](https://github.com/JuanMartinUribe/ELVATest/assets/53051383/1a0ebf26-602b-4575-860d-9fd63e14cf0c)

#### we get that the first street that belongs to a different neighborhood is "2800 SE Stark Street, Portland, OR 97214" in SUNNYSIDE

**_... and the whole output of the script is:_**

![image](https://github.com/JuanMartinUribe/ELVATest/assets/53051383/7025dc00-7055-430a-a12c-3719609606b6)
