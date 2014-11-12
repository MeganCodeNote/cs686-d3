d3.json("data/force.json", function(data) {
    var nodes = new Array();
    var width = 1400,
        height = 600,
        padding = 1.4,       // separation between same-color circles
        clusterPadding = 10, // separation between different-color circles
        maxRadius = 20,
        maxSize = 700;     // max size of college falculty

    var n = 0,    // total number of circles
        m = 0;     // number of distinct clusters

    var color = d3.scale.category20()
                  .domain(d3.range(m));

    // The largest node for each cluster.
    var clusters = new Array(m);

    n = Object.keys(data.values).length;
    m = Object.keys(data.states).length
    nodes = data.values.map(function(college){
        var i = college.state,
            r = college.size / maxSize * maxRadius,
            col = college.name,
            d = {cluster: i, radius: r, name: col};
        if (!clusters[i] || (r > clusters[i].radius)) clusters[i] = d;
        return d;   
    });
    var force = d3.layout.force()
                .nodes(nodes)
                .size([width, height])
                .gravity(0)
                .charge(0)
                .on("tick", tick)
                .start();

    var svg = d3.select("#body").append("svg")
        .attr("width", width)
        .attr("height", height);

    var circle = svg.selectAll("circle")
        .data(nodes)
        .enter()
        .append("circle")
        .attr("r", function(d) { return d.radius; })
        .style("fill", function(d) { return color(d.cluster); })
        .call(force.drag);

    circle.append("text")
        .attr("x", 12)
        .attr("dy", ".35em")
        .attr("font-size","1em")
        .text(function(d) { return d.name;});

    // var labels = svg.selectAll("text")
    //     .data(nodes)
    //     .enter()
    //     .append("text")
    //     // .attr("x", function(d){return d.x;})
    //     // .attr("y", function(d){return d.y;})
    //     .text(function(d){return d.name;})
    //     .call(force.drag);

    function tick(e) {
        circle.each(cluster(10 * e.alpha * e.alpha))
            .each(collide(.5))
            .attr("cx", function(d) { return d.x; })
            .attr("cy", function(d) { return d.y; });
    }

    // Move d to be adjacent to the cluster node.
    function cluster(alpha) {
      return function(d) {
        var cluster = clusters[d.cluster],
            k = 1;

        // For cluster nodes, apply custom gravity.
        if (cluster === d) {
          cluster = {x: width / 2, y: height / 2, radius: -d.radius};
          k = .1 * Math.sqrt(d.radius);
        }

        var x = d.x - cluster.x,
            y = d.y - cluster.y,
            l = Math.sqrt(x * x + y * y),
            r = d.radius + cluster.radius;
        if (l != r) {
          l = (l - r) / l * alpha * k;
          d.x -= x *= l;
          d.y -= y *= l;
          cluster.x += x;
          cluster.y += y;
        }
      };
    }

    // Resolves collisions between d and all other circles.
    function collide(alpha) {
      var quadtree = d3.geom.quadtree(nodes);
      return function(d) {
        var r = d.radius + maxRadius + Math.max(padding, clusterPadding),
            nx1 = d.x - r,
            nx2 = d.x + r,
            ny1 = d.y - r,
            ny2 = d.y + r;
        quadtree.visit(function(quad, x1, y1, x2, y2) {
          if (quad.point && (quad.point !== d)) {
            var x = d.x - quad.point.x,
                y = d.y - quad.point.y,
                l = Math.sqrt(x * x + y * y),
                r = d.radius + quad.point.radius + (d.cluster === quad.point.cluster ? padding : clusterPadding);
            if (l < r) {
              l = (l - r) / l * alpha;
              d.x -= x *= l;
              d.y -= y *= l;
              quad.point.x += x;
              quad.point.y += y;
            }
          }
          return x1 > nx2 || x2 < nx1 || y1 > ny2 || y2 < ny1;
        });
      };
    }
});
