import socket

# Configuración del cliente
HOST = '127.0.0.1'  # Dirección IP del servidor
PORT = 65432        # Puerto del servidor al que conectarse

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        operacion = input("Ingresa una operación matemática (o 'salir' para terminar): ")
        if operacion.lower() == "salir":
            break
        s.sendall(operacion.encode())
        data = s.recv(1024)
        print(f"Respuesta del servidor: {data.decode()}")
