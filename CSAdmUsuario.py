class UsuariosSistema:
    usuarios = ["Pietryk", "Judy"]

    @classmethod
    def create(cls):
        novo_usuario = input("Digite o nome do novo usuário: ")
        cls.usuarios.append(novo_usuario)
        print(f"Usuário {novo_usuario} cadastrado com sucesso!")

    @classmethod
    def read(cls):
        print("Usuários cadastrados:")
        for i, usuario in enumerate(cls.usuarios, start=1):
            print(f"{i}. {usuario}")

    @classmethod
    def update(cls):
        cls.read()
        indice = int(input("Digite o número do usuário que deseja atualizar: ")) -1 
        if 0 <= indice < len(cls.usuarios):
            novo_nome = input(f"Digite o novo nome para {cls.usuarios[indice]}: ")
            cls.usuarios[indice] = novo_nome
            print(f"Usuario atualizado para {novo_nome} com sucesso!")
        else:
            print("Invalido")

    @classmethod
    def delete(cls):
        cls.read()
        indice = int(input("Digite o número do usuário que deseja excluir: ")) -1 
        if 0 <= indice < len(cls.usuarios):
            removido = cls.usuarios.pop(indice)
            print(f"Usuário {removido} excluído com sucesso!")
        else:
            print("Invalido.")

## -- fim Usuariosistema -- ##

def menu():
    opcao = 0
    while opcao != 5:
        print("\nEscolha uma opção:")
        print("1 - Cadastrar Usuário")
        print("2 - Ler Usuários")
        print("3 - Atualizar Usuário")
        print("4 - Deletar Usuário")
        print("5 - Sair")

        opcao = int(input("Digite o número da opção desejada: "))

        if opcao == 1:
            UsuariosSistema.create()
        elif opcao == 2:
            UsuariosSistema.read()
        elif opcao == 3:
            UsuariosSistema.update()
        elif opcao == 4:
            UsuariosSistema.delete()
        elif opcao == 5:
            print("Encerrando o sistema.")
        else:
            print("Opção inválida. Tente novamente.")

## -- inicio -- ##
menu()