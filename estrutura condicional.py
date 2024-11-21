# idade = int(input("digite sua idade: "))

# if idade >= 18:
#     print("voce e maior de idade")
# else:
#     print("voce e menor de idade")

# notas = int(input("digite sua nota: "))

# if notas >= 7:
#     print("vc passou")
# elif notas >= 6:
#     print("vc esta de recuperacao")
# else:
#     print("exame direto")


idade = int(input("digite sua idade: "))
temCNH = True

if idade >=18 and temCNH:
    print("pode dirigir")
else:
    print("nao pode dirigir")