# ENTRADA
encontrar = False
saldo_total = 0
negativados = set()
clientes = [
    {"id": 1, "nome": "Ana Lima",    "cpf": "111.111.111-11", "saldo": 1500.00, "transacoes": []},
    {"id": 2, "nome": "Bruno Souza", "cpf": "222.222.222-22", "saldo": 320.00,  "transacoes": []},
    {"id": 3, "nome": "Carla Dias",  "cpf": "333.333.333-33", "saldo": 0.00,    "transacoes": []},
    {"id": 4, "nome": "Diego Melo",  "cpf": "444.444.444-44", "saldo": 875.50,  "transacoes": []},
]

transacoes = (
    (1, "deposito", 500.00),
    (2, "saque",    100.00),
    (3, "deposito", 200.00),
    (4, "saque",    900.00),
    (1, "saque",    300.00),
    (2, "deposito", 150.00),
)

# PROCESSAMENTO/SAÍDA
print("--- Clientes Cadastrados ---")

for cliente in clientes:
    print(f"{cliente['nome']} - CPF: {cliente['cpf']} - Saldo: R$ {cliente['saldo']}")

# processamento de deposito e saque
for id_cliente, tipo, valor in transacoes:
    for cliente in clientes:
        if id_cliente == cliente['id']:
            if tipo == 'deposito':
                cliente['saldo'] += valor
                cliente['transacoes'].append((tipo, valor))
            elif tipo == 'saque':
                cliente['saldo'] -= valor
                cliente['transacoes'].append((tipo, valor))
                if cliente['saldo'] < 0:
                    negativados.add(cliente['nome'])
print("\n--- Contas com Saldo Negativo ---")
for nome in negativados:
    print(f"- {nome}")

# saida de deposito e saque
for cliente in clientes:
    print(f"\n--- Extrato: {cliente['nome']} ---")
    for tipo, valor in cliente['transacoes']:
        print(f"{tipo}: R$ {valor:.2f}")
    print(f"Saldo final: R$ {cliente['saldo']:.2f}")

# estatisticas (não sei ver o maior saldo e nem o menor)
print('\n--- Estatísticas ---')
for cliente in clientes:
    saldo_total += cliente['saldo']
print(f"Saldo total: R$ {saldo_total}")
maior = clientes[0]
menor = clientes[0]
for cliente in clientes:
    if cliente['saldo'] > maior['saldo']:
        maior = cliente
    if cliente['saldo'] < menor['saldo']:
        menor = cliente
print(f"Maior saldo: {maior['nome']} — R$ {maior['saldo']:.2f}")
print(f"Menor saldo: {menor['nome']} — R$ {menor['saldo']:.2f}")
#   print(f"Maior saldo: {cliente['nome']}- R$ {cliente['saldo']}")

try:
    entrada = input('\nDigite o ID do cliente: ')
    if not entrada.strip():
        raise ValueError("ID não pode ser vazio.")
    id_digitado = int(entrada)

    encontrado = False
    for cliente in clientes:
        if cliente['id'] == id_digitado:
            print(f"{cliente['nome']} - Saldo: R$ {cliente['saldo']:.2f}")
            encontrado = True

    if not encontrado:
        print('Cliente não encontrado.')

except ValueError as e:
    print(f'Erro: {e}')
finally:
    print('--- Consulta Encerrada ---')