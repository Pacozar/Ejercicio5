def numeroPrimo():

    while True:
        try:
            numero = int(input('Escribe un numero: \n'))
            break
        except:
            print('Escribe un numero valido')
    if numero == 1:
        print(numero, 'es un numero especial')

    for valorActual in range(1, numero):
        if numero == 2:
            print(numero, 'es primo')
        elif valorActual == 1:
            continue
        elif numero % valorActual == 0:
            print(numero, 'no es primo', valorActual, 'es su divisor')
            break
        elif valorActual + 1 == numero:
            print(numero, 'es primo')

    numeroPrimo()

numeroPrimo()