import json
import requests
try:
    import config 
except:
    print("Config file was not found \n please create a config file with the name config and add a variable __apikey__ with your respective api key")
class request:
    
    def __init__(self,Method, url, data, headers, params,response="Default"):
        self.Method = Method
        self.url = url
        self.data = data
        self.headers = headers
        self.params = params
        self.response = response = (((str(requests.request(Method, url, data=data, headers=headers, params=params).text))))
        
  

function = "CRYPTO_RATING"
symbol = "BTC"
apikey = config.__apikey__
querystring = {f"function":{function},"symbol":{symbol},"apikey":{apikey}}
url = "https://google.com"
payload = ""
headers = {"cookie": "__cfduid=d3692d71ffe2bf9b65d65db30ee0895e41618990651"}
 


shejhoj = request("GET", "https://www.alphavantage.co/query", data=payload, headers=headers, params=querystring)
out = (shejhoj.response)
def filter(jsondata,*braces):
    filterout = jsondata
    for key in jsondata:
        for brace in braces:
            filterout = (filterout[brace])

    return filterout
    
        
a=filter(json.loads(out),"Crypto Rating (FCAS)","1. symbol") 
print(a)