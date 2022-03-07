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
    param["CSV"] = param["query"].replace(" ", "_").replace(",", "") + ".csv"
    param["CSV"] = param["CSV"].lower()
    cmd_str = f"scrapy crawl airbnb -a query=\"{param['query']}\", -o {param['CSV']}"
    print(cmd_str)
    # run scrapy
    os.system(cmd_str)
    print("\n")
