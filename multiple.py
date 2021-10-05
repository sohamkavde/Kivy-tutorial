import kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

class Firstclass(Screen):
    pass

class Secondclass(Screen):
    pass

class Windowclass(ScreenManager):
    pass


varname = Builder.load_file('multiple.kv')



class MyMainClassForThisApp(App):
    Window.clearcolor = (1, 0, 1, 1)

    def build(self):
        return varname


MyMainClassForThisApp().run()