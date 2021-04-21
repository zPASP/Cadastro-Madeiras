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
    data = date.today()
    dia = data.strftime("%d")
    mes = data.strftime("%m")
    ano = data.strftime("%Y")
    pass

class CadMadeira(Screen):

    tipoMadeira = ['PINUS','EUCALIPTO']
    modelosMadeiras = []
    path = ''

    def on_pre_enter(self,*args):
        self.path = App.get_running_app().user_data_dir+'/cadmadeira/'
        print(self.path)    
        print(DesData.dia)
        with open(str(DesData.data)+'.json','w') as f:
            json.dump(self.modelosMadeiras,f)

    def saveData(self,*args):
        with open(str(DesData.data)+'.json','w') as f:
            json.dump(self.modelosMadeiras,f)

    def salvarMadeira(self):
        modelo = (self.ids.tipoMadeira.text,' - ', self.ids.nomeMadeira.text)
        self.ids.nomeMadeira.text = ''
        self.modelosMadeiras.append(modelo)
        self.saveData()


class ModificaMadeira(Screen):
    pass

class ModificacaoDia(Screen):
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


 #def verificaArquivo(self):
    #    try:
    #        f = open(self.path+self.DesData.data+'.json')
    #        f.close
    #        return (True)
    #    except:
    #        return (True)