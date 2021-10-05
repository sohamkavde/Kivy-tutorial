import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

Builder.load_file('progreeBar.kv')


class Mylayout(BoxLayout):
    def progress(self):
        val = self.ids.progree.value
        if val == 1:
            val = 0
        val += .20

        self.ids.my_label.text = f'{int(val*100)} % progress'
        self.ids.progree.value = val


class MyProgress(App):
    def build(self):
        return Mylayout()


MyProgress().run()