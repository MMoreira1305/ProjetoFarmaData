import controllers.estController as ec
import controllers.clientController as cc
import PySimpleGUI as psg


def telaAlterarProduto(idProduct, product, information, composition, price, typek, fabri, quantity):
    psg.theme("DarkBlue12")
    layout = [
        [psg.Text('Alteração de medicamentos')],
        [psg.Text("")],
        [psg.Text("Nome do medicamento: ", size=(25,0)), psg.InputText(f'{product}', size=(40, 0), key="produto")],
        [psg.Text("Informação do produto: ", size=(25,0)), psg.InputText(f'{information}', size=(40, 0), key="info")],
        [psg.Text("Composição: ", size=(25,0)), psg.InputText(f'{composition}', size=(40, 0), key="composicao")],
        [psg.Text("Preço: ", size=(25,0)), psg.InputText(f'{price}', size=(40, 0), key="preco")],
        [psg.Text("Tipo do remédio: ", size=(25,0)), psg.Combo(ec.getTipos(), key='tipo', size=(38, 0))],
        [psg.Text("Fabricante: ", size=(25,0)), psg.Combo(ec.getFabricantes(), key='fabricante', size=(38, 0))],
        [psg.Text("Quantidade: ", size=(25,0)), psg.InputText(f'{quantity}', size=(40, 0), key="quantidade")],
        [psg.Text("\n")],
        [psg.Button("Cancelar"), psg.Button("Confirmar")],
        [psg.Text("", key="mensagem")]]

    window = psg.Window("Alteração Medicamento", layout=layout, size=(800, 600), element_justification="c", margins=(30, 30))

    while True:
        event, values = window.Read()
        if event == psg.WIN_CLOSED or event == "Cancelar":
            window.close()
            break
        elif event == "Confirmar":
            produto = values['produto']
            info = values['info']
            composicao = values['composicao']
            preco = values['preco']
            tipo = values['tipo']
            fabricante = values['fabricante']
            quantidade = values['quantidade']

            alterar = ec.alterarProdutos(idProduct, produto, info, composicao, preco, tipo, fabricante, quantidade)
            if alterar == True:
                psg.popup("Produto alterado com sucesso.")