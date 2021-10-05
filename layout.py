import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class Boxlayout(BoxLayout):
    def __init__(self, **kwargs):
        super(Boxlayout, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        button = Button(text="A")
        self.add_widget(button)
        button = Button(text="B")
        self.add_widget(button)
        button = Button(text="C")
        self.add_widget(button)


class Gridlayout(GridLayout):
    def __init__(self, **kwargs):
        super(Gridlayout, self).__init__(**kwargs)
        # self.cols = 3
        self.rows = 2
        button = Button(text="A",size_hint =(None,None), size=("200dp","200dp"))
        self.add_widget(button)
        button = Button(text="B")
        self.add_widget(button)
        button = Button(text="C",size_hint =(None,None),size=("200dp","200dp"))
        self.add_widget(button)



class Layoutapp(App):
    def build(self):
        return Gridlayout()



Layoutapp().run()