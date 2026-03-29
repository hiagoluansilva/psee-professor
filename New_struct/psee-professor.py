from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from PIL import Image
  
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
        a="Tensões de Referência:{}".format(self.ids.texto_tela4.text)
        b=self.ids.texto_tela4.text
        for i in range(2):
            #self.add_widget(Button(text=str(i),id=str(i)))
            pass
        #self.add_widget(Button(text=str(b)))#(Label(text=str(b)))
        #self.add_widget(layout)
    pass

class PSEE_Professor(App):
    master = ScreenManager()
    def build(self):
        PSEE_Professor.master.add_widget(Menu(name="menu"))
        PSEE_Professor.master.add_widget(Tela1(name="tela1"))
        PSEE_Professor.master.add_widget(Tela2(name="tela2"))
        PSEE_Professor.master.add_widget(Tela3(name="tela3"))
        PSEE_Professor.master.add_widget(Tela4(name="tela4"))
        return PSEE_Professor.master

PSEE_Professor().run()


