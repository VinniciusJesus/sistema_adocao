class Cao:
    def __init__(self, nome, idade, raca, disponivel=True):
        self.nome = nome
        self.idade = idade
        self.raca = raca
        self.disponivel = disponivel

    def informacoes(self):
        return f"{self.nome} - {self.idade} anos - Raça: {self.raca} - {'Disponível para adoção' if self.disponivel else 'Adotado'}"


class Gato:
    def __init__(self, nome, idade, cor, disponivel=True):
        self.nome = nome
        self.idade = idade
        self.cor = cor
        self.disponivel = disponivel

    def informacoes(self):
        return f"{self.nome} - {self.idade} anos - Cor: {self.cor} - {'Disponível para adoção' if self.disponivel else 'Adotado'}"


class Adocao:
    def __init__(self):
        self.cachorros = []
        self.gatos = []
        self.doacoes_dinheiro = 0
        self.doacoes_racao = 0

    def adicionar_animal(self, animal):
        if isinstance(animal, Cao):
            self.cachorros.append(animal)
        elif isinstance(animal, Gato):
            self.gatos.append(animal)

    def listar_animais(self):
        print("\nAnimais disponíveis para adoção:")
        for cachorro, gato in zip(self.cachorros, self.gatos):
            print(f"{cachorro.informacoes()}             |             {gato.informacoes()}")

    def adotar_animal(self, escolha):
        total_animais = len(self.cachorros)

        if 1 <= escolha <= total_animais:
            animal = self.cachorros[escolha - 1]
            if animal.disponivel:
                animal.disponivel = False
                print(f"{animal.nome} foi adotado com sucesso!")
            else:
                print(f"{animal.nome} já foi adotado anteriormente.")
        else:
            print("Escolha inválida. Por favor, escolha um número válido.")

    def fazer_doacao(self):
        print("\nEscolha o tipo de doação:")
        print("1. Dinheiro")
        print("2. Ração")
        tipo_doacao = input("Digite o número do tipo de doação que você deseja fazer: ")

        if tipo_doacao == "1":
            valor_doacao = float(input("Digite o valor da doação em dinheiro: R$ "))
            self.doacoes_dinheiro += valor_doacao
            print(f"Obrigado pela sua doação em dinheiro! Total arrecadado: R${self.doacoes_dinheiro}")

        elif tipo_doacao == "2":
            quantidade_racao = int(input("Digite a quantidade de ração a ser doada (em kg): "))
            self.doacoes_racao += quantidade_racao
            print(f"Obrigado pela sua doação de ração! Total arrecadado: {self.doacoes_racao} kg")

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

# Função para exibir a abertura com rostinhos de cachorro e gato
def exibir_abertura():
    print("\nBem-vindo ao Sistema de Adoção de Cachorros e Gatos!")
    print("\n")
    print("  / \\__            |\\_/|")
    print(" (    @\\____      ( o.o )")
    print(" /         O       > ^ <")
    print("/   (_____/")
    print("\n")

# Exemplo de uso
if __name__ == "__main__":
    # Inicializando o sistema de adoção
    adocao = Adocao()

    # Adicionando quatro cachorros e quatro gatos diferentes
    adocao.adicionar_animal(Cao(nome="Buddy", idade=3, raca="Labrador Retriever"))
    adocao.adicionar_animal(Cao(nome="Max", idade=2, raca="Golden Retriever"))
    adocao.adicionar_animal(Cao(nome="Daisy", idade=4, raca="Bulldog"))
    adocao.adicionar_animal(Cao(nome="Charlie", idade=2, raca="Beagle"))

    adocao.adicionar_animal(Gato(nome="Whiskers", idade=2, cor="Cinza"))
    adocao.adicionar_animal(Gato(nome="Mittens", idade=3, cor="Branco e Preto"))
    adocao.adicionar_animal(Gato(nome="Luna", idade=1, cor="Tricolor"))
    adocao.adicionar_animal(Gato(nome="Oliver", idade=4, cor="Amarelo"))

    # Exibindo a abertura com rostinhos de cachorro e gato
    exibir_abertura()

    # Menu principal
    while True:
        print("\nMenu:")
        print("1. Adotar um animal")
        print("2. Fazer uma doação")
        print("3. Sair")

        escolha_menu = input("Escolha uma opção (1/2/3): ")

        if escolha_menu == "1":
            # Listando animais disponíveis
            adocao.listar_animais()

            # Pedindo ao usuário para escolher um animal
            escolha_adocao = int(input("Escolha o número do animal que você deseja adotar: "))
            adocao.adotar_animal(escolha_adocao)

        elif escolha_menu == "2":
            adocao.fazer_doacao()

        elif escolha_menu == "3":
            print("Obrigado por visitar o Sistema de Adoção")
