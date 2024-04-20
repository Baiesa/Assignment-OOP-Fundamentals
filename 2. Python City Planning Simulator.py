'''
Objective:
The aim of this assignment is to solidify understanding of Python's Object-Oriented Programming concepts through 
the development of a simulated city planning system. This system will integrate the use of classes, objects, inheritance, 
and file handling to manage various city elements like buildings, traffic systems, and public events.

Task 1: File Handling for Building Records

Problem Statement: Implement a system to handle building records using file operations. Create a Building class and 
write a script to save and load building details to and from a file.
Code Example: Skeleton of the Building class.
```python
class Building:
def init(self, name, floors):
self.name = name
self.floors = floors
# Methods to save to file and load from file
'''

class Building:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors
    
    def save_to_file(self, filename):
        with open(filename, 'a') as file:
            file.write(f"{self.name},{self.floors}\n")
    
    @staticmethod
    def load_from_file(filename):
        buildings = []
        with open(filename, 'r') as file:
            for line in file:
                name, floors = line.strip().split(',')
                buildings.append(Building(name, int(floors)))
        return buildings

building1 = Building("Office Building", 10)
building2 = Building("Apartment Complex", 20)

building1.save_to_file("buildings.txt")
building2.save_to_file("buildings.txt")


loaded_buildings = Building.load_from_file("buildings.txt")


for building in loaded_buildings:
    print("Name:", building.name)
    print("Floors:", building.floors)
    print()
    