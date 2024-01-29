#usaremos socket para ejecutar una peticion
#usaremos sys para el cirre del programa
import socket
import sys
import argparse

#argparse nos permite crear argumentos en la terminal
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help='indicar el dominio de la victima')
parser = parser.parse_args()

def banner(ip, port):   #creamos la funcion banner
    s = socket.socket() #creamos el socket
    s.connect((ip, port))  #conectamos el socket con la ip y el puerto
    print(str(s.recv(1024)).strip('b')) #imprimimos el banner del servidor
    
def main():
    if parser.target:   #si parser.target es verdadero
        ip = parser.target  # ip de la victima
        port = 21  # puerto ftp
        banner(ip, port)   #llamamos a la funcion banner
    else:
        print("(-) ingresar ip de la victima")


#creamos el cierre del programa con sys.exit() con la excepcion KeyboardInterrupt
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()