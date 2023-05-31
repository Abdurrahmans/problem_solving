var myString = "this is my home abdur rahman";


let myObject={};
function strToObj(data){
    for (let i=0; i<data.length; i++) {
        console.log(i);
     myObject[data[i]] = data[i].length;
     console.log(myObject);

    }
console.log(myObject);
return myObject;
}
var myArray = strToObj(myString.split(" "));
console.log("output", JSON.stringify(myArray))