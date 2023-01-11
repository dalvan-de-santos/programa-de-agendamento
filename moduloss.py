from time import sleep
import mysql.connector

def horarios_disponiveis():
    ...

def botcadastro(n, d, h):
    nm = n
    da = d
    hr = h
    con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_clientes"
    )
    cursor = con.cursor()
    cursor.execute("INSERT INTO clientes (nome, dia, hora) VALUES (%s, %s, %s)", (n, d, h));





def botmsg():
    print('\033[36m<º>\033[m: \033[34mOla eu sou o bot de agendamentos!\033[m\n...')
    sleep(3)
    print('\033[36m<º>\033[m: \033[34mSou responsavel por fazer os agendamentos dos clientes!\033[m\n...')
    sleep(3)

    print('\033[36m<º>\033[m: \033[34mInforme seu nome completo! por favor\033[m')
    no = str(input('Você: '))
    sleep(3)
    print('\033[36m<º>\033[m: \033[34m Agora Informe o dia! por favor\033[m')
    print('...')
    di = str(input('Você: '))
    print('...')
    sleep(3)
    print('\033[36m<º>\033[m: \033[34m Por ultimo Informe a hora! por favor\033[m')
    ho = str(input('Você: '))

    botcadastro(no, di, ho)