import kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

Builder.load_file('checkbox.kv')


class Defineclass(BoxLayout):
    checkbox = []
    def activefunction(self,boolvalue,value):

        if boolvalue == True:
            Defineclass.checkbox.append(value)
            varvalue = ''

            for x in Defineclass.checkbox:
                varvalue = f"{varvalue} {x}"

            self.ids.answer.text = f'You selected : {varvalue}'
        else:
            Defineclass.checkbox.remove(value)
            varvalue = ''

            for x in Defineclass.checkbox:
                varvalue = f"{varvalue} {x}"

            self.ids.answer.text = f'You selected : {varvalue}'

class MycheckboxApp(App):
    Window.clearcolor = (0, 0, 0, 1)

    def build(self):
        return Defineclass()


MycheckboxApp().run()