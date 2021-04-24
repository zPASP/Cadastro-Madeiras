from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class Janelas(ScreenManager):
    pass

class Menu(Screen):
    pass

class Cadastro(Screen):
    pass

class Exibir(Screen):
    cadastros = ['a','b','c','D']
    def on_pre_enter(self):
        for cadastro in self.cadastros:
            self.ids.box_exibir.add_widget(ListarCad(text=cadastro))

    def removerCadastro(self,ListarCad):
        self.ids.box_exibir.remove_widget(ListarCad)


class ListarCad(BoxLayout):
    def __init__(self,text='',**kwargs):
        super(ListarCad, self).__init__(**kwargs)
        self.ids.label.text = text

class Test(App):
    def build(self):
        return Janelas()

Test().run()