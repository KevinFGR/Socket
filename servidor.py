from socket import *

servidor = '127.0.0.1'
porta = 5000

obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((servidor,porta))
obj_socket.listen(2)
print('Aguardando cliente ...')

while True:
    con, cliente = obj_socket.accept()
    print(f'conectado com {cliente}')
    while True:
        msg_recebida = str(con.recv(1024))
        print(f'Mensagem recebida: {str(msg_recebida)[2:-1]}')
        msg_enviada = bytes(input('Resposta: '),'utf-8')
        con.send(msg_enviada)
        break
    con.close()