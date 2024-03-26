# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:26:53 2024

@author: Devon Henderson

Week 5 Lecture 1
Getting Data from the web (APIs)

"""

import requests
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from PIL import Image
from io  import BytesIO

########################################################################
### HTTP Requests and responses
response = requests.get('https://www.op.ac.nz')
print("Request URL: ", response.request.url)
print("Request Headers: ", response.request.headers)

#Addition information encapsulated in HTTP req. object
print("dir(response.request): ", dir(response.request))

#Look at response object
print("\nResponse Headers: ", response.headers)
print("\nStatus Code: ", response.status_code)
print("Response Server: ", response.headers["Server"])
print("Response Encoding: ", response.encoding)
print("Response Cookies: ", response.cookies)

#read the payload content of the server's HTTP response, 
#in this case an HTML document in minified form
#########print("Response text: ", response.text)      #Commented out due to length

#Make a POST request
response = requests.post('http://httpbin.org/post', data = {'BIT':'Bachelor of Information Technology'})
print("\nPOST status code: ", response.status_code)
print("POST response text: ", response.text)

#Other HTTP request types: PUT, DELETE, HEAD and OPTIONS
response = requests.put('http://httpbin.org/put', data = {'key':'value'}) #Returns PUT data.
print("\nPUT status code: ", response.status_code)
print("PUT response text: ", response.text)

response = requests.delete('http://httpbin.org/delete') #/delete Returns DELETE data
print("\nDELETE status code: ", response.status_code)
print("DELETE response text: ", response.text)

response = requests.head('http://httpbin.org/get')
print("\nGET HEAD status code: ", response.status_code)
print("GET HEAD response text: ", response.text)

response = requests.options('http://httpbin.org/get')
print("\nGET OPTIONS status code: ", response.status_code)
print("GET OPTIONS response text: ", response.text)

#Using key value pairs to send data
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('http://httpbin.org/get', params=payload)
print("Check URL with params: ", response.url)

#Add HTTP request headers with a dict
url = 'http://httpbin.org/put'
headersDictionary = {'user-agent': 'I\'m a fake browser'}

response = requests.get(url, headers=headersDictionary)
print("\nresponse.request.headers (using dict in headers): ", response.request.headers)

# Send some form-encoded data — much like an HTML form.
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('http://httpbin.org/post', data=payload)
print("Response text (using data and payload)", response.text)


########################################################################
### Binary Response Content
response = requests.get('https://cdn.britannica.com/79/232779-050-6B0411D7/German-Shepherd-dog-Alsatian.jpg')
binaryImage = Image.open(BytesIO(response.content))
binaryImage.save("./data/imageRetrievedFromTheWeb.png")
imgplot = plt.imshow(binaryImage)
plt.axis('off')
plt.show()

########################################################################
### Retrieving data from APIs
#FDA Adverse effects
response = requests.get('https://api.fda.gov/drug/event.json?search=patient.drug.openfda.pharm_class_epc:"nonsteroidal+anti-inflammatory+drug"&count=patient.reaction.reactionmeddrapt.exact')
print("FDA JSON response: ", response.json())

#Dunedin weather
response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Dunedin,nz&appid=f6b6fecf2c4292d8d19d201e57667588&mode=json')
print("\nDunedin Weather JSON response: ", response.json())

#Financial API
response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey=demo')





