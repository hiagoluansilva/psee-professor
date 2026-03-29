from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
  
class Master(ScreenManager):
    pass

class Menu(Screen):
    pass

class Tela1(Screen):
    def gravar(self):
        n=self.ids.n_tensoes.text
        
        if(n.isdigit()):
            self.manager.screens[4].ids.texto_tela4.text=n
            n="Tensões de Referência:{}".format(n)
            self.manager.screens[3].ids.confirma.text=n
            self.parent.current = 'tela3'
        else:
            n="Erro"
            self.manager.screens[2].ids.confirma.text=n
            self.parent.current = 'tela2'

class Tela2(Screen):
    pass

class Tela3(Screen):
    pass

class Tela4(Screen):
    def __init__(self, **kwargs):
        super(Tela4,self).__init__(**kwargs)
        b=3
        for i in range(b):
            self.add_widget(Button(text=str(b)))#(Label(text=str(b)))

class PSEE_Professor(App):
    def build(self):
        return Master()

PSEE_Professor().run()


