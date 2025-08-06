# Cliente

import socket

HOST = 'localhost'
PORT = 9000

mensaje = input("Digite tu mensaje: ")
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))


cliente.sendall(mensaje.encode())
print(f"Mensaje enviados: '{mensaje}'")

respuesta = cliente.recv(1024)
print(f"Respuesta del 'Echo': '{respuesta.decode()}'")

cliente.close()