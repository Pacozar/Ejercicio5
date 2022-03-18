def bisiesto():
    while True:
        try:
            numero = int(input('Escribe un año: \n'))
            break
        except:
            print('Escribe un año valido')

    if numero % 4 == 0:
        print(numero, 'es un año bisiesto')
    elif numero % 4 != 0:
        print(numero, 'no es un año bisiesto')

    bisiesto()
bisiesto()
