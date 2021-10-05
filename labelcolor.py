import kivy
from kivy.app import App
from kivy.lang import Builder

Hello = Builder.load_file('color.kv')

class Myapp(App):
    def build(self):
        return Hello


Myapp().run()