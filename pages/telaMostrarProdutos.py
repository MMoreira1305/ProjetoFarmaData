import controllers.estController as ec
import PySimpleGUI as psg
import pages.telaDeOpções as tdo
import pages.telaAlterarExcluirProduto as talp

class ShowProducts:
    def __init__(self):
        self.dataProducts = ec.mostrarProdutos()
        self.headings = ["Código", "Produto", "Info", "Composição", "Preço", "Tipo", "Fabricante", "Quantidade"]
    def tela(self):
        psg.theme("DarkBlue12")
        layout = [
            [psg.Table(values=self.dataProducts,
                        headings=self.headings,
                        auto_size_columns=True,
                        max_col_width=50,
                        display_row_numbers=False,
                        justification='center',
                        num_rows=10,
                        key="-CONTATO-NA-TABELA-",
                        enable_events=True,
                        row_height=35)
            ],
            [psg.Text("")],
            [psg.Button("Cancelar")]
        ]

        window = psg.Window("FarmaData", layout=layout)

        while True:
            event, values = window.Read()
            if event == psg.WIN_CLOSED or event == "Cancelar":
                window.close()
                tdo.telaOpcoes()
                break
        
            if event == "-CONTATO-NA-TABELA-":
                numero_linha_selecionada = values["-CONTATO-NA-TABELA-"][0]
                informacao_produto = self.dataProducts[numero_linha_selecionada]
                
                talp.telaAlterarExcluirProduto(informacao_produto[0], informacao_produto[1], informacao_produto[2],
                            informacao_produto[3], informacao_produto[4], 
                            informacao_produto[5], informacao_produto[6], informacao_produto[7])
                window.refresh()


