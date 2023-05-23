import controllers.clientController as cc
import PySimpleGUI as psg
import pages.telaAlterarExcluirCliente as talc
import pages.telaDeOpções as tdo

class ShowClients:
    def __init__(self):
        self.dataClient = cc.mostrarClientes()
        self.headings = ["Id", "Nome", "Endereco", "Telefone", "Cep", "Localidade", "CPF/CNPJ"]
    def telaMC(self):
        psg.theme("DarkBlue12")
        layout = [
            [psg.Table(values=self.dataClient,
                        headings=self.headings,
                        auto_size_columns=True,
                        max_col_width=35,
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
                informacao_cliente = self.dataClient[numero_linha_selecionada]

                talc.telaAE(informacao_cliente[0], informacao_cliente[1], informacao_cliente[2],
                            informacao_cliente[3], informacao_cliente[4], informacao_cliente[5],
                              informacao_cliente[6])
                window.refresh()