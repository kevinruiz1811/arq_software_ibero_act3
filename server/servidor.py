import socket

# Configuración del servidor
HOST = '127.0.0.1'  # Dirección IP del servidor
PORT = 65432        # Puerto en el que el servidor escuchará

def procesar_operacion(operacion):
    try:
        # Evalúa la operación enviada por el cliente (por ejemplo, "2 + 3")
        resultado = eval(operacion)
        return f"Resultado: {resultado}"
    except Exception as e:
        return f"Error en la operación: {e}"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor escuchando en {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"Conexión establecida desde {addr}")
        while True:
            # Recibe la operación enviada desde el cliente
            data = conn.recv(1024)
            # valida si la información es vacía
            if not data:
                break
            operacion = data.decode()
            print(f"Operación recibida: {operacion}")
            respuesta = procesar_operacion(operacion)
            conn.sendall(respuesta.encode())  # Enviamos el resultado al cliente
