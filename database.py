import pyodbc
import streamlit as st

dados_conexao = (
    'Driver={SQL Server};'
    'Server=DESKTOP-12J7EL8\\DLINK;'
    'Database=Teste;'
)

conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()


def incluir(nome, idade, profissao):
    comando = f'''INSERT INTO Clientes(cliNome, cliIdade, cliProfissao)
    VALUES
        ('{nome}', {idade}, '{profissao}')'''
    cursor.execute(comando)
    cursor.commit()
    st.success('Cliente adicionado com sucesso!')


def listar():
    comando = '''SELECT * FROM Clientes'''
    cursor.execute(comando)
    lista_clientes = []

    for clientes in cursor.fetchall():
        lista_clientes.append({
            'id': clientes[0],
            'nome': clientes[1],
            'idade': clientes[2],
            'profissao': clientes[3]
        })

    return lista_clientes
