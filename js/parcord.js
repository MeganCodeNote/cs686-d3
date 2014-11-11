var pc_progressive;

// load csv file and create the chart
d3.csv('data/houses.csv', function(data) {
    var colorgen = d3.scale.category20();
    var colors = {
        0: "#CF7EF2",
        1: "#A5F26D",
        2: "#F27EA8",
        3: "#04D9D9",
        4: "#F2DA91",
        5: "#73D99F"
    }
    var color = function(d) { 
        var colorkey = Math.floor(d['median house value'] / 100000);
        return colors[colorkey]; 
    };

    pc_progressive = d3.parcoords()("#house")
        .data(data)
        .color(color)
        .alpha(0.4)
        .margin({ top: 24, left: 150, bottom: 12, right: 0 })
        .mode("queue")
        .render()
        .brushMode("1D-axes")  // enable brushing
        .interactive()         // command line mode
        .reorderable()
        .rate(150)

    pc_progressive.svg.selectAll("text")
        .style("font", "10px sans-serif");
});