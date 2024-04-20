'''
Task 1: Public Transportation Module

Problem Statement: Develop a Bus class as part of a public transportation module. Use class variables to represent 
common attributes like city name and base fare. 
Implement instance variables for specific attributes like route number and passenger capacity.
Expected Outcome: A Bus class with both class and instance variables, and a transportation module to 
manage different bus routes. A test script should demonstrate creating bus instances 
and accessing both class and instance attributes.
'''

class Bus:

    print("\n welcome to the city Bus station")
    city_name ="cityville"
    bas_fare = 2.5

    def __init__(self,rout_number,passenger_capacity):
       self.rout_number = rout_number
       self.passenger_capacity = passenger_capacity


if __name__ == "__main__":

    bus1 = Bus(101, 50,)
    bus2 = Bus(106 ,70)

    print("city name:",Bus.city_name)
    print("Bus fare:",Bus.bas_fare)

    print("\n Bus one rout number", bus1.rout_number)
    print("\n Bus one passenger capacity", bus1.passenger_capacity)

    print("\n Bus two number")
    print("\n Bus two route number", bus2.rout_number)
    print("\n Bus two passenger capacity", bus2.passenger_capacity)
