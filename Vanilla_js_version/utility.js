function generateValues(mySum,myYs) {
    return myYs.map((x,index) => {
      const element = convertToPercentages(x, mySum)
      return {name: `${element}-${index}`, value: element}
    });
  }
  
  // this function generates the y values according to the slope. the x values are the natural numbers from 1 to n.
  function generate_y(slope,element_count) {
    let yList = []
    for (let i = 1; i < element_count+1; i++) {
        yList.push(slope * (i - (element_count/2))+1)
    }
    return yList
  }
  function convertToPercentages(x, mySum) {
    return Math.round((x / mySum) * 10000) / 100;
  }
  
  function getYLimit(element_count) {
    const x_center = element_count / 2;
    const y_center = 1;
    const start_x = 1;
    const start_y = 0;
  
    const to_limit = (start_y - y_center) / (start_x - x_center);
  
    const y = to_limit * element_count + (-to_limit * 1);
    const totalSum = element_count / 2 * (to_limit * element_count - to_limit);
    const yLimit = y / totalSum * 100;
    return yLimit
  }
  
  export function getSlope(m_norm, element_count) {
    const x_center = element_count / 2;
    const y_center = 1;
    const start_x = 1;
    const start_y = 0;
    const end_x = element_count;
    const end_y = 0;
  
    const to_limit = (start_y - y_center) / (start_x - x_center);
    const from_limit = (end_y - y_center) / (end_x - x_center);
    const m = m_norm * (to_limit - from_limit) + from_limit;
    return m;
  }
  
  // Function to generate and process data
  export function processData(element_count,m) {
    
    const yLimit = getYLimit(element_count)
    const myYs = generate_y(m, element_count)
    const mySum = myYs.reduce((a, b) => a + b, 0)
    const data = generateValues(mySum, myYs);
  
    return { data, yLimit };
  }