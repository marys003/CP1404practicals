from kivy.app import App
from kivy.lang import Builder

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

# Constants
MILES_TO_KM_CONVERSION_FACTOR = 1.60934

class MilesConverter(BoxLayout):
    output_text = StringProperty('0.0')

    def calculate_conversion(self):
        try:
            miles = float(self.ids.miles_input.text)
            kilometers = miles * MILES_TO_KM_CONVERSION_FACTOR
            self.output_text = f'{kilometers:.2f}'
        except ValueError:
            # Handle invalid input
            self.output_text = '0.0'

    def handle_increment(self, value):
        try:
            current_miles = float(self.ids.miles_input.text)
        except ValueError:
            current_miles = 0.0

        new_miles = current_miles + value
        self.ids.miles_input.text = str(new_miles)
        self.calculate_conversion()


class MilesConverterApp(App):
    def build(self):
        return MilesConverter()


if __name__ == '__main__':
    MilesConverterApp().run()
