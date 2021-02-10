// // Create function to determine marker size based on magnitude
// function markerSize(magnitude){
//   // if (magnitude === 0){
//   //     return 1;
//   // }
//   // else {
//   return magnitude *5;
//   // }
// };

// function markerColor(pol_avg){
//   if (pol_avg > 0) {
//       return 'blue';
//   }
//   else if (pol_avg < 0) {
//       return 'red';
//   }
//   else {
//       return 'white';
//   }
// };

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


// bavg_url = "/bidenavg"
// tavg_url = "/trumpavg"
count_url ="/sentcounts" 


d3.json(count_url).then(function(data) {
  console.log(data)

  var trace1 = {
    x: data.map(row => row.analysis), 
    y: data.map(row => row.Biden_Count),
    name: 'Biden',
    type: 'bar',
    marker:{color:'blue'}
  };

  var trace2 = {
    x: data.map(row => row.analysis), 
    y: data.map(row => row.Trump_Count),
    name: 'Trump',
    type: 'bar',
    marker:{color:'red'}
  };

  var data = [trace1, trace2];

  var layout = {
    title: "Biden vs Trump Hashtag Tweet Sentiment",
    xaxis: { title: "Sentiment Category" },
    yaxis: { title: "Count of Tweets"}
  };

  Plotly.newPlot("sentcount", data, layout);
});


