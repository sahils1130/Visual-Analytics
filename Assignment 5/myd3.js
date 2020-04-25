chart = {

  const svg = d3.create("svg")
      .attr("viewBox", [0, 0, width, height]);

  svg.append("g")
      .call(grid);

  svg.append("g")
      .call(xAxis);

  svg.append("g")
      .call(yAxis);

  const clipId = DOM.uid("clip");

  svg.append("clipPath")
      .attr("id", clipId.id)
    .append("rect")
      .attr("x", x.range()[0])
      .attr("width", 0)
      .attr("height", height)
    .transition()
      .duration(5000)
      .ease(d3.easeQuadOut)
      .attr("width", x.range()[1] - x.range()[0]);

  svg.append("g")
      .attr("fill", "none")
      .attr("stroke-miterlimit", 1)
      .attr("stroke-width", 2)
      .attr("clip-path", clipId)
    .selectAll("path")
    .data(d3.groups(data, d => d.name))
    .join("path")
      .attr("stroke", ([name]) => z(name))
      .attr("d", ([name, d]) => line(d));

  svg.append("g")
      .attr("font-family", "sans-serif")
      .attr("font-size", 10)
      .attr("font-weight", "bold")
      .attr("text-anchor", "start")
    .selectAll("text")
    .data(d3.groups(data, d => d.name).map(([, group]) => group.shift()))
    .join("text")
      .attr("fill", d => z(d.name))
      .attr("x", d => x(d.date))
      .attr("y", d => y(d.value))
      .attr("dy", "1.2em")
      .text(d => d.name);

  return svg.node();
}

data = Object.assign(d3.csvParse(await FileAttachment("labor-force.csv").text(), ({code, year, month, value}) => ({name: code === "M" ? "Men" : code === "W" ? "Women" : "Overall", date: new Date(Date.UTC(year, month - 1)), value: value / 100})), {y: "↑ Participation rate"})

line = d3.line().x(d => x(d.date)).y(d => y(d.value))

x = d3.scaleUtc(d3.extent(data, d => d.date), [margin.left, width - margin.right])
y = d3.scaleLinear([0, 1], [height - margin.bottom, margin.top])

z = d3.scaleOrdinal(["Overall", "Men", "Women"], ["currentColor", "#4e79a7", "#e15759"])

xAxis = g => g
    .attr("transform", `translate(0,${height - margin.bottom})`)
    .call(d3.axisBottom(x).ticks(width / 80).tickSizeOuter(0))

yAxis = g => g
    .attr("transform", `translate(${margin.left},0)`)
    .call(d3.axisLeft(y).ticks(null, "%"))
    .call(g => g.select(".domain").remove())
    .call(g => g.append("text")
        .attr("x", -margin.left)
        .attr("y", 10)
        .attr("fill", "currentColor")
        .attr("text-anchor", "start")
        .text(data.y))

grid = g => g
    .attr("stroke", "currentColor")
    .attr("stroke-opacity", 0.1)
    .call(g => g.append("g")
      .selectAll("line")
      .data(y.ticks())
      .join("line")
        .attr("y1", d => 0.5 + y(d))
        .attr("y2", d => 0.5 + y(d))
        .attr("x1", margin.left)
        .attr("x2", width - margin.right));

    height = 500
    margin = ({top: 30, right: 20, bottom: 20, left: 40})

    d3 = require("d3@5", "d3-array@2")

