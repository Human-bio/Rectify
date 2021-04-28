import json
import requests
import config 
class request:
    
    def __init__(self,Method, url, data, headers, params,response="Default"):
        self.Method = Method
        self.url = url
        self.data = data
        self.headers = headers
        self.params = params
        self.response = response = ((json.loads(str(requests.request(Method, url, data=data, headers=headers, params=params).text)))["Crypto Rating (FCAS)"]["1. symbol"])
        
  
url = "https://www.alphavantage.co/query"
function = "CRYPTO_RATING"
symbol = "BTC"
apikey = config.__apikey__
querystring = {f"function":{function},"symbol":{symbol},"apikey":{apikey}}

payload = ""
headers = {"cookie": "__cfduid=d3692d71ffe2bf9b65d65db30ee0895e41618990651"}
 
response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    
shejhoj = request("GET", url, data=payload, headers=headers, params=querystring)
print(shejhoj.response)