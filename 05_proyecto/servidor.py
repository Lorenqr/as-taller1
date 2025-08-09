# Servidor
import socket

HOST = 'localhost'
PORT = 9000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Servidor de cálculo escuchando en {HOST}:{PORT}")

while True:
    conn, addr = server_socket.accept()
    print(f"Cliente conectado desde {addr}")

    while True:
        data = conn.recv(1024).decode('utf-8')
        if not data:
            break
        print(f"Operación recibida: {data}")

        try:
            resultado = eval(data)  # Evalúa la operación
            respuesta = f"Resultado: {resultado}"
        except:
            respuesta = "Error: Operación inválida"

        conn.sendall(respuesta.encode('utf-8'))

    conn.close()
    print("Conexión cerrada")

