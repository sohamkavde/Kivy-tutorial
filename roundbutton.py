import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder

Builder.load_file("Buttonfile.kv")

class Buttonclass(Widget):
    pass

class RoundbuttonApp(App):
    def build(self):
        return Buttonclass()


RoundbuttonApp().run()