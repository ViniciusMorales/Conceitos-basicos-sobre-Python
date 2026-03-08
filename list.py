list = [10, 77, 45, 20]

print(list)

#Adicionar um elemento ao final da lista
list.append(30)
print(list)

#Adicionar um elemento em uma posição específica
list.insert(1, 15)
print(list)

#Remover um elemento específico da lista
list.remove(20)
print(list)

#Remover o último elemento da lista
list.pop()
print(list)

#Ordenar a lista em ordem crescente
list.sort()
print(list)

#Ordenar a lista em ordem decrescente
list.sort(reverse=True)
print(list)

#Obter o índice de um elemento específico
index = list.index(45)
print(f"O índice de 45 é: {index}")

#Contar quantas vezes um elemento aparece na lista
count = list.count(77)
print(f"O número 77 aparece {count} vezes na lista.")


