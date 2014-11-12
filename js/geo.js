d3.json("data/geo.json", function(geodata){
    console.log(geodata)
    var max_size = geodata['max']
    var data = geodata['states']
    console.log(data)   
    function tooltipHtml(n, d){ /* function to create html content string in tooltip div. */
        return "<h4>"+n+"</h4><table>"+
            "<tr><td>Number of Colleges</td><td>"+(d.num_colleges)+"</td></tr>"+
            "<tr><td>Total Faculty</td><td>"+(d.num_falcuty)+"</td></tr>"+
            "</table>";
    }

    var sampleData ={}; 
    ["HI", "AK", "FL", "SC", "GA", "AL", "NC", "TN", "RI", "CT", "MA",
    "ME", "NH", "VT", "NY", "NJ", "PA", "DE", "MD", "WV", "KY", "OH", 
    "MI", "WY", "MT", "ID", "WA", "DC", "TX", "CA", "AZ", "NV", "UT", 
    "CO", "NM", "OR", "ND", "SD", "NE", "IA", "MS", "IN", "IL", "MN", 
    "WI", "MO", "AR", "OK", "KS", "LS", "VA"]
        .forEach(function(state){ 
            sampleData[state] = {'num_colleges':0, 'num_falcuty':0, 'color':d3.interpolate("#ffffcc", "#6835A6")(0)}
            if (data[state]) {
                var num = data[state]['num_falcuty']
                sampleData[state]['num_colleges'] = data[state]['num_colleges']
                sampleData[state]['num_falcuty'] = num
                sampleData[state]['color'] = d3.interpolate("#F2947E", "#6503A6")(num / max_size)
            }
        });

    /* draw states on id #statesvg */   
    uStates.draw("#statesvg", sampleData, tooltipHtml);
});