while True:
    print("\nBem vindo a calculadora!")
    try:
        numb1 = float(input("Digite o primeiro número: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        break

    try:    
        print('''Operações disponíveis: +, -, *, /, %1, %2, ^, root
        atente-se que %1 é usando para trezer o resto da divisão
        enquanto %2 é usado para calcular porcentagem.''')
        operation = input("Digite a operação (+, -, *, /, %1, %2, ^, root): ").strip()
        if operation not in ["+", "-", "*", "/", "%1", "%2", "^", "root"]:
            raise ValueError("Operação inválida.")
            
    except ValueError:
        print("Por favor, digite uma operação válida.")
        break

    try:
        numb2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        break
    
    if operation == "+":
        result = numb1 + numb2
        print(f"O resultado de {numb1} + {numb2} é: {result}")
        continuar = str(input(("Quer fazer outra operação? (s/n)"))).lower().strip()
        if continuar != "s":
            print("Obrigado por usar a calculadora!")
            break
        
    elif operation == "-":
        result = numb1 - numb2
        print(f"O resultado de {numb1} - {numb2} é: {result}")
        continuar = str(input(("Quer fazer outra operação? (s/n)"))).lower().strip()
        if continuar != "s":
            print("Obrigado por usar a calculadora!")
            break
        
    elif operation == "*":
        result = numb1 * numb2
        print(f"O resultado de {numb1} * {numb2} é: {result}")
        continuar = str(input(("Quer fazer outra operação? (s/n)"))).lower().strip()
        if continuar != "s":
            print("Obrigado por usar a calculadora!")
            break
        
    elif operation == "/":
        if numb2 != 0:
            result = numb1 / numb2
            print(f"O resultado de {numb1} / {numb2} é: {result}")
            continuar = str(input(("Quer fazer outra operação? (s/n)"))).lower().strip()
            if continuar != "s":
                print("Obrigado por usar a calculadora!")
                break
        else:
            print("Erro: Divisão por zero não é permitida.")
            continuar = str(input(("Quer fazer outra operação? (s/n)"))).lower().strip()
            if continuar != "s":
                print("Obrigado por usar a calculadora!")
                break
            
    elif operation == "%1":
        if numb1 < numb2:
            print('''Erro: O primeiro número deve ser maior ou igual ao segundo número.
            Isso ocorre porque o operador de módulo (%) retorna o resto da divisão, 
            e se o primeiro número for menor que o segundo, o resultado será igual ao primeiro número, 
            o que pode não ser o comportamento esperado.''')
        elif numb2 != 0:
            result = numb1 % numb2
            print(f"O resto da divisão de {numb1} % {numb2} é: {result}")
            continuar = str(input(("Quer fazer outra operação? (s/n)"))).lower().strip()
            if continuar != "s":
                print("Obrigado por usar a calculadora!")
                break
            
        else:
            print("Erro: Divisão por zero não é permitida.")
            continuar = str(input(("Quer fazer outra operação? (s/n)"))).lower().strip()
            if continuar != "s":
                print("Obrigado por usar a calculadora!")
                break
    elif operation == "%2":
        result = (numb1 * numb2) / 100
        print(f"{numb2}% de {numb1} é: {result}")
        continuar = str(input(("Quer fazer outra operação? (s/n)"))).lower().strip()
        if continuar != "s":
            print("Obrigado por usar a calculadora!")
            break
               
    elif operation == "^":
        result = numb1 ** numb2
        print(f"O resultado de {numb1} ^ {numb2} é: {result}")
        continuar = str(input(("Quer fazer outra operação? (s/n)"))).lower().strip()
        if continuar != "s":
            print("Obrigado por usar a calculadora!")
            break
        
    elif operation == "root":
        if numb2 != 0:
            result = numb1 ** (1 / numb2)
            print(f"A raiz de índice {numb2} de {numb1} é: {result}")
            continuar = str(input(("Quer fazer outra operação? (s/n)"))).lower().strip()
            if continuar != "s":
                print("Obrigado por usar a calculadora!")
                break
        else:
            print("Erro: Índice da raiz não pode ser zero.")
            continuar = str(input(("Quer fazer outra operação? (s/n)"))).lower().strip()
            if continuar != "s":
                print("Obrigado por usar a calculadora!")
                break
            
    else:
        print("Operação inválida. Por favor, escolha uma operação válida.")
        continuar = str(input(("Quer fazer outra operação? (s/n)"))).lower().strip()
        if continuar != "s":
            print("Obrigado por usar a calculadora!")
            break