""""
CP1404 -NGUYEN TAN ANH
JC950881
PRACTICAL 9
"""
from Practical_9.taxi import Taxi

my_taxi = Taxi(name="Prius 1", fuel=100)
my_taxi.drive(40)
print(my_taxi)
my_taxi.start_fare()
my_taxi.drive(100)
print(my_taxi)
print(my_taxi.get_fare())
