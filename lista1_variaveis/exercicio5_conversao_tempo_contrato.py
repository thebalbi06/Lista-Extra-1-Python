"""
Exercício 5: Conversão de Tempo de Contrato (Gestão de Projetos)

Um contrato de manutenção de software tem a duração de 40 meses. O cliente
quer ver esse tempo no formato: "X anos e Y meses". Utilize os operadores
de divisão inteira e resto da divisão para converter os 40 meses.
"""

total_meses = 40

anos = total_meses // 12
meses_restantes = total_meses % 12

print(f"{total_meses} meses equivalem a {anos} anos e {meses_restantes} meses")
