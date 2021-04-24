#from os import path
from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
import json
from datetime import date
import os


class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    pass

class DesData():
    data = date.today()
    data_string = str(data)
    dia = data.strftime("%d")
    mes = data.strftime("%m")
    ano = data.strftime("%Y")
    pass

class CadMadeira(Screen):

    tipoMadeira = ['PINUS','EUCALIPTO']
    modelosMadeiras = []
    path = ''

    def on_pre_enter(self,*args):
        print(self.ids)
        self.path = App.get_running_app().user_data_dir+'/'
        self.carregarData()
        print(self.path)    
        print(DesData.dia)
        print(DesData.data_string)
        self.pastaDia()
        with open(self.path+DesData.data_string+'/'+str(DesData.data)+'.json','w') as f:
            json.dump(self.modelosMadeiras,f)

    def saveData(self,*args):
        with open(self.path+DesData.data_string+'/'+str(DesData.data)+'.json','w') as f:
            json.dump(self.modelosMadeiras,f)

    def carregarData(self,*args):
        try:
            with open(self.path+DesData.data_string+'/'+str(DesData.data)+'.json','r') as f:
                self.modelosMadeiras = json.load(f)
        except FileNotFoundError:
            pass

    def salvarMadeira(self):
        modelo = (self.ids.tipoMadeira.text+' - '+self.ids.nomeMadeira.text)
        self.ids.nomeMadeira.text = ''
        self.modelosMadeiras.append(modelo)
        self.saveData()

    def pastaDia(self):
        pastadoDia = self.path+DesData.data_string

        if not os.path.exists(pastadoDia):
            os.makedirs(pastadoDia)
        



class ModificaMadeira(Screen):
    pass

class JTeste(Screen):
    def on_pre_enter(self,**kwargs):
        super().__init__(**kwargs)
        self.add_widget(MostraMadeira(text='a'))
        

class ModificacaoDia(Screen):
    varModDia = []
    path = ''
    def on_pre_enter(self):
        self.path = App.get_running_app().user_data_dir+'/'
        print('ENTROU')
        print(self.path)
        self.loadData()
        print(self.ids)
        for madeira in self.varModDia:
            self.add_widget(MostraMadeira(text=madeira))

    def addTelaMad (self):
        texto = self.ids.tex
        self.ids.tex.add_widget(MostraMadeira(text='a'))
        
    def loadData(self,*args):
        try:
            with open(self.path+DesData.data_string+'/'+str(DesData.data)+'.json','r') as f:
                print('JSON ENCONTRADO')
                self.varModDia = json.load(f)
        except FileNotFoundError:
            print ('Arquivo não encontrado')
            pass   
    
class Mostramadeira (BoxLayout):
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