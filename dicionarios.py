pessoa ={
    'nome': 'João',
    'idade': 30,
    'profissão': 'Engenheiro',
    'cidade': 'São Paulo',
}
print(f"Dados da pessoa: {pessoa}\n\n")

#Acessando os valores do dicionário usando as chaves

nome = pessoa['nome']
print(f"Nome: {nome}")

idade = pessoa['idade']
print(f"Idade: {idade}")

profissao = pessoa['profissão']
print(f"Profissão: {profissao}")

cidade = pessoa['cidade']
print(f"Cidade: {cidade}\n\n")

#Adicionando novos pares chave-valor ao dicionário

pessoa['país'] = 'Brasil'
print(f"Dicionário atualizado: {pessoa}\n\n")

#Modificando os valores existentes no dicionário
pessoa['idade'] = 31
pessoa['cidade'] = 'Rio de Janeiro'
print(f"Dicionário atualizado: {pessoa}\n\n")

#Removendo pares chave-valor do dicionário usando del
del pessoa['profissão']
print(f"Dicionário atualizado: {pessoa}\n\n")

#Adicionado informações usando o método de outros métodos de dicionário
pessoa.update({'profissão': 'Analista de Dados'})
print(f"Dicionário atualizado: {pessoa}\n\n")

salario = {
    'liquido': 5000,
    'bruto': 7000,
    'impostos': 2000,
}

pessoa.update(salario)
print(f"Dicionário atualizado: {pessoa}\n\n")

pessoa |= salario
print(f"Dicionário atualizado: {pessoa}\n\n")

# Dicionários matemáticos usando operadores aritméticos

operadores = {
    'soma': lambda x, y: x + y,
    'subtração': lambda x, y: x - y,
    'multiplicação': lambda x, y: x * y,
    'divisão': lambda x, y: x / y if y != 0 else 'Divisão por zero não é permitida'
}
# O lambda cria uma função, só que a função é anônima, ou seja, não tem nome
# Ela é útil para criar funções simples e rápidas, sem a necessidade de definir uma função completa usando def. 
# OS requisitos são passados em vírgulas, seguidos por : (dois pontos) que antecedem a operação ou retorno da função.

x = float(input('Digite o primeiro número: '))
y = float(input('Digite o segundo número: '))

print(f"Soma: {operadores['soma'](x, y)}")
print(f"Subtração: {operadores['subtração'](x, y)}")
print(f"Multiplicação: {operadores['multiplicação'](x, y)}")
print(f"Divisão: {operadores['divisão'](x, y)}\n\n") 