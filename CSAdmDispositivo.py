class DispositivosSistema:
    dispositivos = [
        {"nome": "Painel Solar A", "energia": 150.5},
        {"nome": "Turbina Eólica B", "energia": 320.0}
    ]

    @classmethod
    def create(cls):
        nome = input("Nome do dispositivo de geração: ")
        try:
            energia = float(input("Energia gerada atual (em kWh): "))
        except ValueError:
            print("Valor de energia inválido! Definido como 0.0")
            energia = 0.0
            
        novo_dispositivo = {"nome": nome, "energia": energia}
        cls.dispositivos.append(novo_dispositivo)
        print(f"Dispositivo '{nome}' cadastrado com sucesso!")

    @classmethod
    def read(cls):
        if not cls.dispositivos:
            print("Nenhum dispositivo cadastrado.")
            return
        
        print("\nDispositivos cadastrados:")
        for i, disp in enumerate(cls.dispositivos, start=1):
            print(f"{i}. {disp['nome']} - Geração: {disp['energia']} kWh")

    @classmethod
    def update(cls):
        cls.read()
        if not cls.dispositivos:
            return
            
        try:
            indice = int(input("Digite o número do dispositivo que deseja atualizar: ")) - 1
            if 0 <= indice < len(cls.dispositivos):
                novo_nome = input(f"Digite o novo nome para {cls.dispositivos[indice]['nome']} : ")
                nova_energia_str = input(f"Digite a nova geração em kWh para {cls.dispositivos[indice]['nome']}  : ")
                
                if novo_nome:
                    cls.dispositivos[indice]['nome'] = novo_nome
                if nova_energia_str:
                    cls.dispositivos[indice]['energia'] = float(nova_energia_str)
                    
                print("Dispositivo atualizado com sucesso!")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida. Operação cancelada.")

    @classmethod
    def delete(cls):
        cls.read()
        if not cls.dispositivos:
            return
            
        try:
            indice = int(input("Digite o número do dispositivo que deseja excluir: ")) - 1 
            if 0 <= indice < len(cls.dispositivos):
                removido = cls.dispositivos.pop(indice)
                print(f"Dispositivo '{removido['nome']}' excluído com sucesso!")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida.")

    @classmethod
    def total_energia(cls):
        if not cls.dispositivos:
            print("Nenhum dispositivo cadastrado para somar.")
            return
        
        total = sum(disp['energia'] for disp in cls.dispositivos)
        print(f" Geração do mês: {total:.2f} kWh")


def menu():
    opcao = 0
    while opcao != 6:
        print("\n=== SISTEMA DE GERAÇÃO DE ENERGIA ===")
        print("1 - Cadastrar Dispositivo")
        print("2 - Listar Dispositivos")
        print("3 - Atualizar Dispositivo")
        print("4 - Deletar Dispositivo")
        print("5 - Total de Energia do Mês (Soma)")
        print("6 - Sair")

        try:
            opcao = int(input("Digite o número da opção desejada: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        if opcao == 1:
            DispositivosSistema.create()
        elif opcao == 2:
            DispositivosSistema.read()
        elif opcao == 3:
            DispositivosSistema.update()
        elif opcao == 4:
            DispositivosSistema.delete()
        elif opcao == 5:
            DispositivosSistema.total_energia()
        elif opcao == 6:
            print("Encerrando o sistema.")
        else:
            print("Opção inválida. Tente novamente.")

menu()