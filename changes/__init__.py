import services.databaseFunc as db
from os import strerror

# ========================= FUNÇÕES PARA SELECT, INSERT, UPDATE E DELETE PARA CLIENTES ================================

class Controllers:
    def __init__(self) -> None:
        pass

    def IncluirCliente(nome, endereco, telefone, cep, localidade, cpf):

        # Inserindo os dados do cliente via parâmetros
        try:
            sql = "INSERT INTO cliente (nome, endereco, telefone, cep, localidade, cpf) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (f'{nome}', f'{endereco}', f'{telefone}', f'{cep}', f'{localidade}', f'{cpf}')
            db.cursor.execute(sql, val)
            db.mydb.commit()
            return True
        
        except:
            return False

        
    def mostrarClientes():

        # Pegando os dados dos cliente sdo banco de dados
        sql = "SELECT id, nome, endereco, telefone, cep, localidade, cpf FROM cliente"
        db.cursor.execute(sql)
        listData = []

        for i in db.cursor.fetchall():
            listData.append(list(i))

        return listData

    def mostrarClienteNomeEcpf():

        # Pegando apenas o id, nome e cpf
        sql = "SELECT id, nome, cpf FROM cliente"
        db.cursor.execute(sql)
        listData = []

        for i in db.cursor.fetchall():
            listData.append(list(i))

        return listData


    def excluirCliente(id):

        # Excluindo clientes
        try:
            sql = f"""DELETE FROM cliente WHERE id = {id};"""
            db.cursor.execute(sql)
            db.mydb.commit()

            return True
        
        except:
            
            return False

    def alterarClientes(idCliente, nome, endereco, telefone, cep, localidade, cpf):
        #Alterando os dados do cliente enviados via parâmetros
        try:
            sql = f"""UPDATE cliente set nome = '{nome}', endereco = '{endereco}', telefone = '{telefone}',
            cep = '{cep}', localidade = '{localidade}', cpf = '{cpf}' WHERE id = {idCliente};"""
            db.cursor.execute(sql)

            return True
        
        except:

            return False
        
    # ========================= FUNÇÕES PARA SELECT, INSERT, UPDATE E DELETE PARA PRODUTOS ================================

    def getFabricantes():
        sql = "SELECT nome FROM fabricantes"
        db.cursor.execute(sql)
        listData = []

        for i in db.cursor.fetchall():
            listData.append(i[0].upper())

        return listData

    def getTipos():
        sql = "SELECT tipo FROM tipos_produtos"
        db.cursor.execute(sql)
        listData = []

        for i in db.cursor.fetchall():
            listData.append(i[0].upper())

        return listData

    def IncluirFabricante(nome):
        try:
            sql = "INSERT INTO fabricantes (nome) VALUES (%s)"
            val = (f"{nome}",)
            db.cursor.execute(sql, val)
            db.mydb.commit()
            return True
        
        except:
            return False
        
    def IncluirTipoProduto(nome):
        try:
            sql = "INSERT INTO tipos_produtos (nome) VALUES (%s)"
            val = (f"{nome}",)
            db.cursor.execute(sql, val)
            db.mydb.commit()
            return True
        
        except:
            return False
        
    def mostrarProdutos():
        sql = """SELECT p.id AS Código, p.produto AS Nome, p.info AS Info, p.composicao AS Composicao, 
    p.preco_venda AS Preço, tp.tipo AS Tipo, f.nome AS Fabricante, p.quantidade AS Quantidade FROM produtos 
    AS p, tipos_produtos AS tp, fabricantes AS f WHERE p.id_tipo_produto = tp.id AND p.id_fabricante = f.id;"""
        db.cursor.execute(sql)
        listData = []

        for i in db.cursor.fetchall():
            listData.append(list(i))

        return listData

    def IncluirMedicamento(nome, info, composicao, preco, tipo, fabricante, quantidade):

        # ---- Tipos de produtos ----

        sql = f"SELECT id FROM tipos_produtos WHERE tipo = '{tipo}'"
        db.cursor.execute(sql)
        listData = []

        for i in db.cursor.fetchall():
            listData.append(int(i[0]))

        tipo_produto = listData[0]

        # ---- Fabricantes ----

        sql = f"SELECT id FROM fabricantes WHERE nome = '{fabricante}'"
        db.cursor.execute(sql)
        listData = []

        for i in db.cursor.fetchall():
            listData.append(i[0])

        fabri = listData[0]

        try:
            sql = """INSERT INTO produtos (produto, info, composicao, preco_venda, id_tipo_produto, id_fabricante, quantidade) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            val = (f"{nome}", f"{info}", f"{composicao}", f"{preco}", f"{tipo_produto}", f"{fabri}", f"{quantidade}")
            db.cursor.execute(sql, val)
            db.mydb.commit()
            return True
        
        except IOError as e:
            return strerror(e.errno)
        
    def alterarProdutos(idProduto, produto, info, composicao, preco_venda, tipo, fabricante, quantidade):

        # Fabricantes

        sql = f"SELECT id FROM fabricantes WHERE nome = '{fabricante}'"
        db.cursor.execute(sql)
        listData = []

        for i in db.cursor.fetchall():
            listData.append(i[0])

        id_fabri = listData[0]

        # Tipo de produto

        sql = f"SELECT id FROM tipos_produtos WHERE tipo = '{tipo}'"
        db.cursor.execute(sql)
        listData = []

        for i in db.cursor.fetchall():
            listData.append(int(i[0]))

        id_tipo_produto = listData[0]

        # Interação a inclusão dos dados

        sql = f"""UPDATE produtos set produto = '{produto}', info = '{info}', composicao = '{composicao}',
        preco_venda = '{preco_venda}', id_tipo_produto = '{id_tipo_produto}', id_fabricante = '{id_fabri}', quantidade = {quantidade} WHERE id = {idProduto};"""
        db.cursor.execute(sql)

        return True

    def excluirProduto(idProduto):
        try:
            sql = f"""DELETE FROM produtos WHERE id = {idProduto};"""
            db.cursor.execute(sql)
            db.mydb.commit()

            return True
        
        except:
            
            return False
        
    