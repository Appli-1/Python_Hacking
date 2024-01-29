import subprocess
import sys

def main():     #creamos la funcion main
    target = input("Por favor, ingrese la URL (e.g https://ejemplo.com): ")
    if target: 
        subprocess.call('wad -u'+ target+ "> tecnologias.txt", shell=True) #ejecutamos el comando wad con subprocess.run() pasandole la url de argparser creando un archivo llamado tecnologias.txt
        tecnologias = open('tecnologias.txt', 'r') #abrimos el archivo tecnologias.txt en modo lectura
        tecnologias = tecnologias.read() #leemos el archivo tecnologias.txt
        tecnologias = tecnologias.split('[') #quitamos los caracteres '{' del archivo tecnologias.txt
        tecnologias = tecnologias[1].split(']') #quitamos los caracteres '}' del archivo tecnologias.txt
        tecnologias = tecnologias[0].split('{') #quitamos los caracteres '[' del archivo tecnologias.txt
        
        for tecnologia in tecnologias: #creamos un bucle for para imprimir las tecnologias en la terminal
            nuevo = tecnologia.replace('\n', '') #quitamos los caracteres '\n' del archivo tecnologias.txt
            nuevo = nuevo.replace('                  ', '') #quitamos los caracteres '}' del archivo tecnologias.txt
            nuevo = nuevo.replace('"', '') 
            nuevo = nuevo.split('}') 
            nuevo = nuevo[0]  
            nuevo = nuevo.replace(',', '\n')
            print(nuevo)
            print("*"*20)
    else:
        print("(-) ingresar URL") #si parser.target es falso

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()