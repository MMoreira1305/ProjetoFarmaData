import controllers.funcController as fc
import PySimpleGUI as psg
import pages.telaDeOpções as tdo
import pages.telaAlterarCliente as tal
import controllers.clientController as cc

def telaAE(idC, nome, endereco, telefone, cep, localidade, cpf):
    psg.theme("DarkBlue12")
    layout = [
    [psg.Text("Alterar ou Excluir cliente")],
    [psg.Text("\n")],
    [psg.Button("Alterar"), psg.Button("Excluir")],
    [psg.Text("\n")],
    [psg.Button("Cancelar")],
    [psg.Text("\n")]]

    window = psg.Window("Alterar e Excluir", layout=layout, element_justification="C")

    while True:
        event, values = window.Read()
        if event == psg.WIN_CLOSED or event == "Cancelar":
            window.close()
            break
        
        if event == "Alterar":
            window.close()
            tal.telaAlterarCliente(idC, nome, endereco, telefone, cep, localidade, cpf)
            break
        
        elif event == "Excluir":
            exclusao = cc.excluirCliente(idC)
            if exclusao:
                psg.popup("Cliente excluído com sucesso")
                window.close()
                break