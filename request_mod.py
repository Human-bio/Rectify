import json
import requests
from time import perf_counter 
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
        with open('alphavantageapi/request.txt','a') as requestssave:

            json.dump(name.__dict__, requestssave,ensure_ascii=False, indent=4)
            


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

