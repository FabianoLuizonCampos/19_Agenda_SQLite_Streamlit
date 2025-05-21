# Biblioteca para Banco de Dados Usando SQLite3
import sqlite3

# ---------------------- CRIAR TABELA ----------------------
def criarTabela(nomeDB, nomeTabela, campos):

    conn = sqlite3.connect(nomeDB)
    cursor = conn.cursor()

    colunas = ', '.join([f'"{campo}" {tipo}' for campo, tipo in campos.items()])
    queryTable= f'''CREATE TABLE IF NOT EXISTS "{nomeTabela}" (
        {colunas}
    );'''

    cursor.execute(queryTable)
    conn.commit()
    conn.close()

# ----------------------- INSERIR DADOS -----------------------------
def inserirDados(nomeDB, nomeTabela, registro):

    conn = sqlite3.connect(nomeDB)
    cursor = conn.cursor()

    colunas = ', '.join([f'{campo}' for campo in registro.keys()])
    valores = ', '.join([f'"{campo}"' for campo in registro.values()])

    queryInsert = f'''INSERT INTO {nomeTabela} ({colunas})
        VALUES({valores})
    '''    

    cursor.execute(queryInsert)
    conn.commit()
    conn.close()

# ------------------------ ATUALIZAR DADOS ---------------------------
def atualizarDados(nomeDB, nomeTabela, registro):

    conn = sqlite3.connect(nomeDB)
    cursor = conn.cursor()

    for campo, valor in registro.items():
        if valor != '':
            queryUpdate = f'''UPDATE {nomeTabela} SET {campo}="{valor}" 
                WHERE id="{registro['id']}";'''        
            cursor.execute(queryUpdate)
            conn.commit()

    conn.close()

def apagarDados(nomeDB, nomeTabela, numRegistro):

    conn = sqlite3.connect(nomeDB)
    cursor = conn.cursor()

    queryDelete = f'''DELETE FROM {nomeTabela}
        WHERE id="{numRegistro}";'''
    
    cursor.execute(queryDelete)

    conn.commit()
    conn.close()

def selecionarTodosDados(nomeDB, nomeTabela):

    conn = sqlite3.connect(nomeDB)
    cursor = conn.cursor()

    querySelect = f'''SELECT * FROM {nomeTabela};'''

    cursor.execute(querySelect)
    dados  = cursor.fetchall()

    conn.commit()
    conn.close()

    return dados

def selecionarDadosId(nomeDB, nomeTabela, numRegistro):

    conn = sqlite3.connect(nomeDB)
    cursor = conn.cursor()

    querySelect = f'''SELECT * FROM {nomeTabela} 
        WHERE id="{numRegistro}";'''    

    cursor.execute(querySelect)
    dados  = cursor.fetchall()

    conn.commit()
    conn.close()

    return dados




# # ------------------------ EXEMPLO DE USO ---------------------------
# # Este exemplo de uso pode ser removido ou comentado quando você estiver 
# # usando a biblioteca em outro lugar.

# nomeDB = "agenda.db"
# nomeTabela = "Contatos"


# # Criar tabela com os campos especificados
# campos = {
#         "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
#         "nome": "TEXT NOT NULL",
#         "sobrenome": "TEXT NOT NULL",
#         "idade": "INTEGER NOT NULL"
#     }

# sf.criarTabela(nomeDB, nomeTabela, campos)


# # Inserir dados na tabela
# registro = {        
#         "nome": "Pedro",
#         "sobrenome": "Alvarez",
#         "idade": 84        
#     }

# sf.inserirDados(nomeDB, nomeTabela, registro)

# # Atualizar dados na tabela
# registro = { 
#         "id": 1,       
#         "nome": "Pedro",
#         "sobrenome": "Cabral",
#         "idade": 66        
#     }

# sf.atualizarDados(nomeDB, nomeTabela, registro)

# # Apagar dados na tabela 
# numRegistro = 1
# sf.apagarDados(nomeDB, nomeTabela, numRegistro)

# # Selecionar todos os dados da tabela
# dados = sf.selecionarTodosDados(nomeDB, nomeTabela)
# print(dados)

# # Selecionar dados por ID
# numRegistro = 1
# dados = sf.selecionarDadosId(nomeDB, nomeTabela, numRegistro)
# print(dados)