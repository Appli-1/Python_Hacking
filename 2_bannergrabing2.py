#usaremos socket para ejecutar una peticion
#usaremos sys para el cirre del programa
#sin usar el argparse
import socket
import sys

def banner(ip, port):   #creamos la funcion banner
    s = socket.socket() #creamos el socket
    s.connect((ip, port))  #conectamos el socket con la ip y el puerto
    print(str(s.recv(1024)).strip('b')) #imprimimos el banner del servidor
    
def main():
    ip = str(input("ingresar ip de la victima: "))   # ip de la victima
    port = int(input("ingresar puerto: "))  # puerto ftp 
    banner(ip, port)   #llamamos a la funcion banner

#creamos el cierre del programa con sys.exit() con la excepcion KeyboardInterrupt
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()