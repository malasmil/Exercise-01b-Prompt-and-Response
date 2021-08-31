#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

passage_name = "Starting Room"
passage_text = "You wake up to find yourself to what seems to be a cave. There is a single lit torch laying on the ground. There are entry ways facing North, South, East and West."

print("you are at the " + passage_name)
print(passage_text)
response = input("What would you like to do? ")
if response == "go north":
    print("good job!")
