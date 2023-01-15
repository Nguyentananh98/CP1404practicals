from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """build the window app from kivy file"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """change greet text base on user input name"""
        print('greet')
        print("test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def clear_input(self):
        """clear all output text and input text"""
        self.root.ids.output_label.text = ''
        self.root.ids.input_name.text = ''


BoxLayoutDemo().run()
