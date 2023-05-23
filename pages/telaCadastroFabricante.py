import controllers.estController as ec
import PySimpleGUI as psg
import pages.telaDeOpções as tdo

class TelaCadastroFabricante:
    def __init__(self):
        self.nome = ""

    def telaCF(self):
        psg.theme("DarkBlue12")
        layout = [
            [psg.Text('Cadastro de fabricante')],
            [psg.Text("")],
            [psg.Text("Nome: ", size=(5,0)), psg.InputText(size=(25, 0), key="nome", do_not_clear=False)],
            [psg.Text("")],
            [psg.Button("Cancelar"), psg.Button("Confirmar")]]

        window = psg.Window("FarmaData", layout=layout, size=(320, 200), element_justification="c", margins=(30, 30))

        while True:
            event, values = window.Read()
            if event == psg.WIN_CLOSED or event == "Cancelar":
                window.close()
                tdo.telaOpcoes()
                break
            elif event == "Confirmar":
                self.nome = values['nome']

                incluir = ec.IncluirFabricante(self.nome)

                if incluir == True:
                    psg.popup("Fabricante inserido com sucesso!")
                else:
                    psg.popup("Erro ao inserir fabricante.")