from flask import Flask, render_template_string
from math import radians, sin, cos, sqrt, atan2
import geoguessr
import random

app = Flask(__name__)

def change_pos(lat,long,score=0):
    return """
    <!DOCTYPE html>
    <html>
    <head>
    <title>Draggable Street View</title>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCmMGjDepGn47mC7CdF_qakfGZqQ2Liy1k&callback=initMap" async defer></script>
    <style>
        #street-view-pano {


        }

        #map {


        }

        .item {

            width:1024px;
            height:600px;

        }

        .container{

            display:flex;
        }


    </style>

    </head>
    <body>
    <div class="container">

    <div class="item" id="street-view-pano">
    </div>
    <div class="item" id="map">
    </div>

    </div>

    <div id="output"></div>

    

    <button type="button" onclick="compare_results()">GUESS</button>

    <script>

        var marker = null;
        var answer_marker=null;
        var map=null;

        var initLat="""+str(lat)+""";
        var initLong="""+str(long)+""";
        console.log("InitLat: "+initLat+" InitLong: "+initLong)
        initLat = radians(initLat);
        initLong = radians(initLong);
        var finalLat;
        var finalLong;

        var score="""+str(score)+""";

        function initMap() {
        var panorama = new google.maps.StreetViewPanorama(
            document.getElementById('street-view-pano'),
            {
            position: {lat: """+str(lat)+""", lng: """+str(long)+"""}, // Specify the location
            pov: {heading: 0, pitch: 0}, // Initial point of view (optional)
            zoom: 1, // Zoom level (optional)
            //fullscreenControl: false, // Disable fullscreen control
            //showRoadLabels: false, // Hide location information
            //linksControl: false // Hide links to other locations
            //zoomControl: false, // Disable zoom control
            disableDefaultUI: true, // Disable default UI
            zoomControl: true, // Disable zoom control
            }
        );

        map = new google.maps.Map(document.getElementById("map"), {
            center: { lat: 0.0000, lng: 0.0000 }, // Initial center coordinates (e.g., Seattle)
            zoom: 1, // Initial zoom level
            disableDefaultUI: true, // Disable default UI
            zoomControl: true, // Disable zoom control
        });


        // Add a click event listener to capture the click coordinates
        google.maps.event.addListener(map, "click", function (event) {

            finalLat = event.latLng.lat();
            finalLong = event.latLng.lng();

            if (marker){
                marker.setMap(null);
            }

            marker = new google.maps.Marker({
                position: {lat: finalLat, lng: finalLong}, // Example marker position
                map: map,
                title: 'Hello World!'
            });
            
            console.log("Latitude: " + finalLat + ", Longitude: " + finalLong);
        });
        }
        

        // Include the computeDistance function from your separate script
        function computeDistance() {
            // Radius of the Earth in kilometers
            var R = 6371.0;

            // Convert latitude and longitude from degrees to radians
            finalLat = radians(finalLat);
            finalLong = radians(finalLong);

            // Compute the differences in coordinates
            var dlat = finalLat - initLat;
            var dlon = finalLong - initLong;

            // Haversine formula
            var a = Math.sin(dlat / 2) * Math.sin(dlat / 2) +
                    Math.cos(initLat) * Math.cos(finalLat) * Math.sin(dlon / 2) * Math.sin(dlon / 2);
            var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
            //var c = 2 * Math.asin(a);

            // Compute the distance
            var distance = R * c;

            return distance;
        }

        function radians(degrees) {
            return degrees * (Math.PI / 180);
        }

        function calc_score(distance){
            return Math.round(5000*(1.25)**(-0.005*distance));
        }

        function compare_results(){
            var dist=computeDistance();
            console.log("Distance: "+dist+" km");
            //var outputElement = document.getElementById("output"); // Assuming you have an element with id="output" where you want to display the text
            //outputElement.innerHTML = "Distance: " + dist + " km";
            alert('You scored '+String(calc_score(dist))+' points. Your total score is '+ String(score+calc_score(dist))+' !. You were '+String(Math.round(dist))+' km away!');
            score+=calc_score(dist);

            //NEW THING THAT PROBABLTY DOESN"T WORK
            if (answer_marker){
                answer_marker.setMap(null);
            }

            initLat=initLat * (180/Math.PI)
            initLong=initLong * (180/Math.PI)

            answer_marker = new google.maps.Marker({
                position: {lat: initLat, lng: initLong}, // Example marker position
                map: map,
                title: 'Hello World!'
            });

            var next_round = document.createElement('next_round');
            next_round.innerHTML = 'Next Round';
            next_round.className = 'custom-button';

            // Set inline styles for the button
            next_round.style.backgroundColor = '#ffffff'; // Background color
            next_round.style.border = '1px solid #000000'; // Border
            next_round.style.padding = '5px 10px'; // Padding
            next_round.style.cursor = 'pointer'; // Cursor style

            // Add click event listener to button
            next_round.addEventListener('click', function() {
                window.location.href = "http://127.0.0.1:5000/"+score;
            });

            // Append button to map container
            map.controls[google.maps.ControlPosition.TOP_LEFT].push(next_round);

            initLat=radians(initLat)
            initLong=radians(initLong)

            // Draw dashed line between markers
            var lineCoordinates = [
                marker.getPosition(), // Marker 1 position
                answer_marker.getPosition()  // Marker 2 position
            ];

            var lineSymbol = {
                path: 'M 0,-1 0,1',
                strokeOpacity: 1,
                scale: 1.5
            };

            line = new google.maps.Polyline({
                path: lineCoordinates,
                strokeOpacity: 0,
                icons: [{
                icon: lineSymbol,
                offset: '200',
                repeat: '10px'
                }],
                map: map
            });

            //var bounds = new google.maps.LatLngBounds();
            //bounds.extend(answer_marker.getPosition());
            //bounds.extend(marker.getPosition()); // Assuming marker is your other visible marker

            //map.fitBounds(bounds);

    //
            




        }

    </script>
    </body>
    </html>
    """

'''
def user_map():
    return """

    <!DOCTYPE html>
    <html>
    <head>
    <title>Google Maps Example</title>
    </head>
    <body>
    <div id="map" style="width: 600px; height: 450px;"></div>

    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCmMGjDepGn47mC7CdF_qakfGZqQ2Liy1k&callback=initMap" async defer></script>
    <script>
        function initMap() {
        const map = new google.maps.Map(document.getElementById("map"), {
            center: { lat: 42.8864, lng: -78.8784 }, // Initial center coordinates (e.g., Seattle)
            zoom: 14, // Initial zoom level
        });

        // Add a click event listener to capture the click coordinates
        google.maps.event.addListener(map, "click", function (event) {
            const lat = event.latLng.lat();
            const lng = event.latLng.lng();
            console.log("Latitude: " + lat + ", Longitude: " + lng);
        });
        }
    </script>
    </body>
    </html>

    """
'''

# HTML code from your previous example
'''rand_lat,rand_long=random.randint(-900000,900000)/10000,random.randint(-900000,900000)/10000
rand_lat,rand_long=random.randint(400000,420000)/10000,random.randint(-936250,-800000)/10000
if len(str(rand_lat)[3:])!=4:
    rand_lat=str(rand_lat)
    for i in range(4-len(str(rand_lat[3:]))):
        rand_lat+="0"
if len(str(rand_long)[3:])!=4:
    rand_long=str(rand_long)
    for i in range(4-len(str(rand_long[3:]))):
        rand_long+="0"'''

def next_round(score):
    global html_content

    coord=geoguessr.find_coordinates()
    while coord=="INVALID":
        coord=geoguessr.find_coordinates()
    print(coord)
    rand_lat,rand_long=coord[0],coord[1]

    html_content = change_pos(rand_lat,rand_long,score)
    print("LATITUDE: ",rand_lat)
    print("LONGITUDE: ",rand_long)

@app.route('/')

@app.route("/<int:post_id>")

def render_street_view(post_id=None):
    if post_id==None:
        next_round(0)
    else:
        next_round(post_id)
    return render_template_string(html_content)

if __name__ == '__main__':
    print("HELLO WORLD")
    #app.run(debug=True)
    app.run(debug=False)
    #app.run(debug=True,use_reloader=False)
