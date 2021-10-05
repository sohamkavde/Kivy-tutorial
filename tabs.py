import kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.tabbedpanel import TabbedPanel

Builder.load_file('tabs.kv')


class TabsApp(TabbedPanel):
    pass


class MytabsApp(App):
    def build(self):
        return TabsApp()

MytabsApp().run()