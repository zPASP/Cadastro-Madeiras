import kivy
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
import json
from datetime import date


class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class DesData():
    data_dia_inteira = date.today()
    #data_dia

    pass

class CadMadeira(Screen):
    tipoMadeira = []
    path = ''

    

    def on_pre_enter(self):
        self.path = App.get_running_app().user_data_dir+'/cadmadeira/'
        print(self.path)
       # print(DesData.data_dia)
    
    #def loadData(self,*args):
    #    try:
    #        with open(self.path+ )


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