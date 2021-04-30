import json
import requests
from time import perf_counter 

class request:
    
    def __init__(self,Method, url, data, headers, params,response="Default"):
        self.Method = Method
        self.url = url
        self.data = data
        self.headers = headers
        self.params = params
        try:
            self.response = response = (((str(requests.request(Method, url, data=data, headers=headers, params=params).text))))
        except:
            self.response = "time overload"
        
  

def filter(jsondata,*braces):
    filterout = jsondata
    for key in jsondata:
        for brace in braces:
            filterout = (filterout[brace])

    return filterout
    
        
