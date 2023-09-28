import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


from kivy.core.window import Window

 
Window.clearcolor = [0,0,0,1]

 
class Prog1(App):
    def build(self):
        box01 = BoxLayout(orientation='vertical')
        box02 = BoxLayout(orientation='horizontal')
        grid01 = GridLayout(cols = 2)

        lbl001 = Label(text='Engenharia',font_size='50',color=[1,1,1,1])
        lbl002 = Label(text='UNISANTA',font_size='50',color=[1,1,1,1])

        lbl01 = Label(text='Computação',font_size='20',color=[1,1,1,1])
        lbl02 = Label(text='Civil',font_size='20',color=[1,1,1,1])
        lbl03 = Label(text='Quimica',font_size='20',color=[1,1,1,1])
        
        box02.add_widget(lbl01)
        box02.add_widget(lbl02)
        box02.add_widget(lbl03)

        box01.add_widget(lbl001)
        box01.add_widget(lbl002)

        grid01.add_widget(box01)
        grid01.add_widget(box02)
        
        return grid01

        
        
Prog1().run()
