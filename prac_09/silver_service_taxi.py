from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialized version of Taxi with fanciness and flagfall attributes."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialize a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return the price for the taxi trip, including flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi object."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
