import os
restaurantes = [{"nome":"Axerito", "categoria":"comida brasileira", "status":False},
                {"nome":"Tacacaria", "categoria":"comida regional", "status":True}
                ]

def exibir_nome_programa():
    print("""
      𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤
      """)
def menu():
    print("|1| - Cadastrar restaurante\n|2| - Listar restaurante\n|3| - Alterar status\n|4| - Finalizar")
def finalizar_app():
    os.system("cls")
    #os.system("clear")
    print("""
          𝔽𝕚𝕟𝕒𝕝𝕚𝕫𝕒𝕟𝕕𝕠 𝔸𝕡𝕡
          """)
def opcao_invalida():
    os.system("cls")
    print("Escolha uma opção válida:\n")
    voltar_ao_menu_principal()
def voltar_ao_menu_principal():
    input("Aperte em 'enter' para voltar ao menu principal ") #pensar em outra alternativa
    os.system("cls")
    main()
def cadastrar_restaurante():
    os.system("cls")
    print("""
          ℂ𝕒𝕕𝕒𝕤𝕥𝕣𝕠 𝕕𝕖 𝕣𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕖𝕤
          """)
    
    nome_restaurante = input("Digite o nome do restaurante: ")
    categoria = input("Digite a categoria do restaurante: ")

    dados_restaurante = {"nome":nome_restaurante, "categoria":categoria, "status":False}

    restaurantes.append(dados_restaurante)
    
    print(f"\n{nome_restaurante} foi cadastrado com sucesso!")
    
    voltar_ao_menu_principal()
def listar_restaurantes():
    os.system("cls")
    print("""
          ℝ𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕖𝕤 ℂ𝕒𝕕𝕒𝕤𝕥𝕣𝕒𝕕𝕠𝕤
          """)
    
    print(f"{"Nome Restaurante".ljust(18)} | {"Categoria".ljust(18)} | {"Status"}\n")
    
    for restaurante in restaurantes:

        nomeRestaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        status = "ativado" if restaurante["status"] else "desativado"

        print(f"{nomeRestaurante.ljust(18)} | {categoria.ljust(18)} | {status}")
    
    voltar_ao_menu_principal()
def alterar_status():
    print("""
          𝔸𝕥𝕚𝕧𝕒𝕣 𝕠𝕦 𝔻𝕖𝕤𝕒𝕥𝕚𝕧𝕒𝕣 𝕣𝕖𝕤𝕥𝕒𝕦𝕣𝕒𝕟𝕥𝕖𝕤
          """)

    nome_restaurante = input("Digite o nome do restaurante: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["status"] = not restaurante["status"]
            msg = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante["status"] else f"O restaurante {nome_restaurante} foi desativado"
            print(msg)
    if not restaurante_encontrado:
        print(f"Restaurante {nome_restaurante} não foi encontrado")

    voltar_ao_menu_principal()
def opcao_menu():
    try:
        opcao_menu = int(input("\n\nEscolha uma opção: ").strip())

        if opcao_menu == 1:
            cadastrar_restaurante()
        elif opcao_menu == 2:
            listar_restaurantes()
        elif opcao_menu == 3:
            alterar_status()
        elif opcao_menu == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    exibir_nome_programa()
    menu()
    opcao_menu()

if __name__ == "__main__":
    main()
