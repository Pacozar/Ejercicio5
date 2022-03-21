import math


def triangulo():
    while True:
        try:
            base = int(input('Base del triangulo: \n'))
            altura = int(input('Altura del triangulo: \n'))
            break
        except:
            print('Escribe una longitud valida')

    areat = (base * altura) // 2
    print('El area del triangulo es de', areat)


def circulo():
    while True:
        try:
            radio = int(input('Radio del Circulo: \n'))
            break
        except:4
            print('Escribe una longitud valida')

    areac = math.pi * (radio ** 2)
    print('El diametro del circulo es de ', areac)


triangulo()
circulo()
