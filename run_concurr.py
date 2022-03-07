import json
import threading
import os
import sys
import time
import subprocess


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m) : (i + 1) * k + min(i + 1, m)] for i in range(n))


# cmd_str = f"scrapy crawl airbnb -a query=\"{param['query']}\", -o {param['CSV']}"


# read parameters.json file
with open("parameters.json") as f:
    list_parameters = json.load(f)


commands = []
split_commands = []
for param in list_parameters:
    # print("param: ")
    # print(param)
    param["CSV"] = param["query"].replace(" ", "_").replace(",", "") + ".csv"
    param["CSV"] = param["CSV"].lower()
    cmd_str = f"scrapy crawl airbnb -a query=\"{param['query']}\", -o {param['CSV']}"
    # print(cmd_str)
    commands.append(cmd_str)
    # run scrapy
    # os.system(cmd_str)
    # print("\n")

# print(commands)
split_commands = list(split(commands, 6))
print(len(split_commands))


def thread1(commands):
    print("thread1: ")
    for command in commands:
        print(command)
        os.system(command)
        print("\n")
        print("thread1 done and empty")
        print("\n")


def thread2(commands):
    print("thread2: ")
    for command in commands:
        print(command)
        os.system(command)
        print("\n")
        print("thread2 done and empty")
        print("\n")


def thread3(commands):
    print("thread3: ")
    for command in commands:
        print(command)
        os.system(command)
        print("\n")
        print("thread3 done and empty")
        print("\n")


def thread4(commands):
    print("thread4: ")
    for command in commands:
        print(command)
        os.system(command)
        print("\n")
        print("thread4 done and empty")
        print("\n")


def thread5(commands):
    print("thread5: ")
    for command in commands:
        print(command)
        os.system(command)
        print("\n")
        print("thread5 done and empty")
        print("\n")


def thread6(commands):
    print("thread6: ")
    for command in commands:
        print(command)
        os.system(command)
        print("\n")
        print("thread6 done and empty")
        print("\n")


# run threads in parallel to run scrapy
athread1 = threading.Thread(target=thread1, args=(split_commands[0],))
athread2 = threading.Thread(target=thread2, args=(split_commands[1],))
athread3 = threading.Thread(target=thread3, args=(split_commands[2],))
athread4 = threading.Thread(target=thread4, args=(split_commands[3],))
athread5 = threading.Thread(target=thread5, args=(split_commands[4],))
athread6 = threading.Thread(target=thread6, args=(split_commands[5],))

athread1.start()
athread2.start()
athread3.start()
athread4.start()
athread5.start()
athread6.start()
