import kivy
from kivy.app import App
from kivy.uix.label import Label


class Prog1(App):
    def build(self):
        return Label(text="Salve", font_size='30sp',bold=True,color=[1,0,1,1])


Prog1().run()
