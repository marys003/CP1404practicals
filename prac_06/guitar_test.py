# guitar_test.py
from guitar import Guitar

def test_guitar_methods():
    # Create guitars for testing
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 800.00)

    # Test get_age() method
    print(f"{guitar1.name} get_age() - Expected 100. Got {guitar1.get_age(2022)}")
    print(f"{guitar2.name} get_age() - Expected 9. Got {guitar2.get_age(2022)}")

    # Test is_vintage() method
    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage(2022)}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage(2022)}")

if __name__ == "__main__":
    test_guitar_methods()
