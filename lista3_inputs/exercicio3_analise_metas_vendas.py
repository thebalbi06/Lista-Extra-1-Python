"""
Exercício 3: Análise de Metas de Vendas (Setor Comercial)

Um gerente quer comparar o desempenho de duas filiais. O programa deve:
1. Pedir o faturamento da Loja A e o faturamento da Loja B (o usuário
   pode digitar números decimais).
2. Calcular o faturamento total das duas lojas.
3. Calcular a média de faturamento entre elas.
4. Exibir uma única mensagem formatada informando o total e a média,
   utilizando o separador de milhar e duas casas decimais.
"""

faturamento_a = float(input("Faturamento da Loja A: "))
faturamento_b = float(input("Faturamento da Loja B: "))

total = faturamento_a + faturamento_b
media = total / 2

print(f"Faturamento total: R${total:,.2f} | Média: R${media:,.2f}")
