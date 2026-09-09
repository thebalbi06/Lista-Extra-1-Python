"""
Exercício 1: Cálculo de Bônus de Vendas (RH/Vendas)

Uma empresa decidiu dar um bônus de 10% sobre o faturamento total para a
equipe de vendas. Calcule o valor do bônus e o faturamento final da empresa
após subtrair esse bônus.

- Faturamento inicial: 50.000
- Percentual de bônus: 0.10
"""

faturamento = 50000
percentual_bonus = 0.10

bonus = faturamento * percentual_bonus
faturamento_final = faturamento - bonus

print("Valor do bônus:", bonus)
print("Faturamento final:", faturamento_final)
