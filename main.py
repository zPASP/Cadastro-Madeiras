from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import json

class Janelas(ScreenManager):
    pass

class Menu(Screen):
    pass

class Cadastro(Screen):
    cadastro = []

    def on_pre_enter(self):
        print(self.cadastro)

    def salvarInfo(self,*args):
        textoCadastrar = self.ids.txt_cadastro.text
        self.cadastro.append(textoCadastrar)
        self.ids.txt_cadastro.text = ''
        with open('dados.json','w') as dados:
            json.dump(self.cadastro, dados)
        print(self.cadastro)
    

class Exibir(Screen):
    cadastro = []
    def on_pre_enter(self):
        self.carregarInfo()
        for cad in self.cadastro:
            self.ids.box_exibir.add_widget(ListarCad(text=cad))

    def removerCadastro(self,ListarCad):
        self.ids.box_exibir.remove_widget(ListarCad)

    def carregarInfo(self,*args):
        try:
            with open('dados.json','r') as dados:
                self.cadastro = json.load(dados)
        except fileNotFoundError:
            pass

class ListarCad(BoxLayout):
    def __init__(self,text='',**kwargs):
        super(ListarCad, self).__init__(**kwargs)
        self.ids.label.text = text

class ModiJson():
    def carregarJson():
        try:
            with open('dados.json','r') as dados:
                return json.load(dados)
        except fileNotFoundError:
            return 0    

class Modificacoes(Screen):
    medidas = ModiJson.carregarJson()
    tipos = ['PINUS','EUCALIPTO']
    
    def carregarInfo(self,*args):
        try:
            with open('dados.json','r') as dados:
                self.medidas = json.load(dados)
        except fileNotFoundError:
            pass
    
    def on_pre_enter(self):
        print(self.medidas)

    
    
        

class Test(App):
    def build(self):
        return Janelas()

Test().run()