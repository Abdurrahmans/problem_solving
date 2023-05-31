const data =[2,7,11,4,-2];
const sum = data.reduce((a,b)=>a+b,0);
console.log(sum)
output = data.map(item=>sum-item)
console.log(output)