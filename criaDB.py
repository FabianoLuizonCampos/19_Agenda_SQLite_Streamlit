import sql_funcoes as sf

nomeDB = "cadastro.db"
nomeTabela = "Clientes"


# Criar tabela com os campos especificados
campos = {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "nome": "TEXT NOT NULL",
        "sobrenome": "TEXT NOT NULL",
        "email": "TEXT NOT NULL"
    }

sf.criarTabela(nomeDB, nomeTabela, campos)