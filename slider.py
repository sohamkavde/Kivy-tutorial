import  kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Builder.load_file('sl.kv')

class MysliderforthisApp(BoxLayout):
    def sliderfunction(self, *args):
        # print(*args)
        self.ids.labelvalue.text = str(int(args[1]))
        self.ids.labelvalue.font_size = str(int(args[1])*10)

class MyMainClassForThisApp(App):
    Window.clearcolor = (.9, .9, .9, 1)
    def build(self):
        return MysliderforthisApp()


MyMainClassForThisApp().run()