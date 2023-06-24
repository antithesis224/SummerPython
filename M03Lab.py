#!/usr/bin/env python
# coding: utf-8

# In[1]:


##Colby Koppelmann
##M03Lab.py
##The program asks for info about a Vehicle and repeats the info to the user

class Vehicle():
    def __init__(self, type):
        self.type = type

class Automobiles(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    

type = input("Enter Vehicle Type: ")
year = input("Enter Vehicle Year: ")
make = input("Enter Vehicle Make: ")
model = input("Enter Vehicle Model: ")
doors = input("Enter Vehicle Doors: ")
roof = input("Enter Vehicle Roof Type: ")

print("Vehicle Type:" + type + "\n" + "Vehicle Year:" + year + "\n" + "Vehicle Make:" + make + "\n" + "Vehicle Model:" + model + "\n" + "Vehicle Doors:" + doors + "\n" + "Vehicle Roofs:" + roof + "\n")

