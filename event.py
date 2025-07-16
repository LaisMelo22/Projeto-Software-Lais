from datetime import datetime
from collections import defaultdict

# Lista principal de eventos
eventos = []

# 1. Criar evento
def criar_evento(nome, local, data_str):
    data_hora = datetime.strptime(data_str, "%d/%m/%Y %H:%M")
    evento = {
        "nome": nome,
        "local": local,
        "data_hora": data_hora,
        "participantes": [],  # lista de dicionários
        "fornecedores": set(),  # conjunto para evitar duplicatas
        "ativo": True
    }
    eventos.append(evento)
    print(f"Evento '{nome}' criado com sucesso.")

# 2. Adicionar participante
def adicionar_participante(nome_evento, nome_participante, contato):
    for evento in eventos:
        if evento["nome"] == nome_evento and evento["ativo"]:
            ingresso = f"{nome_evento[:3].upper()}-{len(evento['participantes'])+1}"
            participante = {"nome": nome_participante, "contato": contato, "ingresso": ingresso}
            evento["participantes"].append(participante)
            print(f"Participante '{nome_participante}' adicionado com ingresso {ingresso}.")
            return
    print("Evento não encontrado ou inativo.")

# 3. Adicionar fornecedor
def adicionar_fornecedor(nome_evento, nome_fornecedor, servico, contato):
    for evento in eventos:
        if evento["nome"] == nome_evento and evento["ativo"]:
            fornecedor = (nome_fornecedor, servico, contato)
            evento["fornecedores"].add(fornecedor)
            print(f"Fornecedor '{nome_fornecedor}' adicionado.")
            return
    print("Evento não encontrado ou inativo.")

# 4. Listar eventos
def listar_eventos():
    for evento in eventos:
        status = "Ativo" if evento["ativo"] else "Cancelado"
        print(f"{evento['nome']} - {evento['local']} - {evento['data_hora']} ({status})")

# 5. Gerar ingressos (já é feito ao adicionar participantes)

# 6. Agendar evento (já ocorre ao criar com data/hora)

# 7. Ver participantes de um evento
def listar_participantes(nome_evento):
    for evento in eventos:
        if evento["nome"] == nome_evento:
            print(f"Participantes do evento '{nome_evento}':")
            for p in evento["participantes"]:
                print(f"- {p['nome']} (ingresso: {p['ingresso']})")
            return
    print("Evento não encontrado.")

# 8. Ver fornecedores de um evento
def listar_fornecedores(nome_evento):
    for evento in eventos:
        if evento["nome"] == nome_evento:
            print(f"Fornecedores do evento '{nome_evento}':")
            for f in evento["fornecedores"]:
                print(f"- {f[0]} ({f[1]}) - Contato: {f[2]}")
            return
    print("Evento não encontrado.")

# 9. Cancelar evento
def cancelar_evento(nome_evento):
    for evento in eventos:
        if evento["nome"] == nome_evento:
            evento["ativo"] = False
            print(f"Evento '{nome_evento}' cancelado.")
            return
    print("Evento não encontrado.")

# 10. Coordenar fornecedores
def coordenar_fornecedores(nome_evento):
    for evento in eventos:
        if evento["nome"] == nome_evento:
            print(f"Coordenando fornecedores de '{nome_evento}':")
            for f in evento["fornecedores"]:
                print(f"- Enviar instruções para {f[0]} ({f[1]}) via {f[2]}")
            return
    print("Evento não encontrado.")