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
        
  
def getprevuisrequest():
        
        with open('requests.csv') as data:
            reader = csv.reader(data)
            for row in reader:
                print(row)
        print

def filter(jsondata,*braces):
    filterout = jsondata
    for key in jsondata:
        for brace in braces:
            filterout = (filterout[brace])

    return filterout
def showoptions():
    return input("your options \n 1. save request \n2. show output \n [1,2] ")
def requestandsave():
    name,Method, url,function, data, headers, params = input("name of the request "),input("request method "),input("request url "),input("request function or query "),input("request data "),input("request headers "),input("request parameters ")
    name = request(name=name,Method=Method, url=url+function, data=data, headers=headers, params=params)
    b=showoptions()
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
input("welcome to rectify design api tool \n")
while online:

    a = input("a. send requests  b. get prevuise requests c.leave network")
    
    if a.upper() in ['A']:
        requestandsave()
    if a.upper() in ['B']:
        getprevuisrequest()
    if a.upper() in ['C']:
        online = False