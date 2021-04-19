import kivy
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
import json


class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class CadMadeira(Screen):
    tipoMadeira = ['PINUS', 'EUCALIPTO']
    pass

class ModificaMadeira(Screen):
    tipoMadeira = CadMadeira.tipoMadeira 
    pass

class ModificacaoDia(Screen):
    madeiras = ['PINUS', 'EUCALIPTO']
    def on_pre_enter(self):
        print('ENTROU')
        for madeira in self.madeiras:
            self.ids.tex_modificacoes.add_widget(MostraMadeira(text=madeira))
    
class MostraMadeira(BoxLayout) :
    def __init__(self,text='',**kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

class Myapp (App):
    def build(self):
        return Gerenciador()

Myapp().run()