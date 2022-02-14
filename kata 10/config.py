def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print('Nose pudo encontrar el archivo config.txt')
    except IsADirectoryError:
        print('Encontre config.txt pero es un directorio, no puedo leerlo.')
    except PermissionError:
        print('No tengo permisos para leer el archivo config.txt')
    except (BlockingIOError, TimeoutError):
        print("Sistema de archivos con mucha carga, no se puede completar la lectura del archivo de configuración")

if __name__ == '__main__':
    main()