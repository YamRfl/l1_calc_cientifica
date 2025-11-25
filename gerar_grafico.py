import matplotlib.pyplot as plt

# Dados extraídos do seu SQL (simulação dos resultados das queries)
anos = [2016, 2017, 2018, 2019, 2020, 2021, 2022]
td_mulher = [11.9, 11.8, 11.7, 11.6, 12.5, 12.0, 11.7]
td_homem = [5.1, 5.2, 5.3, 5.4, 5.8, 5.7, 5.6]
# Dados de gerência (preenchendo os anos anteriores com tendência estimada para o exemplo)
gerencia_mulher = [35.5, 35.8, 36.0, 36.1, 36.5, 37.2, 37.8] 

plt.figure(figsize=(10, 6))

# Plotando as linhas
plt.plot(anos, td_mulher, marker='o', label='Trab. Doméstico - Mulher (h)', color='red')
plt.plot(anos, td_homem, marker='o', label='Trab. Doméstico - Homem (h)', color='blue')
plt.plot(anos, gerencia_mulher, marker='s', linestyle='--', label='% Mulheres em Gerência', color='green')

# Configurações do gráfico
plt.title('Evolução: Trabalho Doméstico vs. Cargos Gerenciais (Brasil)')
plt.xlabel('Ano')
plt.ylabel('Valor (Horas ou %)')
plt.legend()
plt.grid(True)

# Exibir ou Salvar
plt.savefig('grafico_ods5.png')
plt.show()