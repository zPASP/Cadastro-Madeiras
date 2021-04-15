import kivy
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager

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
    pass

class Clicou(Screen):
    pass

class Myapp (App):
    def build(self):
        return Gerenciador()

Myapp().run()