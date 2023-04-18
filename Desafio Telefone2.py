# Lendo dados dos clientes
quantidade_clientes = int(input("Informe a quantidade de clientes: "))
nomes = []
telefones = []
tipos = []
minutos = []
for i in range(quantidade_clientes):
    print(f"Dados do {i+1}o. cliente:")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    tipo = int(input("Tipo (0, 1 ou 2): "))
    minuto = int(input("Minutos: "))
    nomes.append(nome)
    telefones.append(telefone)
    tipos.append(tipo)
    minutos.append(minuto)

# Lendo dados das assinaturas
precobasico = [[25.5, 0.10], [35.0, 0.12], [60.0, 0.15]]
for i in range(3):
    print(f"Tipo {i}:")
    precobasicotipo = float(input("Preço básico: "))
    precominutotipo = float(input("Preço do minuto excedente: "))
    precobasico[i][0] = precobasicotipo
    precobasico[i][1] = precominutotipo

# Calculando as contas e mostrando o relatório
print("RELATÓRIO DE CLIENTES:")
for i in range(quantidade_clientes):
    nome = nomes[i]
    telefone = telefones[i]
    tipo = tipos[i]
    minuto = minutos[i]
    if minuto <= 90:
        valor_conta = precobasico[tipo][0]
    else:
        valor_conta = precobasico[tipo][0] + (minuto - 90) * precobasico[tipo][1]
    print(f"{nome}, {telefone}, Tipo {tipo}, Minutos: {minuto}, Conta = R$ {valor_conta:.2f}")
