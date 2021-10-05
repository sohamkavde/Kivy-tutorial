import kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget

Builder.load_file("carousel.kv")


class MycarouselApp(Widget):
    pass


class MyMovignImageapp(App):
    def build(self):
        return MycarouselApp()

MyMovignImageapp().run()
