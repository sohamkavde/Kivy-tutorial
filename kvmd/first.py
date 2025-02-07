from kivy.uix.button import Button
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton


class Name(MDApp):
    def build(self):
        screen = Screen()

        l = MDLabel(text="Hello Soham",halign="center",
                    theme_text_color="Custom",
                    text_color=(0.5, 0, 0.5, 1),
                    font_style="Caption",
                    pos_hint={'x': .3, 'y': .2},
                    size_hint=(.5, .6)
                    )
        button = Button(text='Hello world', size_hint=(.5, .5),
                        pos_hint={'x': .2, 'y': .2})

        screen.add_widget(l)
        # screen.add_widget(button)
        return screen
Name().run()
