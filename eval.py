# o Eval analisa a expressão passada como string e a executa como código Python. Ele pode ser usado para avaliar 
# expressões matemáticas, executando sem precisar de try e except ValueError, ou até mesmo criar funções em tempo de execução. 


expressao = input('Digite uma expressão matemática: ')

result = eval(expressao)
print(f'O resultado da expressão "{expressao}" é: {result}')