import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class Hello(BoxLayout):
    pass


class Hellowworld(App):
    def build(self):
        #return Label(text="Hello world!")
        return Hello()


Hellowworld().run()