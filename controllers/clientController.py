import services.databaseFunc as db

def IncluirCliente(nome, endereco, telefone, cep, localidade, cpf):
    try:
        sql = "INSERT INTO cliente (nome, endereco, telefone, cep, localidade, cpf) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (f'{nome}', f'{endereco}', f'{telefone}', f'{cep}', f'{localidade}', f'{cpf}')
        db.cursor.execute(sql, val)
        db.mydb.commit()
        return True
    
    except:
        return False

    
def mostrarClientes():
    sql = "SELECT id, nome, endereco, telefone, cep, localidade, cpf FROM cliente"
    db.cursor.execute(sql)
    listData = []

    for i in db.cursor.fetchall():
        listData.append(list(i))

    return listData

def mostrarClienteNomeEcpf():
    sql = "SELECT id, nome, cpf FROM cliente"
    db.cursor.execute(sql)
    listData = []

    for i in db.cursor.fetchall():
        listData.append(list(i))

    return listData


def excluirCliente(id):
    try:
        sql = f"""DELETE FROM cliente WHERE id = {id};"""
        db.cursor.execute(sql)
        db.mydb.commit()

        return True
    
    except:
        
        return False

def alterarClientes(idCliente, nome, endereco, telefone, cep, localidade, cpf):
    sql = f"""UPDATE cliente set nome = '{nome}', endereco = '{endereco}', telefone = '{telefone}',
    cep = '{cep}', localidade = '{localidade}', cpf = '{cpf}' WHERE id = {idCliente};"""
    db.cursor.execute(sql)

    return True