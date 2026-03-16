# Trocando os valores de duas variáveis sem usar uma variável temporária

b = None
temp = a = 10
print(temp, a)

a, b = b, a

print(f'O valor de a é: {a}')
print(f'O valor de b é: {b}')

b = a

print(f'O valor de a é: {a}')
print(f'O valor de b é: {b}\n')

# Acessando os elementos de uma tupla usando desempacotamento

cordenadas = (10, 20, 30, 40, 50)

x, y, z, a, b = cordenadas

print('''A cordenada x é: {}
A cordenada y é: {}
A cordenada z é: {}
A cordenada a é: {}
A cordenada b é: {}\n'''.format(x, y, z, a, b))

# Desempacotamento usando o operador asterisco (*) para separar

cordenadas2 = (10, 20, 30, 40, 50)

primeiro, *resto = cordenadas2

print('''O primeiro elemento é: {}
Os elementos restantes são: {}\n'''.format(primeiro, resto))

primeiro, *middle, ultimo = cordenadas2

print('''O primeiro elemento é: {}
Os elementos do meio são: {}
O último elemento é: {}\n'''.format(primeiro, middle, ultimo))

#Acessando dados e descartando informações usando o operador asterisco (*) e o caractere de sublinhado (_)

dados = (
    'João',
    30,
    'Engenheiro',
    'São Paulo',
    'Brasil\n'
)

nome, idade, pais,*_ = dados

print('''O nome é: {}
A idade é: {}
O país é: {}\n'''.format(nome, idade, pais))

_, _, profissao, cidade, pais = dados
print('''A profissão é: {}
A cidade é: {}
O país é: {}\n'''.format(profissao, cidade, pais))