import streamlit as st
import sql_funcoes as sf

st.set_page_config(page_title="Sistema de Cadastro de Cliente", page_icon=":bar_chart:", layout="wide")

# Título da aplicação
st.title("Sistema de Cadastro de Cliente")

with st.form ("Cadastro de Cliente"):
    text_input_name = st.text_input("Nome")
    text_input_sobrenome = st.text_input("Sobrenome")
    text_input_email = st.text_input("Email")

    if st.form_submit_button("Cadastrar"):
        if text_input_name and text_input_sobrenome and text_input_email:
            nomeDB = "cadastro.db"
            nomeTabela = "Clientes"

            # Inserir dados na tabela
            registro = {        
                    "nome": text_input_name,
                    "sobrenome": text_input_sobrenome,
                    "email": text_input_email        
            }
            
            sf.inserirDados(nomeDB, nomeTabela, registro)        
            st.success("Cliente cadastrado com sucesso!")

            
        else:
            st.error("Por favor, preencha todos os campos.")

    # if st.button("Limpar"):
    #     st.experimental_rerun()