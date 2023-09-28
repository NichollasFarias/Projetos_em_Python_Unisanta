import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

 

from kivy.core.window import Window

 

Window.clearcolor = [0,0,0,1]
lista = ['7','8','9','+','4','5','6','-','1','2','3','*','clear','0','=','/']

 
class Prog1(App):
    def build(self):
        grid = GridLayout(rows = 4)
        for nome in lista:
            grid.add_widget(Label(text= nome,font_size='20',color=[1,1,1,1]))
            
        return grid
        
        
Prog1().run()

