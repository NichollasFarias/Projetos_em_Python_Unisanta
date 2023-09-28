import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


from kivy.core.window import Window

 
Window.clearcolor = [0,0,0,1]

 
class Prog1(App):
    def build(self):
        box01 = BoxLayout(orientation='horizontal')

        lbl01 = Label(text="João",font_size='30',color=[0.90,1,0.20,1])
        lbl02 = Label(text="Maria",font_size='40',color=[1,0.50,0.90,1])
        lbl03 = Label(text="José",font_size='60',color=[0.10,0.80,0.90,1])
        box01.add_widget(lbl01)
        box01.add_widget(lbl02)
        box01.add_widget(lbl03)
        return box01

        
        
Prog1().run()
