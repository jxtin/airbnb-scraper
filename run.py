import json
import os
import sys


# read parameters.json file
with open("parameters.json") as f:
    parameters = json.load(f)

print(parameters)

cmd_str = (
    f"scrapy crawl airbnb -a query=\"{parameters['query']}\", -o {parameters['CSV']}"
)
# run scrapy
os.system(cmd_str)
print(cmd_str)
