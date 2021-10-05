import kivy
from kivy.animation import Animation
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
Builder.load_file('animation.kv')

class Mylayout(BoxLayout):
    def animate(self,anim,*args):
        animation = Animation(
            background_color=(1,0,0,1),
            duration=3
        )

        animation += Animation(
            background_color=(0, 1, 1, 1),
            duration=3
        )

        animation += Animation(
           size_hint=(.7,.3)
        )

        animation += Animation(
            font_size=10,
            size_hint=(.2, .2),
            pos_hint={"center_x":.2}
        )
        animation += Animation(
            font_size=32,
            size_hint=(.5, .8),
            pos_hint={"center_x": .7}
        )
        animation += Animation(
            font_size=32,
            size_hint=(.4,.2),
            pos_hint={"center_x": .5}
        )
        animation.start(anim)

        animation.bind(on_complete=self.complete)

    def complete(self,*args):
        self.ids.my_label.text = "Your animation is completed"

class Echocoding(App):
    def build(self):
        return Mylayout()


Echocoding().run()
