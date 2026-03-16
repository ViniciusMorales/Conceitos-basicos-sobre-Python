#Analisando Tuplas com all() e any()

numeros = [-100, -80, -60, -40, -20, 0, 10, 20, 30, 40, 50]

all_positive = all(num > 0 for num in numeros)
print(f'Todos os números são positivos? {all_positive}')

any_positive = any(num > 0 for num in numeros)
print(f'Existe algum número positivo? {any_positive}')



