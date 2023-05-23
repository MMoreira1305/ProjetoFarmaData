from os import strerror
import controllers.funcController as fc
import controllers.estController as ec
import PySimpleGUI as psg
import pages.telaDeOpções as tdo

class TelaCadastroProduto:
    def __init__(self):
        self.nome = ""
        self.info = ""
        self.composicao = ""
        self.preco = 0
        self.tipo = ""
        self.fabricante = ""
        self.quantidade = 0

    def telaCP(self):
        psg.theme("DarkBlue12")
        layout = [
            [psg.Text('Cadastro de medicamentos')],
            [psg.Text("")],
            [psg.Text("Nome do medicamento: ", size=(25,0)), psg.InputText(size=(40, 0), key="produto", do_not_clear=False)],
            [psg.Text("Informação do produto: ", size=(25,0)), psg.InputText(size=(40, 0), key="info", do_not_clear=False)],
            [psg.Text("Composição: ", size=(25,0)), psg.InputText(size=(40, 0), key="composicao", do_not_clear=False)],
            [psg.Text("Preço: ", size=(25,0)), psg.InputText(size=(40, 0), key="preco", do_not_clear=False)],
            [psg.Text("Tipo do remédio: ", size=(25,0)), psg.Combo(ec.getTipos(), key='tipo', size=(38, 0))],
            [psg.Text("Fabricante: ", size=(25,0)), psg.Combo(ec.getFabricantes(), key='fabricante', size=(38, 0))],
            [psg.Text("Quantidade: ", size=(25,0)), psg.InputText(size=(40, 0), key="quantidade", do_not_clear=False)],
            [psg.Text("\n")],
            [psg.Button("Cancelar"), psg.Button("Confirmar")],
            [psg.Text("", key="mensagem")]]

        window = psg.Window("FarmaData", layout=layout, size=(800, 600), element_justification="c", margins=(30, 30))

        while True:
            event, values = window.Read()
            if event == psg.WIN_CLOSED or event == "Cancelar":
                window.close()
                tdo.telaOpcoes()
                break
            elif event == "Confirmar":
                self.nome = values['produto']
                self.info = values['info']
                self.composicao = values['composicao']
                self.preco = values['preco']
                self.tipo = values['tipo']
                self.fabricante = values['fabricante']
                self.quantidade = values['quantidade']

                incluir = ec.IncluirMedicamento(self.nome, self.info, self.composicao, self.preco, self.tipo, self.fabricante, self.quantidade)
                if incluir:
                    psg.popup("Produto inserido com sucesso")
                else:
                    psg.popup("erro", incluir)