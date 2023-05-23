import controllers.estController as ec
import PySimpleGUI as psg
import pages.telaDeOpções as tdo


def telaCTP():
    psg.theme("DarkBlue12")
    layout = [
        [psg.Text('Cadastro de Tipo de Produto')],
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
            nome = values['nome']

            incluir = ec.IncluirFabricante(nome.upper())

            if incluir == True:
                psg.popup("Tipo de produto inserido com sucesso!")
            else:
                psg.popup("Erro ao inserir tipo de produto.")