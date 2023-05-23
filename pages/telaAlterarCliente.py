import controllers.funcController as fc
import controllers.clientController as cc
import PySimpleGUI as psg


def telaAlterar(idClient, name, adress, number, number_postal, location, number_cpf):
    psg.theme("DarkBlue12")
    layout = [
        [psg.Text('Alteração de cliente')],
        [psg.Text("")],
        [psg.Text("Nome: ", size=(10,0)), psg.InputText(f"{name}", size=(50, 0), key="nome")],
        [psg.Text("Endereco: ", size=(10,0)), psg.InputText(f"{adress}", size=(50, 0), key="endereco")],
        [psg.Text("Telefone: ", size=(10,0)), psg.InputText(f"{number}", size=(50, 0), key="telefone")],
        [psg.Text("CEP: ", size=(10,0)), psg.InputText(f"{number_postal}", size=(50, 0), key="cep")],
        [psg.Text("Localidade: ", size=(10,0)), psg.InputText(f"{location}", size=(50, 0), key="localidade")],
        [psg.Text("CPF/CNPJ: ", size=(10,0)), psg.InputText(f"{number_cpf}", size=(50, 0), key="cpf")],
        [psg.Text("\n")],
        [psg.Button("Cancelar"), psg.Button("Confirmar")],
        [psg.Text("", key="mensagem")]]

    window = psg.Window("Login FarmaData", layout=layout, size=(400, 350), element_justification="c", margins=(30, 30))

    while True:
        event, values = window.Read()
        if event == psg.WIN_CLOSED or event == "Cancelar":
            window.close()
            break
        elif event == "Confirmar":
            nome = values['nome']
            endereco = values['endereco']
            telefone = values['telefone']
            cep = values['cep']
            localidade = values['localidade']
            cpf = values['cpf']

            alterar = cc.alterarClientes(idClient, nome, endereco, telefone, cep, localidade, cpf)
            if alterar == True:
                psg.popup("Cliente alterado com sucesso.")