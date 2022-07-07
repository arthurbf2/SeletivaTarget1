def fibonacci(x):
    n = 2
    lista = [0, 1]
    while n < 31:
        valor = lista[n-2] + lista[n-1]
        lista.append(valor)
        n = n + 1

    if x in lista:
        print(f'O número {x} está presente na sequência de fibonacci')
    else:
        print(f'O número {x} não está presente na sequência de fibonacci')
