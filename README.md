# Aplicativo para la actividad 3 Cliente/Servidor

En este repositorio de GitHub, muestro el pequeño proyecto para la actividad No. 3 de Arquitectura de Software

En este proyecto se lleva a cabo una pequeña aplicación en que se ejecuta por el lado de cliente/servidor

# Ejecución desde el lado de cliente

- Se ejecuta el archivo servidor.py dentro de la carpeta server
  `python servidor.py`

En este archivo se inicia un 'servidor' en el host '127.0.0.1' y el puerto '65432'

Este archivo lo que hará es recibir una operación matemática desde el lado de cliente y devolverá la respuesta de la operación.

- Se ejecuta también el cliente dentro de la carpeta client
  `python cliente.py`

En este archivo se envía la operación matemática, después de que el servidor la procese, devolverá el resultado.
