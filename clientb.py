import requests

__author__ = 'mandreacchio'

r = requests.get("http://www.python.org")

with (open("test_requests.html", 'wb')) as code:
    code.write(r.content)
