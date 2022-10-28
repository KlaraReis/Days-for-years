def triangle(a, b, c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False


valor_one = float(input('Valor do primeiro lado:'))
valor_two = float(input('Valor do segundo lado:'))
valor_third = float(input('EValor do terceiro lado:'))

# funcao de decisao

if triangle(valor_one, valor_two, valor_third):
    print('e um triangulo.')
else:
    print('nao e um triangulo')


