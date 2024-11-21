# lados1 = float(input("digite o primeiro lado"))
# lados2 = float(input("digite o segundo lado"))
# lados3 = float(input("digite o terceiro lado"))

# if lados1 == lados2 == lados3:
#     print("triangulo equilatero")
# elif lados1 == lados2 or lados1 == lados3 or lados2 == lados3:
#     print("triangulo isosceles") 
# else:
#     print("triangulo escaleno")


# idade = int(input("digite sua idade: "))

# if idade <= 13:
#     print("crianca")
# elif idade <= 17:
#     print("adolescente")
#     elif idade <= 60:
#     print("adulto")
# else:
#     print("invalida")  

# peso = float(input("digite seu peso"))
# altura = float(input("digite sua altura"))

# imc = peso / (altura ** 2)
# if imc >= 15 or imc <= 19.4:
#     print("abaixo do peso")
# elif imc >=19.5 or imc <= 24.9:
#     print("peso normal")
# elif imc >= 25 or imc <= 29.9:
#     print("acima do peso")
# elif imc >= 30 or imc <39.9:
#     print("obesidade grau 1")
# else:
#     print("obesidade grau 2")



nota1 = float(input("digite sua nota"))
nota2 = float(input("digite sua nota"))
nota3 = float(input("digite sua nota"))
nota4 = float(input("digite sua nota"))
media = (nota1 + nota2 + nota3 + nota4) / 4

if media < 3:
    print("reprovado")
elif media >=6:
    print("aprovado")
else:
    print("exame final")    