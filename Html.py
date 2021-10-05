import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('Html.kv')

class MyLayout(BoxLayout):
    pass


class Echocoding(App):
    def build(self):
        return MyLayout()


Echocoding().run()