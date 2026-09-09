"""
Exercício 4: Análise de Metas Combinadas (Setor Comercial)

Uma empresa paga bônus se a meta individual do vendedor e a meta da loja
forem batidas.
1. Peça as vendas do vendedor e a meta individual dele.
2. Peça as vendas totais da loja e a meta da loja.
3. Se o vendedor bater a meta dele E a loja bater a meta total, o bônus
   é de 20% sobre as vendas do vendedor.
4. Caso contrário, o bônus é zero. Exiba a mensagem: "Seu bônus este mês
   é de: R$[valor]".
"""

vendas_vendedor = float(input("Vendas do vendedor: "))
meta_vendedor = float(input("Meta individual do vendedor: "))
vendas_loja = float(input("Vendas totais da loja: "))
meta_loja = float(input("Meta da loja: "))

if vendas_vendedor >= meta_vendedor and vendas_loja >= meta_loja:
    bonus = vendas_vendedor * 0.20
else:
    bonus = 0

print(f"Seu bônus este mês é de: R${bonus:.2f}")
