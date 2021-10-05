import kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget

Builder.load_file('acc.kv')

class MYaccordion(Widget):
    pass


class MymainApp(App):
    def build(self):
        return MYaccordion()


MymainApp().run()
