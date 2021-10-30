import streamlit as st
#import database as db
import pandas as pd
#import pywhatkit as kit

st.title('Adicionar Cliente')

st.sidebar.title('Menu')
crud = st.sidebar.selectbox('Clientes', ['Visualizar', 'Adicionar', 'Editar', 'Excuir'])


if crud == 'Adicionar':
    with st.form(key='include_cliente'):
        input_name = st.text_input(label='Insira o seu nome')
        input_age = st.number_input(label='Insira a sua idade', format='%i', step=1)
        input_occupation = st.selectbox('Selecione sua profissão', ['Desenvoledor', 'Programador', 'Designer'])
        input_button_submit = st.form_submit_button('Enviar')

    #if input_button_submit:
   #     db.incluir(nome=input_name, idade=input_age, profissao=input_occupation)
     #   kit.sendwhatmsg('+553888597211', 'Teste', 22, 50)
        
elif crud == 'Visualizar':
    lista_clientes = []

  #  for cliente in db.listar():
 #       lista_clientes.append([cliente['nome'], cliente['idade'], cliente['profissao']])

    df = pd.DataFrame(
        lista_clientes,
        columns=['Nome''', 'Idade', 'Profissao']
    )

    st.table(df)
