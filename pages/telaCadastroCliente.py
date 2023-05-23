import controllers.funcController as fc
import controllers.clientController as cc
import PySimpleGUI as psg
import pages.telaDeOpções as tdo

class TelaCadastroCliente:
    def __init__(self):
        self.nome = ""
        self.endereco = ""
        self.telefone = ""
        self.cep = ""
        self.localidade = ""
        self.cpf = ""

    def telaCC(self):
        psg.theme("DarkBlue12")
        layout = [
            [psg.Text('Cadastro de cliente')],
            [psg.Text("")],
            [psg.Text("Nome: ", size=(10,0)), psg.InputText(size=(50, 0), key="nome", do_not_clear=False)],
            [psg.Text("Endereco: ", size=(10,0)), psg.InputText(size=(50, 0), key="endereco", do_not_clear=False)],
            [psg.Text("Telefone: ", size=(10,0)), psg.InputText(size=(50, 0), key="telefone", do_not_clear=False)],
            [psg.Text("CEP: ", size=(10,0)), psg.InputText(size=(50, 0), key="cep", do_not_clear=False)],
            [psg.Text("Localidade: ", size=(10,0)), psg.InputText(size=(50, 0), key="localidade", do_not_clear=False)],
            [psg.Text("CPF/CNPJ: ", size=(10,0)), psg.InputText(size=(50, 0), key="cpf", do_not_clear=False)],
            [psg.Text("\n")],
            [psg.Button("Cancelar"), psg.Button("Confirmar")],
            [psg.Text("", key="mensagem")]]

        window = psg.Window("Login FarmaData", layout=layout, size=(400, 350), element_justification="c", margins=(30, 30))

        while True:
            event, values = window.Read()
            if event == psg.WIN_CLOSED or event == "Cancelar":
                window.close()
                tdo.telaOpcoes()
                break
            elif event == "Confirmar":
                self.nome = values['nome']
                self.endereco = values['endereco']
                self.telefone = values['telefone']
                self.cep = values['cep']
                self.localidade = values['localidade']
                self.cpf = values['cpf']

                incluir = cc.IncluirCliente(self.nome, self.endereco, self.telefone, self.cep, self.localidade, self.cpf)
                if incluir == True:
                    psg.popup("Cliente inserido com sucesso.")
                else:
                    psg.popup("Erro ao inserir cliente, verifique os dados.")

                window.refresh()