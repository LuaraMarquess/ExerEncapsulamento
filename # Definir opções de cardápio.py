# Definindo opções de cardápio
cafe_da_manha = ["pão com manteiga", "cereal com leite", "fruta fresca"]
almoco = ["arroz e feijão", "massa com molho", "frango grelhado", "salada de legumes"]
jantar = ["sopa de legumes", "omelete", "sanduíche", "wrap de frango"]

# Função para obter alergias/intolerâncias do usuário
def obter_alergias():
    alergias = input("Você tem alguma alergia ou intolerância? (separe por vírgula, ou digite 'nenhuma'): ")
    if alergias  == 'nenhuma':
        return []
    return [alergia.strip().lower() for alergia in alergias.split(',')]

# Função para verificar se um alimento contém alguma das alergias/intolerâncias
def verificar_alergias(alergias, alimento):
    for alergia in alergias:
        if alergia in alimento:
            return False
    return True

# Função para mostrar opções e obter escolha do usuário
def escolher_opcao(opcoes, refeicao):
    print(f"\nEscolha uma opção para {refeicao}:")
    for i, opcao in enumerate(opcoes, 1):
        print(f"{i}. {opcao}")
    
    escolha = int(input(f"Digite o número da sua escolha para {refeicao}: ")) - 1
    
    while escolha < 0 or escolha >= len(opcoes):
        print("Escolha inválida. Tente novamente.")
        escolha = int(input(f"Digite o número da sua escolha para {refeicao}: ")) - 1

    return opcoes[escolha]

# Função para gerar e analisar o cardápio com base na escolha do usuário
def gerar_cardapio(alergias):
    cafe_escolhido = escolher_opcao(cafe_da_manha, "café da manhã")
    almoco_escolhido = escolher_opcao(almoco, "almoço")
    jantar_escolhido = escolher_opcao(jantar, "jantar")
    
    print("\nSugestão de Cardápio:")
    
    if verificar_alergias(alergias, cafe_escolhido):
        print(f"Café da Manhã: {cafe_escolhido}")
    else:
        print(f"Café da Manhã: [Opção com alergênico detectado: {cafe_escolhido}]")
    
    if verificar_alergias(alergias, almoco_escolhido):
        print(f"Almoço: {almoco_escolhido}")
    else:
        print(f"Almoço: [Opção com alergênico detectado: {almoco_escolhido}]")
    
    if verificar_alergias(alergias, jantar_escolhido):
        print(f"Jantar: {jantar_escolhido}")
    else:
        print(f"Jantar: [Opção com alergênico detectado: {jantar_escolhido}]")

# Função principal
def main():
    print("Bem-vindo ao gerador de cardápio!")
    alergias = obter_alergias()
    gerar_cardapio(alergias)

if __name__ == "__main__":
    main()
