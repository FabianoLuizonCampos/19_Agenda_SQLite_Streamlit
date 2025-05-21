import streamlit as st
import sql_funcoes as sf

dados = [ ["","","",""]]        


# print(dados[0][1])

st.set_page_config(page_title="Sistema de Cadastro de Cliente", page_icon=":bar_chart:", layout="wide")

# Título da aplicação
st.title("Sistema de Cadastro de Cliente")

num_registro = st.number_input("Número do Cadastro", min_value=1, step=1)

if st.button("Buscar"):
    nomeDB = "cadastro.db"
    nomeTabela = "Clientes"

    # Selecionar dados por ID
    dados = sf.selecionarDadosId(nomeDB, nomeTabela, num_registro)

    if dados:
        st.success("Cliente encontrado!")
        st.write(dados)
        print(dados)
    else:
        st.error("Cliente não encontrado!")


with st.form ("Alterar Cadastro de Cliente"):
    
    if dados not in st.session_state:
        text_input_nome = st.text_input("Nome", value=dados[0][1])
        text_input_sobrenome = st.text_input("Sobrenome", value=dados[0][2])          
        text_input_email = st.text_input("Email", value=dados[0][3])

        if st.form_submit_button("Atualizar"):
            if text_input_nome and text_input_sobrenome and text_input_email:
                nomeDB = "cadastro.db"
                nomeTabela = "Clientes"

                # Inserir dados na tabela
                registro = {        
                        "nome": text_input_nome,
                        "sobrenome": text_input_sobrenome,
                        "email": text_input_email,        
                }

                print(text_input_name)

                st.write("Registro:", registro)
                
                # sf.atualizarDados(nomeDB, nomeTabela, registro)        
                st.success("Cliente cadastrado com sucesso!")

                
            else:
                st.error("Por favor, preencha todos os campos.")