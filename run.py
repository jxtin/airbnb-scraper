import json
import os
import sys


# read parameters.json file
with open("parameters.json") as f:
    list_parameters = json.load(f)

print(list_parameters)

for param in list_parameters:
    print("param: ")
    print(param)
    cmd_str = f"scrapy crawl airbnb -a query=\"{param['query']}\", -o {param['CSV']}"
    # run scrapy
    os.system(cmd_str)
    print("\n")
