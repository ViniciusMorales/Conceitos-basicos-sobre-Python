people = input("Digite o nome de uma pessoa: ")

try:
    age = int(input("Digite a idade dessa pessoa: "))
    try:
        if age < 0:
            raise ValueError("A idade não pode ser negativa.")
        print(f"{people} tem {age} anos.")
    except ValueError as e:
        print(f"Erro: {e}")
except ValueError:
    print("Por favor, digite um número válido para a idade.")