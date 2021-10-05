import kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Builder.load_file('imagebutton.kv')


class ImageButtonApp(BoxLayout):
   def press(self):
       val = self.ids.labelforchange.text
       if val == "Your decision to subscribe this channel is right !":
            self.ids.labelforchange.text = "We will meet again"
            self.ids.my_image.source = 'img/sub2.png'
       else:
           self.ids.labelforchange.text = "Your decision to subscribe this channel is right !"
           self.ids.my_image.source = 'img/sub2.png'

   def release(self):
       self.ids.my_image.source = 'img/sub1.png'


class MyMainClassForThisApp(App):
    Window.clearcolor = (0, 1, 1, 1)

    def build(self):
        return ImageButtonApp()


MyMainClassForThisApp().run()