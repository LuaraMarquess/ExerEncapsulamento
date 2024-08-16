
cafe_da_manha = ["pão com manteiga", "cereal com leite", "fruta fresca"]
almoco = ["arroz e feijão", "massa com molho", "frango grelhado", "salada de legumes"]
jantar = ["sopa de legumes", "omelete", "sanduíche", "wrap de frango"]

def obter_alergias():
    resposta = input("Você tem alguma alergia ou intolerância?   S/N")
    if resposta == "S":
       alergias = []
    else:
        input("Sem alergia!")
    
def verificar_alergias(alergias, alimento):
    for alergia in alergias:
        if alergia in alimento:
            return False
    return True
def gerar_cardapio(alergias):
    import random
    
    cafe_sugerido = random.choice(cafe_da_manha)
    almoco_sugerido = random.choice(almoco)
    jantar_sugerido = random.choice(jantar)
    
    print("\nSugestão de Cardápio:")
    
    if verificar_alergias(alergias, cafe_sugerido):
        print(f"Café da Manhã: {cafe_sugerido}")
    else:
        print(f"Café da Manhã: [Opcão com alérgico detectado: {cafe_sugerido}]")
    
    if verificar_alergias(alergias, almoco_sugerido):
        print(f"Almoço: {almoco_sugerido}")
    else:
        print(f"Almoço: [Opcão com alérgico detectado: {almoco_sugerido}]")
    
    if verificar_alergias(alergias, jantar_sugerido):
        print(f"Jantar: {jantar_sugerido}")
    else:
        print(f"Jantar: [Opcão com alérgico detectado: {jantar_sugerido}]")

# Main
def main():
    print("Bem-vindo ao gerador de cardápio!")
    alergias = obter_alergias()
    gerar_cardapio(alergias)

if __name__ == "__main__":
    main()













