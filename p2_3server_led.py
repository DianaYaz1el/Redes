import socket
import serial
import time

# --- Configuración del Arduino (puerto serie) ---
SERIAL_PORT = "/dev/ttyACM0"
BAUDRATE = 9600

ser = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1)
time.sleep(2)  # tiempo para que el Arduino se reinicie

print("Puerto serie abierto:", SERIAL_PORT)

# --- Configuración del servidor TCP ---
HOST = "0.0.0.0"   # escucha en todas las interfaces
PORT = 5000        # puerto del servidor

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)

print(f"Servidor escuchando en puerto {PORT}...")

try:
    while True:
        conn, addr = sock.accept()
        print("Conexión desde:", addr)
        with conn:
            data = conn.recv(1)   # leer 1 byte
            if data in (b'0', b'1'):
                print("Recibido:", data)
                ser.write(data)   # mandar al Arduino
            else:
                print("Dato inválido:", data)
except KeyboardInterrupt:
    print("Cerrando servidor...")
finally:
    ser.close()
    sock.close()
