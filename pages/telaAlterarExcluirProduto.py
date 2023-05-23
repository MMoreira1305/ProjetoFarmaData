import PySimpleGUI as psg
import pages.telaAlterarProduto as talp
import controllers.estController as ec

def telaAlterarExcluirProduto(idP, produto, info, composicao, preco, tipo, fabricante, quantidade):
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
            talp.telaAlterarProduto(idP, produto, info, composicao, preco, tipo, fabricante, quantidade)
            break
        
        elif event == "Excluir":
            exclusao = ec.excluirProduto(idP)
            if exclusao:
                psg.popup("Produto excluído com sucesso")
                window.close()
                break

            else:
                psg.popup("Erro ao excluir produto")