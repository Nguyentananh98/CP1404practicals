""""
CP1404 -NGUYEN TAN ANH
JC950881
PRACTICAL 9
"""
from Practical_9.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name='', fuel=0, fanciness=1):
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """display the information of the taxi status"""
        return f'{super().__str__()} plus flagfall of ${SilverServiceTaxi.flagfall}'

    def get_fare(self):
        """calculate the driven fare"""
        return SilverServiceTaxi.flagfall + super().get_fare()
