from collections import Counter

palavras = ["Python", "Programação", "Desenvolvimento", "Tecnologia", "Inteligência Artificial"
            "Programação", "Analista", "Debugger", "Inteligência Artificial"]

print(f"Lista de palavras: {palavras}\n\n")

#Contando a frequência de palavras usando Counter
contagem = Counter(palavras)
print(f"Contagem de palavras: {contagem}\n\n")

# Obtendo as palavras mais comuns
contagemComuns = contagem.most_common(3)
print(f"Palavras mais comuns: {contagemComuns}\n\n")

#Contar carcteres em uma string curta ou frase

word = "Python"
char_count = Counter(word)
print(f"Contagem de caracteres em '{word}': {char_count}\n\n")

phrase = "Contar palavras em uma frase usando Counter"
char_count_phrase = Counter(phrase)
print(f"Contagem de caracteres em '{phrase}': {char_count_phrase}\n\n")

#Combinação entre contagens usando operadores aritméticos

a = Counter({'Python', 'Programação', 'Desenvolvimento'})
b = Counter({'Tecnologia', 'Inteligência Artificial', 'Programação'})

# União de contagens
uniao = a | b
print(f"União de contagens: {uniao}\n\n")

# Interseção de contagens
intersecao = a & b
print(f"Interseção de contagens: {intersecao}\n\n")

