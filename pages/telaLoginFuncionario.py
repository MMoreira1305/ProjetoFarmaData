import time
import controllers.funcController as fc
import PySimpleGUI as psg
import pages.telaDeOpções as tdo

class TelaLogin:
    def __init__(self):
        self.usuario = ""
        self.senha = ""

    def telaLogin(self):
        psg.theme("DarkBlue12")
        layout = [
        [psg.Text("Login", size=(5,0)), psg.InputText(size=(25, 0), key="login")],
        [psg.Text("Senha", size=(5,0)), psg.InputText(size=(25, 0), key="senha")],
        [psg.Text("\n")],
        [psg.Button("Cancelar"), psg.Button("Confirmar")],
        [psg.Text("", key="mensagem")]]

        window = psg.Window("Login FarmaData", layout=layout)

        while True:
            event, values = window.Read()
            if event == psg.WIN_CLOSED or event == "Cancelar":
                break
            elif event == "Confirmar":
                self.usuario = values['login']
                self.senha = values['senha']

                if self.senha == fc.verfFunc(self.usuario):
                    psg.popup("Seja bem-vindo!")
                    window.close()
                    tdo.telaOpcoes()

    def getUsuario(self):
        return self.usuario
    
    def getSenha(self):
        return self.senha