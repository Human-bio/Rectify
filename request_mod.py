import csv
import json
import requests
import os.path 
online = True


class request:
    
    def __init__(self,name,Method, url, data, headers, params,response="Default"):
        self.Method = Method
        self.url = url
        self.data = data
        self.headers = headers
        self.params = params
        self.name = name
        try:
            self.response = response = (((str(requests.request(Method, url, data=data, headers=headers, params=params).text))))
        except:
            self.response = "an error has occoured"
        
  

def filter(jsondata,*braces):
    filterout = jsondata
    for key in jsondata:
        for brace in braces:
            filterout = (filterout[brace])

    return filterout
def askinput():
    return input("your options \n 1. save request \n2. show output \n [1,2]")
def requestandsave():
    
    b=askinput()
    if b=="1":
        csv_columns = ["name","Method", "url", "data", "headers", "params","response"]

        with open("requests.csv", 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            if not os.path.isfile("requests.csv"):
                writer.writeheader()
            writer.writerow(name.__dict__)
        

    elif b=="2":
        print(name.response)
    else: 
        print("Choose one of the option's please")
        requestandsave()
i = 1

while online:

    input("welcome to rectify design api tool")
    a = input("a. send requests -- not yet available b. get prevuise requests")
    name,Method, url,function, data, headers, params = input(""),input(""),input(""),input(""),input(""),input(""),input("")
    name = request(name=name,Method=Method, url=url+function, data=data, headers=headers, params=params)

    if a.upper() in ['A']:
        requestandsave()

