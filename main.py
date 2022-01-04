from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class BoxLayoutExample(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
            b1 = Button()


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass  # This pass is a syntax placeholder that is awesome so far!!


TheLabApp().run()  # This opens up a new window for the App. This is very interesting stuff
