'''
Objective:
The aim of this assignment is to apply the concepts of Object-Oriented Programming in Python to build a simulated 
City Infrastructure Management System. This system will incorporate classes, objects, methods, and data structures 
to manage different aspects of a city, such as buildings, traffic, and events.

Task 1: Vehicle Registration System

Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. 
Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and 
demonstrate changing the owner.
Code Example: Provide a basic structure for the Vehicle class without methods.
```python
class Vehicle:
def init(self, reg_num, type, owner):
self.registration_number = reg_num
self.type = type
self.owner = owner
```
Expected Outcome: Completion of the Vehicle class with the update_owner method and a demonstration script showing the creation of 
Vehicle objects and updating their owners.
'''

# class Vehicle:
#     def __init__(self, reg_num, type, owner):
#         self.registration_number = reg_num
#         self.type = type
#         self.owner = owner

#     def update_owner(self, new_owner):
#         self.owner = new_owner

# vehicle1 = Vehicle("ABCD1234", "car", "john")
# vehicle2 = Vehicle("ABCD12344", "Motorcycle", "Allice")

# vehicle1.update_owner("bob")

# print("vehicle one details after updating owner")
# print("Regestration number", vehicle1.registration_number)
# print("Type of vehicle ",vehicle1.type)
# print("vehicle owner", vehicle1.owner)


# print("\n vehicle2 details:")
# print("vehicle regestration", vehicle2.registration_number)
# print("type of vehicle", vehicle2.type)
# print("owner of vehicle", vehicle2.owner)

'''
Task 2: Event Management System Enhancement

Problem Statement: Extend an existing Event class by adding a feature to keep track of the number of participants. 
Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.
Code Example: Basic Event class without participant tracking.
```python
class Event:
def init(self, name, date):
self.name = name
self.date = date
'''

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0

    def add_participant(self):
        self.participant_count += 1

    def get_participant_count(self):
       return self.participant_count
    
# Create an event instance
event1 = Event("Birthday Party", "2024-04-20")

# Add participants
event1.add_participant()
event1.add_participant()
event1.add_participant()

# Retrieve participant count
participant_count = event1.get_participant_count()
print("Participant count:", participant_count)




