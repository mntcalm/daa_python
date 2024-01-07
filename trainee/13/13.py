#!/usr/bin/python3
import sys

if (len(sys.argv) >= 3):
  name = sys.argv[1]
  surname = sys.argv[2]
  print(f"Hello, {name} {surname}! Nice to see you here!")

else:
  print("запускайте с двумя аргументами! примерно так: ./13.py Name Surname")

