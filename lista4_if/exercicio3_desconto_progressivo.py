"""
Exercício 3: Cálculo de Desconto Progressivo (Setor de Vendas)

Um e-commerce aplica descontos automáticos no carrinho. Crie um programa
que receba o valor total da compra e aplique a seguinte lógica:
- Compras a partir de R$ 500,00: 15% de desconto.
- Compras a partir de R$ 200,00 (e menos de 500): 10% de desconto.
- Compras abaixo de R$ 200,00: Sem desconto.
O programa deve exibir o valor do desconto e o valor final a pagar,
formatados em R$.
"""

valor_compra = float(input("Digite o valor total da compra: "))

if valor_compra >= 500:
    desconto = valor_compra * 0.15
elif valor_compra >= 200:
    desconto = valor_compra * 0.10
else:
    desconto = 0

valor_final = valor_compra - desconto

print(f"Desconto: R${desconto:.2f} | Valor final: R${valor_final:.2f}")
