# two types of modules in python :
#  - Build in modules
#  - external modules
# lists of all build in modules : https://docs.python.org/3/py-modindex.html

import math
import os
import mymodule
import requests # requests module prompt

print(math.sqrt(16))
mymodule.hello()
r = requests.get("https://www.google.com")
print(r.text)

import requests

response = requests.get("https://api.github.com")
print(response.status_code)
print(response.text)

'''
I have to learn this 
as soon as possible
for sure !!!
'''

