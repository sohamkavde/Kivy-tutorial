import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

Builder.load_file("splitter.kv")


class SplitterClass(BoxLayout):
    pass


class MaineSpliterApp(App):
    def build(self):
        return SplitterClass()


MaineSpliterApp().run()