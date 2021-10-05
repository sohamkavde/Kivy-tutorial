import kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


Builder.load_file('pos_size.kv')

class ContainerPosAndSize(BoxLayout):
    pass


class Sizeofwidget(FloatLayout):
    def __init__(self,**kwargs):
        super(Sizeofwidget, self).__init__(**kwargs)
        button = Button(text="First Button",size_hint=(.2,.2),pos=(100,100))
        # {"x" ,"y","center_x","center_y","top","bottom","left","right"}
        button1 = Button(text="second Button", size_hint=(.2, .2), pos_hint={"x":.8,"y":.8})
        button2 = Button(text="third Button", size_hint=(.2, .2), pos_hint={"center_x": .5, "center_y": .5})
        self.add_widget(button)
        self.add_widget(button1)
        self.add_widget(button2)
class PossizeApp(App):
    def build(self):
        return Sizeofwidget()

PossizeApp().run()