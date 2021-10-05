import kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Builder.load_file('poppus.kv')


class PopforthisApp(BoxLayout):
    pass


class MyMainClassForThisApp(App):
    Window.clearcolor = (1, 1, 0, 1)

    def build(self):
        return PopforthisApp()


MyMainClassForThisApp().run()