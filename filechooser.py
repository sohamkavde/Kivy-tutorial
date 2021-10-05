import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder


Builder.load_file("filechoose.kv")


class filesChoose(Widget):
    def selected(self,filesource):
        try:
            self.ids.My_image.source = filesource[0]

        except:
            pass


class MyfileApp(App):
    def build(self):
        return filesChoose()


MyfileApp().run()