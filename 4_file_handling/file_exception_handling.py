try:
    with open('nofile.txt') as f:
        print(f.read())
except FileNotFoundError:
    print("Archivo no encontrado")