// // SVG wrapper dimensions are determined by the current width
// // and height of the browser window.
// var svgWidth = 1200;
// var svgHeight = 660;

// var margin = {
//   top: 50,
//   right: 50,
//   bottom: 50,
//   left: 50
// };

// var height = svgHeight - margin.top - margin.bottom;
// var width = svgWidth - margin.left - margin.right;

// var svg = d3.select("#sentmapid")
//   .append("svg")
//   .attr("height", svgHeight)
//   .attr("width", svgWidth);

// var chartGroup = svg.append("g")
//   .attr("transform", `translate(${margin.left}, ${margin.top})`);


// count_url ="/sentcounts" 


// d3.json(count_url).then(function(data) {
//   console.log(data)

//   var trace1 = {
//     x: data.map(row => row.analysis), 
//     y: data.map(row => row.Biden_Count),
//     name: 'Biden',
//     type: 'bar',
//     marker:{color:'blue'}
//   };

//   var trace2 = {
//     x: data.map(row => row.analysis), 
//     y: data.map(row => row.Trump_Count),
//     name: 'Trump',
//     type: 'bar',
//     marker:{color:'red'}
//   };

//   var data = [trace1, trace2];

//   var layout = {
//     title: "Biden vs Trump Hashtag Tweet Sentiment",
//     xaxis: { title: "Sentiment Category" },
//     yaxis: { title: "Count of Tweets"}
//   };

//   Plotly.newPlot("sentcount", data, layout);
// });

/////////////////////////////////////////////////////////////////////////

// // // Create function to determine marker size based on magnitude
// function markerSize(polarity){
//   if (polarity === 0){
//       return 1;
//   }
//   else {
//     return polarity *75;
//   }
// };

// function markerColor(Pol_Avg){
//   if (Pol_Avg > 0) {
//       return 'blue';
//   }
//   else if (Pol_Avg < 0) {
//       return 'red';
//   }
//   else {
//       return 'white';
//   }
// };

// // // Function to add marker with style options
// // function addMarker (feature, location){
// //   var options = {
// //       stroke: true,
// //       weight: .5,
// //       fillOpacity: 0.5,
// //       color: "black",
// //       fillColor: markerColor(feature.coordinates),
// //       radius: markerSize(feature.Pol_Avg)
// //   }
// //   return L.circleMarker(location, options);
// // };


// function addPopup (feature, layer) {
//   return layer.bindPopup("<h3>" + feature.city +", " + feature.state_code + "</h3><hr><p>" + "Polarity: " + feature.Pol_Avg + "</p>");
// };

// bavg_url = "/bidenavg"
// tavg_url = "/trumpavg"

// var bidenMarkers = [];
// var trumpMarkers = [];

// d3.json(bavg_url).then(function(location) {
//   bidenMarkers.push(
//     L.circle(location.coordinates, {
//       stroke: false,
//       fillOpacity: 0.75,
//       color: markerColor(location.Pol_Avg),
//       fillColor: markerColor(location.Pol_Avg),
//       radius: markerSize(location.Pol_Avg)
//     })
//   );
// });

// d3.json(tavg_url).then(function(location) {
//   console.log(location)
//   trumpMarkers.push(
//     L.circle(location.coordinates, {
//       stroke: false,
//       fillOpacity: 0.75,
//       color: markerColor(location.Pol_Avg),
//       fillColor: markerColor(location.Pol_Avg),
//       radius: markerSize(location.Pol_Avg)
//     })
//   );
// });



// // function createMap(sentimentmap) {

  // Create the tile layer that will be the background of our map
// var streetmap = L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
//   attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
//   tileSize: 512,
//   maxZoom: 18,
//   zoomOffset: -1,
//   id: "mapbox/streets-v11",
//   accessToken: API_KEY
// });

// var biden = L.layerGroup(bidenMarkers);
// var trump = L.layerGroup(trumpMarkers);

  // Create a baseMaps object to hold the lightmap layer
// var baseMaps = {
//   "USA Cities": streetmap
// };

//   // Create an overlayMaps object to hold the bikeStations layer
// var overlayMaps = {
// //   "Biden Sentiment" : biden,
// //   "Trump Sentiment" : trump
    
// };

  // Create the map object with options
// var map = L.map("sentmapid", {
//   center: [40.73, -74.0059],
//   zoom: 12,
//   layers: [streetmap]
// });

  // Create a layer control, pass in the baseMaps and overlayMaps. Add the layer control to the map
// L.control.layers(baseMaps,).addTo(map);

/////////////////////////////////////////////

// bavg_url = "/bidenavg"
// tavg_url = "/trumpavg"


// d3.json(bavg_url).then(function(data) {
//   console.log(data)
//   data.
// });

// // Create a map object
// var myMap = L.map("sentmapid", {
//   center: [15.5994, -28.6731],
//   zoom: 3
// });

// L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
//   attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
//   tileSize: 512,
//   maxZoom: 18,
//   zoomOffset: -1,
//   id: "mapbox/streets-v11",
//   accessToken: API_KEY
// }).addTo(myMap);
