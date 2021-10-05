import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

#Hello = Builder.load_file('xyz.kv')


Hello = Builder.load_string('''
Label:
    text:"Hello Viewer"

''')

# class Mylayout(BoxLayout):
#     pass


class Myapp(App):
    def build(self):
        return Hello


Myapp().run()