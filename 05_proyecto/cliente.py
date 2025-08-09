# Cliente
import socket

HOST = 'localhost'
PORT = 9000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("Conectado al servidor de cálculo. Escribe 'salir' para terminar.")

while True:
    operacion = input("Ingresa operación: ")
    if operacion.lower() == 'salir':
        break

    client_socket.sendall(operacion.encode('utf-8'))
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Servidor: {data}")

client_socket.close()

