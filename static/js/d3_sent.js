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

// var svg = d3.select(".chart")
//   .append("svg")
//   .attr("height", svgHeight)
//   .attr("width", svgWidth);

// var chartGroup = svg.append("g")
//   .attr("transform", `translate(${margin.left}, ${margin.top})`);

// either works!
// url = "http://127.0.0.1:5000/hashtag2020"

// Create function to determine marker size based on magnitude
function markerSize(magnitude){
  // if (magnitude === 0){
  //     return 1;
  // }
  // else {
  return magnitude *5;
  // }
};

function markerColor(pol_avg){
  if (pol_avg > 0) {
      return 'blue';
  }
  else if (pol_avg < 0) {
      return 'red';
  }
  else {
      return 'white';
  }
};

// Function to add marker with style options
// function addMarker (feature, location){
//   var options = {
//       stroke: true,
//       weight: .5,
//       fillOpacity: 0.8,
//       color: "black",
//       fillColor: markerColor(feature.geometry.coordinates[2]),
//       radius: markerSize(feature.properties.mag)
//   }


bavg_url = "/bidenavg"
tavg_url = "/trumpavg"
bcount_url ="/bidencount" 
tcount_url = "/trumpcount"


d3.json(bavg_url).then(function(data) {
  console.log(data);
})

d3.json(tavg_url).then(function(data) {
  console.log(data);
})

d3.json(bcount_url).then(function(data) {
  console.log(data);
})

d3.json(tcount_url).then(function(data) {
  console.log(data);
})