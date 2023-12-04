# band.py

class Band:
    """Band class for a musical band with a list of musicians."""

    def __init__(self, name):
        """Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing their first (or no) instrument."""
        output = []
        for musician in self.musicians:
            output.append(musician.play())
        return "\n".join(output)

