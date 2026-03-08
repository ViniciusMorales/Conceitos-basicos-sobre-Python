numb = int(input("Digite um número: "))
print(f'"O número digitado foi: {numb} e te enviarei algumas coisas sobre ele, junto de sua tabuada de 1 a 10."')

if numb % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
    
if numb > 0:
    print("O número é positivo.")   
elif numb < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
    
for i in range(1, 11):
    print(f"{numb} x {i} = {numb * i}")