# Você é um programador que trabalha em uma loja virtual que vende produtos eletrônivos. A sua tarefa é criar um programa em Python que calcule o preço final de um produto após o acréscimo de impostos e descontos, e exibir na tela o valor final que será cobrado do cliente.

# preco = float(input('Digite o valor do produto: '))
# imposto = float(input('Digite o valor do imposto: '))
# desconto = float(input('Digite o valor do desconto: '))

# valor_imposto = imposto / 100 * preco
# valor_desconto = desconto / 100 * preco
# preco_final = preco + valor_imposto - valor_desconto

# print(f'O preço final do produto é R$ {preco_final}')


# ---------------------------------------------------------------------------------------------


# Você foi contratado para desenvolver um sistema de login para um aplicativo da web. Sua primeira tarefa é criar uma tela de login para autenticar os usuários. Para isso, você precisa escrever um programa em Pytho9n que solicita ao usuário um nome de usuário e uma senha. Em seguida, o programa verifica se o nome de usuário e a senha correpondem a um par de login válido. Se o login  for bem-sucedido, o programa deve exibir: acesso bem sucedido, caso contrário, deve-se exibir: usuário não cadastrado.

# usuario_cadastrado = 'ghost'
# senha_cadastrada = '123'

# usuario_digitado = input('Digite seu nome de usuário: ')
# senha_digitada = input('Digite sua senha: ')

# if usuario_digitado == usuario_cadastrado and senha_digitada == senha_cadastrada:
#   print (f'Bem vindo, {usuario_digitado}')
# else:
#   print('Usuário não cadastrado!')

# -------------------------------------------------------------------------------


# Um vendedor recebe uma comissão por suas vendas. Dependendo do valor da venda, a comissão varia. A comissão é calculada da seguinte forma:
# - 5% para vendas de até R$1.000,00
# - 7.5% para vendas entre R$1.000,01 e R$5.000,00
# - 10% para vendas entre R$5.000,01 e R$ 10.000,00
# - 15% para vendas acima de R$10.000,00
# Escreva um programa em Python que calcule a comissão do vendedor, dado o valor da venda e o nome do vendedor.

# nome_vendedor = input('Digite o nome do vendedor:')
# valor_venda = float(input('Digite o valor da venda: '))

# if valor_venda <= 1000:
#   taxa = 0.05
# elif valor_venda <= 5000:
#   taxa = 0.075
# elif valor_venda <= 10000:
#   taxa = 0.10
# else:
#   taxa = 0.15

# comissao = valor_venda * taxa

# print(f'{nome_vendedor} sua comissao é de R$ {comissao}')


# ---------------------------------------------------------------------------------------------

# Crie um programa em Python que classifique a nota de um aluno, seguindo a tabela abaixo:
# Menor que 3   - F
# Entre 3 e 5   - D
# Entre 5 e 8   - C
# Entre 8 e 9.9 - B
# Igual a 10    - A

# nota = float(input('Digite a sua nota: '))
# F = "F"
# D = "D"
# C = "C"
# B = "B"
# A = "A"

# if nota <= 3:
#   nota_final = F
# elif nota >= 3 and nota < 5:
#   nota_final = D
# elif nota > 5 and nota <= 8:
#   nota_final = C
# elif nota > 8 and nota <= 9.9:
#   nota_final = B
# else: nota_final = A

# print(f'Sua nota final é: {nota_final}')

# ----------------------------------------------------------------------

# senha_correta = '123'
# senha_digitada = ''

# while senha_correta != senha_digitada:
#   senha_digitada = input('Digite sua senha: ')
#   if senha_digitada != senha_correta:
#     print ('Senha incorreta, tente novamente!')

# print('Bem vindo ao sistema!')

# ------------------------------------------------------------------------

# Você precisa criar cinco novas listas a partir de uma lista originnal dde números inteiros.
# As novas listas devem ser as seguintes:
#   1 - Uma lista contendo apenas os números pares da lista original.
#   2 - Uma lista contendo apenas os números ímpares da lista original.
#   3 - Uma lista contendo apenas os múltiplos de 3 da lista original.
#   4 - Uma lista contendo apenas os múltiplos de 3 e 4 da lista original.
#   5 - Uma lista contendo apenas os múltiplos de 3 ou 4 da lista original.

# numeros = [1, 2, 31, 4, 12, 567, 80]

# pares = []
# impares = []
# multiplo_3 = []
# multiplo_3_e_4 = []
# multiplo_3_ou_4 = []

# for numero in numeros:
#   if numero % 2 == 0:
#     pares.append(numero)
#   else:
#     impares.append(numero)
#   if numero % 3 == 0:
#     multiplo_3.append(numero)
#   if numero % 3 == 0 and numero % 4 == 0:
#     multiplo_3_e_4.append(numero)
#   if numero % 3 == 0 or numero % 4 == 0:
#     multiplo_3_ou_4.append(numero)

# print(f'Números pares: {pares}')
# print(f'Números impares: {impares}')
# print(f'Números multiplos de 3: {multiplo_3}')
# print(f'Números multiplos de 3 e 4: {multiplo_3_e_4}')
# print(f'Números multiplos de 3 ou 4: {multiplo_3_ou_4}')