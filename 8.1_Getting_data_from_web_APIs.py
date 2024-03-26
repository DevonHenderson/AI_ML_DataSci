# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:26:53 2024

@author: Devon Henderson

Week 5 Lecture 1
Getting Data from the web (APIs)

"""

import requests

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
print(response.url)