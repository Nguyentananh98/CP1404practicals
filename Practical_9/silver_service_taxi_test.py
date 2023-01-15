""""
CP1404 -NGUYEN TAN ANH
JC950881
PRACTICAL 9
"""
from Practical_9.SilverServiceTaxi import SilverServiceTaxi

my_taxi = SilverServiceTaxi(name='Taxi_good', fuel=100, fanciness=2)
my_taxi.drive(18)
print(my_taxi.get_fare())