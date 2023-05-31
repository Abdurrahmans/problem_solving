const input  = "This is javascript code";
const arrOfStr = input.split(" ")
const strReverse = arrOfStr.map(item=>
    item.split('').reverse().join("")).join(' ')
console.log(strReverse);