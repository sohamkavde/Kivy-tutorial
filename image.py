import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang.builder import Builder


Builder.load_file('image.kv')


class LayoutHeader(BoxLayout):
    pass
    # def __init__(self,**kwargs):
    #     super(LayoutHeader, self).__init__(**kwargs)
    #     self.add_widget(Button(text='Hellow'))


class NavigationApp(App):
    def build(self):
        return LayoutHeader()

NavigationApp().run()