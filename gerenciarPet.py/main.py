from gerenciarPet import gato, cachorro
def criar_animal():
    nome = input("digite o nome do seu pet: ")
    idade = input("digite a idade do seu animal")
    especie = input("e um gato ou um cachorro?: ").lower()

    if especie == "gato":
        return gato(nome, idade)
    elif especie == "cachorro":
        return cachorro(nome, idade)
    else:
        print("tipo invalido. criando um tipo padrao")
        return cachorro(nome, idade)
  
def menu():
    print("\nOque vc quer fazer?")
    print("1 - brincar")
    print("2 - dormir")
    print("3 - comer")
    print("4 - ouvir som")
    print("5 - mostrar a energia")
    print("6 - sair")

def main():
    pet = criar_animal()
    while True:
        menu()
        escolha = input("escolha uma opcao:")
        if escolha == "1":
            horas = int(input("por quantas horas brincar:"))
            pet.brincar(horas)
        elif escolha == "2":
            horas = int(input("por quantas horas dormir: "))
            pet.dormir(horas)
        elif escolha == "3":
            comida = input("oque ele vai comer:")
            pet.comer(comida)
        elif escolha == "4":
            pet.fazerSom()
        elif  escolha == "5":
            print(f"energia e {pet.nome}|: {pet.energia}")
        elif escolha == "0":
            print("ate mais")
            break
        else:
            print("opcao invalida")

if __name__ == "__main__":
    main()