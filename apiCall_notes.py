# API --> means one program talk to another program (Application Pragramming Interface)
""" 
For example:

-your Python script sends a request

-server sends back data

-often the data comes in JSON format
 """
"""
API = a way for two software systems to talk
JSON = a common format they use to send data

Easy example to remember forever
You open food delivery app
app talks to restaurant server using API
order details are sent in structured form like JSON

So:

API = communication system
JSON = structured data format

"""

# Request --> it's a popular python HTTP library for sending web requests.

import requests

req= requests.get("https://api.github.com") # get requests means 'give me data' -->here asking github api to send public data

print(req) #response is stored in req
print(req.status_code) # status_code tells whether request succeeded
print(req.text) # text gives response body as string
print("---------")
print(req.json()) # req.json() --> convert json response directly into Python dictionary/list

## HTTP status_code: (common codes)
# 200 = success
# 404 = not found
# 500 = server error

# Ex:
import requests

r = requests.get("https://api.github.com")
data = r.json()

print(type(data))
#print(data["current_user_url"])

print("=========")
# Full example
import requests

r = requests.get("https://api.github.com")

print("Status code:",r.status_code)

if r.status_code == 200:
    data = r.json()
    print("Current user URL:",data["current_user_url"])
    print("Repository URL:",data["repository_url"])
else:
    print("Request failed")

## Query Parameters
#-->Query parameters are extra information added at the end of a URL.
"""
They help you tell the server:
- which data you want 
- how much data you want 
- which page you want 
- which filter you want

Think like this:

You go to a shop and say:

“Give me notebooks”

That is normal request.

But if you say:

“Give me 5 notebooks, blue color”

That extra detail is like query parameters.

--->query parameters always come after ?

And if there are multiple parameters, they are joined by &

"""
print("=========")

params = {
    "page": 1,
    "per_page": 5
}
r = requests.get("https://api.github.com/repositories",params=params)
print(r.url)

# Headers
#--> Headers are extra information sent with the request,but not inside the url

"""
They tell the server things like:

what type of response you want

who you are

your token/authentication

what app/client is sending the request

>>Think like this:

Query parameter says:

what data I want

Header says:

extra rules/information about my request

| Thing    | Query Parameters           | Headers                    |
| -------- | -------------------------- | -------------------------- |
| Where?   | In URL                     | Not in URL                 |
| Purpose  | Ask for specific data      | Give extra request info    |
| Example  | `?page=1&per_page=5`       | `Accept: application/json` |
| Used for | filter, search, pagination | auth, format, client info  |

"""
# ex:
headers ={
    "Accept":"application/json"
}

r = requests.get("https://api.github.com",headers=headers)
print(r.url)  # headers not show in url 
print(r.status_code)

# 'Post' request 
'''
get = receive data
post = send data
'''
import requests
url = "https://httpbin.org/post"
data ={
    "name":"Rijon",
    "skill":"Python"
}

r = requests.post(url,data = data)

print(r.status_code)
print(r.text)

data = r.json()
print("URL:",data["url"])

print("========")

# Error handing
import requests
try:
    r= requests.get("https://api.github.com",timeout=5) #here timeout means how long your program will wait for the server response before giving up.
    r.raise_for_status() #if status is success, it does nothing |||| if status is error, it throws an exception
    data = r.json()
    print(data)
except requests.exceptions.RequestException as e:
    print("Error:", e)