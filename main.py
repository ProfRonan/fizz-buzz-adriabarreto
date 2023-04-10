numero = input("Digite um número ")
numero = int(numero)

resto3 = int( numero % 3)
resto5 = int( numero % 5)

if resto3 == 0 and resto5 == 0:
    print("FizzBuzz")
elif resto3 == 0:
    print("Fizz")
elif resto5 == 0:
    print("Buzz")

else:
    print(numero)