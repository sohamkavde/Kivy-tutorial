import  kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Builder.load_file('switch.kv')

class MySwitchapp(BoxLayout):
    def activefunction(self,boolvalue):
        #print(boolvalue)
        if boolvalue == True:
            self.ids.my_label.text ='This is button and it is on!'
        else:
            self.ids.my_label.text = 'This is button and it is off!'

class Echocoding(App):

    def build(self):
        return MySwitchapp()


Echocoding().run()