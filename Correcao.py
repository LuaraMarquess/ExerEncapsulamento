print("Vamos montar um cardápio personalizado? ")
cafe_da_manha= []
almoco = []
jantar = []


print("Café da Manhã")
print("-------------")
for x in range(0,3):
    opcao = input(f"Digite a {x +1} opção:  ")
    cafe_da_manha.append(opcao) #Adicionando elemento na lista
    if opcao == "leite" or opcao == "queijo" or opcao == "pão":
        print("Alimento não recomendado!")
        print("Eis, as opções escolhidas: ",cafe_da_manha)
        

print("Almoço")
print("-------")
for x in range(0,4):
    opcao = input(f"Digite a opção {x+1}: ")
    almoco.append(opcao)
    if opcao == "camarao" or opcao=="pimenta":
        print("Alimento não recomendado!")
        print("Eis, as opções escolhidas: ",almoco)

print("Janta:")
print("-------")
for x in range(0,4):
    opcao = input(f"Digite a opção {x+1}: ")
    almoco.append(opcao)
    if opcao == "camarao" or opcao=="pimenta":
        print("Alimento não recomendado!")
        print("Eis, as opções escolhidas: ",jantar)

    print("Cardapio montaod: Cafe da Manha")
    print(cafe_da_manha[x])
