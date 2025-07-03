def decorador(func):
    def wrapper():
        print("Antes")
        func()
        print("Después")
    return wrapper