valor = int(input('Valor do numero para identificar se e primo:'))
flag = False


if valor > 1:
    for i in range(2, valor):
        if (valor % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

if flag:
    print(valor, "Valor nao e primo")
else:
    print(valor, "valor e primo")