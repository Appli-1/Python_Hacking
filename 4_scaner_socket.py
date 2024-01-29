import sys   #impoortamos sys para el cierre del programa con ctrl+c
import socket  #importamos socket para la conexion
from datetime import datetime  #importamos datetime para el tiempo de ejecucion


def main ():
    Target = int(input("ingrese la ip a escanear: "))  #variable para la ip
    port_min = int(input("ingrese el puerto minimo: "))  #variable para el puerto minimo
    port_max = int(input("ingrese el puerto maximo: "))  #variable para el puerto maximo
    
    print(""*46)  #imprimimos 20 espacios
    print("La ip es: "+Target)  #imprimimos la ip
    print("inicio de escaneo: "+str(datetime.now()))  #imprimimos el tiempo de inicio
    print(""*20)  #imprimimos 20 espacios
    
    for port in range(1, 65535):  #recorremos los puertos
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creamos el socket el af_inet es para ipv4 y el sock_stream es para tcp
        socket.setdefaulttimeout(1)  #definimos el tiempo de espera si no se conecta en 1 segundo se cierra
        result = s.connect_ex((Target, port)) #conectamos al objetivo y al puerto
        
        if result == 0:  #si el resultado es 0
            print("(+) el puerto {} esta abierto".format(port))  #imprimimos el puerto
            
            s.close() #cerramos el socket
    


if __name__ == "__main__":
    try:
        main()  #llamamos a la funcion main
    except KeyboardInterrupt:  #si se presiona ctrl+c
        sys.exit()  #cerramos el programa