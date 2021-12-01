
Python Requests Module
======================



### Example


Make a request to a web page, and print the response text:



```python
import requestsx = requests.get('https://w3schools.com/python/demopage.htm')print(x.text)
```


Definition and Usage
--------------------


The `requests` module allows you to send HTTP 
requests using Python.


The HTTP request returns a [Response Object](ref_requests_response.asp) with all the response data 
(content, encoding, status, etc).


Download and Install the Requests Module
----------------------------------------


Navigate your command line to the location of PIP, and type the following:




C:\Users\*Your Name*\AppData\Local\Programs\Python\Python36-32\Scripts>pip install requests


Syntax
------




 requests.*methodname(params)*


Methods
-------




| Method | Description |
| --- | --- |
| [delete(*url*, *args*)](ref_requests_delete.asp) | Sends a DELETE request to the specified url |
| [get(*url*, *params, args*)](ref_requests_get.asp) | Sends a GET request to the specified url |
| [head(*url*, *args*)](ref_requests_head.asp) | Sends a HEAD request to the specified url |
| patch(*url*, *data, args*) | Sends a PATCH request to the specified url |
| [post(*url*, *data, json, args*)](ref_requests_post.asp) | Sends a POST request to the specified url |
| put(*url*, *data, args*) | Sends a PUT request to the specified url |
| request(*method*, *url*, *args*) | Sends a request of the specified method to the specified url |


