from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

__author__ = 'NGUYEN TAN ANH'

MILES_TO_KILOMETRE = 1609


class ConvertMilesToKmApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    message = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "Convert miles to km"
        return self.root

    def handle_convert(self):
        mile_value = self.check_mile_input()
        kilometre_value = mile_value * MILES_TO_KILOMETRE
        self.root.ids.output_label.text = str(kilometre_value)

    def handle_increment(self, value):
        input_value = self.check_mile_input()
        input_value += value
        self.root.ids.text_input.text = str(input_value)

    def check_mile_input(self):
        try:
            input_value = float(self.root.ids.text_input.text)
        except ValueError:
            input_value = 0.0
        return input_value


ConvertMilesToKmApp().run()