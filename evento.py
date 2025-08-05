import random

class Participante:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.ingresso = self.gerar_ingresso()

    def gerar_ingresso(self):
        return f"ING{random.randint(1000, 9999)}"

class Fornecedor:
    def __init__(self, nome, servico):
        self.nome = nome
        self.servico = servico

class Evento:
    def __init__(self, nome, data):
        self.nome = nome
        self.data = data
        self.participantes = {}
        self.fornecedores = []

    def adicionar_participante(self, participante):
        self.participantes[participante.ingresso] = participante

    def adicionar_fornecedor(self, fornecedor):
        self.fornecedores.append(fornecedor)

class SistemaEventos:
    def __init__(self):
        self.eventos = {}

    def selecionar_evento(self):
        if not self.eventos:
            print("Nenhum evento cadastrado.")
            return None

        eventos_list = list(self.eventos.items())
        print("\nEventos disponíveis:")
        for idx, (nome, evento) in enumerate(eventos_list):
            print(f"{idx} - {nome} (Data: {evento.data})")

        try:
            escolha = int(input("Digite o número do evento desejado: "))
            if 0 <= escolha < len(eventos_list):
                return eventos_list[escolha][0]
            else:
                print("Índice inválido.")
                return None
        except ValueError:
            print("Entrada inválida.")
            return None

    def criar_evento(self):
        nome = input("Nome do evento: ")
        if nome in self.eventos:
            print("Evento já existe.")
            return
        data = input("Data do evento (ex: 10/12/2025): ")
        self.eventos[nome] = Evento(nome, data)
        print(f"Evento '{nome}' criado com sucesso.")

    def cancelar_evento(self):
        nome_evento = self.selecionar_evento()
        if nome_evento:
            del self.eventos[nome_evento]
            print(f"Evento '{nome_evento}' cancelado com sucesso.")

    def adicionar_participante(self):
        nome_evento = self.selecionar_evento()
        if not nome_evento:
            return
        evento = self.eventos[nome_evento]
        nome = input("Nome do participante: ")
        email = input("Email: ")
        participante = Participante(nome, email)
        evento.adicionar_participante(participante)
        print(f"Participante '{nome}' adicionado com ingresso {participante.ingresso}.")

    def adicionar_fornecedor(self):
        nome_evento = self.selecionar_evento()
        if not nome_evento:
            return
        evento = self.eventos[nome_evento]
        nome = input("Nome do fornecedor: ")
        servico = input("Serviço fornecido: ")
        fornecedor = Fornecedor(nome, servico)
        evento.adicionar_fornecedor(fornecedor)
        print(f"Fornecedor '{nome}' adicionado ao evento '{nome_evento}'.")

    def listar_eventos(self):
        if not self.eventos:
            print("Nenhum evento cadastrado.")
            return
        for evento in self.eventos.values():
            print(f"\nEvento: {evento.nome} - Data: {evento.data}")
            print(f"Participantes: {len(evento.participantes)}")
            print(f"Fornecedores: {len(evento.fornecedores)}")

    def listar_participantes(self):
        nome_evento = self.selecionar_evento()
        if not nome_evento:
            return
        evento = self.eventos[nome_evento]
        if not evento.participantes:
            print("Nenhum participante cadastrado.")
            return
        print(f"\nParticipantes do evento '{evento.nome}':")
        for ingresso, p in evento.participantes.items():
            print(f"- {p.nome} ({p.email}) | Ingresso: {ingresso}")

    def listar_fornecedores(self):
        nome_evento = self.selecionar_evento()
        if not nome_evento:
            return
        evento = self.eventos[nome_evento]
        if not evento.fornecedores:
            print("Nenhum fornecedor cadastrado.")
            return
        print(f"\nFornecedores do evento '{evento.nome}':")
        for f in evento.fornecedores:
            print(f"- {f.nome} (serviço: {f.servico})")

    def excluir_participante(self):
        nome_evento = self.selecionar_evento()
        if not nome_evento:
            return
        evento = self.eventos[nome_evento]

        if not evento.participantes:
            print("Nenhum participante cadastrado neste evento.")
            return

        participantes_list = list(evento.participantes.items())
        print(f"\nParticipantes do evento '{evento.nome}':")
        for idx, (ingresso, p) in enumerate(participantes_list):
            print(f"{idx} - {p.nome} ({p.email}) | Ingresso: {ingresso}")

        try:
            escolha = int(input("Digite o número do participante que deseja excluir: "))
            if 0 <= escolha < len(participantes_list):
                ingresso = participantes_list[escolha][0]
                del evento.participantes[ingresso]
                print("Participante removido com sucesso.")
            else:
                print("Índice inválido.")
        except ValueError:
            print("Entrada inválida.")

    def menu(self):
        while True:
            print("\n====== MENU DE EVENTOS ======")
            print("1. Criar evento")
            print("2. Cancelar evento")
            print("3. Adicionar participante")
            print("4. Adicionar fornecedor")
            print("5. Listar eventos")
            print("6. Listar participantes de um evento")
            print("7. Listar fornecedores de um evento")
            print("8. Excluir participante de um evento")
            print("0. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                self.criar_evento()
            elif escolha == '2':
                self.cancelar_evento()
            elif escolha == '3':
                self.adicionar_participante()
            elif escolha == '4':
                self.adicionar_fornecedor()
            elif escolha == '5':
                self.listar_eventos()
            elif escolha == '6':
                self.listar_participantes()
            elif escolha == '7':
                self.listar_fornecedores()
            elif escolha == '8':
                self.excluir_participante()
            elif escolha == '0':
                print("Encerrando o sistema.")
                break
            else:
                print("Opção inválida. Tente novamente.")

# Execução
if __name__ == "__main__":
    sistema = SistemaEventos()
    sistema.menu()
