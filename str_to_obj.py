import json
myString = "this is my home abdur rahman";
obj = dict()
def strToObj(data):
    for i in range(len(data)):
        obj[data[i]] = len(data[i])
    return obj
   
mydata = strToObj(myString.split(" "))
print("OutPUT",json.dumps(mydata))

