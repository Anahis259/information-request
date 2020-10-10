import re

string = input ("Enter a valid email:")

match = re.search('^[a-zA-Z0-9.-_]+@[a-zA-Z]+\.[a-z-A-Z.]+', string)

if match:
  print("Valid email")
else:
  print("Not valid email")  