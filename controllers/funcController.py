import services.databaseFunc as dbf
def verfFunc(user):
    sql = f"SELECT senha FROM permissions WHERE login = '{user}'"
    dbf.cursor.execute(sql)
    passdb = dbf.cursor.fetchall()

    for Device in passdb:
        dev = Device[0]
    
    return dev