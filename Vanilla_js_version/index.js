import { processData, getSlope } from "./utility.js";
// Get a reference to the element count slider and the slope slider
let sliderElementCount = document.getElementById("element_count");
let sliderSlope = document.getElementById("slope");

// Define the dimensions of the graph
let width = window.innerWidth - 300;
let height = 500;
let padding = 50;

// Create the SVG container
let svg = d3.select(".graph").append("svg")
  .attr("width", width)
  .attr("height", height + padding);

// Define the scales
let x = d3.scaleBand()
  .range([0, width])
  .padding(0.2);

let y = d3.scaleLinear()
  .range([height, 0]);

// Append the x axis to the SVG (without call)
let xAxis = svg.append("g")
  .attr("class", "xAxis")
  .attr("transform", "translate(0," + height + ")");

// Append the y axis to the SVG (without call)
let yAxis = svg.append("g")
  .attr("class", "yAxis");

function generateHtml(d) {
  
  let [whole, fractional] = d.value.toFixed(2).split('.');
  //
  fractional = fractional || '00';
  return `<div class="number">
            <span class="percent">%</span>
            <span class="whole">${whole}</span>
            <span class="decimal">.</span>
            <span class="fraction">${fractional.padEnd(2, ' ')}</span>
          </div>`;
}

function updateLabels(data) {
  xAxis.call(d3.axisBottom(x).tickFormat(""))
  .selectAll("foreignObject")
  .data(data)
  .join(
    enter => enter.append("foreignObject")
      .attr("y", 0)
      .attr("x", d => x(d.name))
      .attr("width", x.bandwidth())
      .attr("height", 40)
      .append("xhtml:body")
      .html(generateHtml), // use generateHtml function here
    update => update
      .attr("x", d => x(d.name))
      .attr("width", x.bandwidth())
      .attr("height", 40)
      .select("body")
      .html(generateHtml), // and here
    exit => exit.remove()
  );
}
// Function to update the bars
function updateBars(data) {

  svg.selectAll(".bar")
    .data(data, d => d.name)
    .join(
      enter => enter.append("rect")
        .attr("class", "bar")
        .attr("x", d => x(d.name))
        .attr("y", d => y(d.value))
        .attr("width", x.bandwidth())
        .attr("height", d => height - y(d.value))
        .attr("fill", "steelblue"),
      update => update
        .attr("x", d => x(d.name))
        .attr("y", d => y(d.value))
        .attr("width", x.bandwidth())
        .attr("height", d => height - y(d.value))
        .attr("fill", "steelblue"),
      exit => exit.remove()
    );
}
// Function to update the axes
function updateAxes(data, yLimit) {
  // Update the scales
  x.domain(data.map(d => d.name));
  y.domain([0, yLimit]);

  // Update the axes
  let tickValues = d3.range(0, yLimit, 5);
  if (yLimit % 5 !== 0) {
    tickValues.push(yLimit);
  }

  yAxis.transition().duration(200).call(d3.axisLeft(y).tickValues(tickValues));
}
// Function to draw the bars
function drawBars() {
  const element_count = parseInt(sliderElementCount.value);
  const m = getSlope(parseFloat(sliderSlope.value), element_count);

  const { data, yLimit } = processData(element_count,m);

  updateAxes(data, yLimit);
  updateLabels(data);
  updateBars(data);
}

drawBars();

// Update the graph on window resize
window.addEventListener("resize", function() {
  width = window.innerWidth;
  x.range([0, width]);
  svg.attr("width", width);
  drawBars();
});

// Update the graph when the slider value changes
sliderElementCount.addEventListener("input", function() {
  drawBars();
});

// Update the graph when the slider value changes
sliderSlope.addEventListener("input", function() {
  drawBars();
});