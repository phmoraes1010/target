fibonacci = [0,1]
valorFinal = 0
valorDigitado = input('Escreva um número: ')

while valorFinal < valorDigitado:
    ultimoNumero = fibonacci[-1]
    penultimoNumero = fibonacci[-2]
    valor = ultimoNumero + penultimoNumero
    fibonacci.append(valor)
    valorFinal = fibonacci[-1]
    print(fibonacci)
