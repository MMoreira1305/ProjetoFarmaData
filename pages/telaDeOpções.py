import PySimpleGUI as psg
import pages.telaCadastroCliente as tcc
import pages.telaCadastroFabricante as tcf
import pages.telaMostrarClientes as tmc
import pages.telaCadastroProdutos as tcp
import pages.telaMostrarProdutos as tmp
import pages.telaCadastrarTipoProduto as tctp

def telaOpcoes():
    psg.theme("DarkBlue12")

    layout = [
        [psg.Button("Cadastrar cliente", size=(50, 1))], 
        [psg.Button("Cadastrar fabricantes", size=(50, 1))],
        [psg.Button("Cadastrar medicamento", size=(50, 1))],
        [psg.Button("Cadastrar Tipo de Produto", size=(50, 1))],
        [psg.Button("Consultar clientes", size=(50, 1))],
        [psg.Button("Consultar medicamentos", size=(50, 1))],
    ]

    window = psg.Window("Tela de Opções - FarmaData", layout=layout, size=(320, 250), element_justification="c", margins=(30, 30))

    while True:
        event, values = window.Read()

        if event == psg.WIN_CLOSED:
            break
        elif event == "Cadastrar cliente":
            window.close()
            tcc.TelaCadastroCliente().telaCC()
        elif event == "Cadastrar fabricantes":
            window.close()
            tcf.TelaCadastroFabricante().telaCF()
        elif event == "Consultar clientes":
            window.close()
            tmc.ShowClients().telaMC()
        elif event == "Cadastrar medicamento":
            window.close()
            tcp.TelaCadastroProduto().telaCP()
        elif event == "Consultar medicamentos":
            window.close()
            tmp.ShowProducts().tela()
        elif event == "Cadastrar Tipo de Produto":
            window.close()
            tctp.telaCTP()


