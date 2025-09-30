# Escreva um programa em Python que solicite ao usuário que digite seu nome, 
# o valor do seu salário mensal e o valor dos bônus que recebeu. 
# O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e 
# informando o valor do salário em comparação com o bônus recebido.


# 1 - O programa deve começar solicitando ao usuário que insira seu nome.
nome = input("Por favor, digite seu nome: ")

# 2 - Em seguida, o programa deve pedir ao usuário para inserir o valor do seu salário. 
# Considere que este valor pode ser um número decimal.
salario = float(input("Por favor, digite o seu salário: "))

# 3 - Depois, o programa deve solicitar uma porcentagem do bônus recebido pelo usuário, 
# que também pode ser um número decimal.
bonus = float(input("Por favor, digite o valor do bônus: "))

# 4 - O cálculo do KPI dos bônus de 2024 é de1000 + salario * bônus
kpi = 1000 + ( salario * bonus)

# 5 - Finalmente, o programa deverá imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
print(f"Olá {nome}, o seu valor de bônus foi de {kpi}.")

# 6 - Salve esse script python como kpi.py
# 7 - Faça uma documentação simples de como executar esse programa, utilize o README
# 8 - Salve no Git e no Github