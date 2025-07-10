import sys

def solveMeFirst(a, b, c):
    # Retorna la suma de los dos números
    return a + b + c

def solveMeSecond(a, b):
    return a * b

if __name__ == '__main__':
    try:
        num1 = int(input().strip())
        num2 = int(input().strip())
        num3 = int(input().strip())
    except ValueError:    
        print(f'debes de ingresar los valores')
        sys.exit(1)   
    res = solveMeFirst(num1, num2, num3)     
    print(res)

    try:
        num1 = int(input().strip())
        num2 = int(input().strip())
    except ValueError:    
        print(f'debes de ingresar los valores')
        sys.exit(1)    
    res = solveMeSecond(num1, num2)
    print(res)


#     import sys

# def solveMeFirst(a, b, c):
#     return a + b + c

# def solveMeSecond(a, b):
#     return a * b

# if __name__ == '__main__':
#     try:
#         # Lee todas las entradas de una sola vez
#         nums = list(map(int, sys.stdin.read().split()))
#         a, b, c, x, y = nums
#     except (ValueError, ValueError, IndexError):
#         print('Se esperaban 5 números enteros.')
#         sys.exit(1)

#     print(solveMeFirst(a, b, c))
#     print(solveMeSecond(x, y))