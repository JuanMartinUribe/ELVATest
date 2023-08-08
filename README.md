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
For this step refer to the `ArcController.py` file.

This step was done using the ArcGis API provided in the test's instructions. 
https://www.portlandmaps.com/arcgis/rest/services/Public/COP_OpenData/MapServer/125/query

This was the toughest step in the whole process, Arc's API documentation is extensive but in my experience it was hard to understand and implement certain requests to get the information needed.

After a long hour of going trough it's documentation I could only come up with one solution: 

**Send a request to receive all neighborhoods in the respective region and check each neighborhood's ring vortices in order to determine if the coordinates are inside it**

According to Arc's documentation, each neighborhood is represented as a shape, in this case a polygon. After sending a request to the endpoint, I was able to get each neighborhood's "ring" as two dimensional array of vortices. Finally, in order to determine if the coordinates gotten from google maps API lied within a neighborhood I used a third party library.

![image](https://github.com/JuanMartinUribe/ELVATest/assets/53051383/8a5954e0-9be0-4fe7-ba20-bb6cf66610fc)
