# Lista Extra 01 – Paradigmas de Programação com Python

Resolução completa da lista, com cada exercício em um arquivo `.py`
separado e comentado (enunciado incluso no topo de cada arquivo).

## Estrutura

```
Lista_Extra_01/
├── lista1_variaveis/
│   ├── exercicio1_bonus_vendas.py
│   ├── exercicio2_estoque_ecommerce.py
│   ├── exercicio3_divisao_cargas.py
│   ├── exercicio4_margem_lucro.py
│   └── exercicio5_conversao_tempo_contrato.py
│
├── lista2_strings/
│   ├── exercicio1_relatorio_margem_lucro.py
│   ├── exercicio2_padronizacao_crm.py
│   ├── exercicio3_migracao_servidor_email.py
│   ├── exercicio4_extracao_username.py
│   └── exercicio5_personalizacao_email_marketing.py
│
├── lista3_inputs/
│   ├── exercicio1_calculadora_imposto.py
│   ├── exercicio2_cadastro_colaborador.py
│   └── exercicio3_analise_metas_vendas.py
│
└── lista4_if/
    ├── exercicio1_validacao_investimento.py
    ├── exercicio2_controle_acesso.py
    ├── exercicio3_desconto_progressivo.py
    ├── exercicio4_metas_combinadas.py
    └── exercicio5_triagem_emails.py
```

## Como rodar

Os exercícios das Listas 1 e 2 rodam direto:

```bash
python lista1_variaveis/exercicio1_bonus_vendas.py
```

Os exercícios das Listas 3 e 4 pedem dados via `input()` no terminal —
basta rodar e digitar os valores pedidos.

## Conceitos usados

- **Aritmética:** `+`, `-`, `*`, `/`, `//` (divisão inteira), `%` (resto)
- **Strings:** `.strip()`, `.lower()`, `.upper()`, `.title()`, `.capitalize()`,
  `.replace()`, `.find()`, fatiamento (`texto[inicio:fim]`)
- **Formatação:** f-strings com `:,.2f` (milhar + decimais) e `:.0%` (porcentagem)
- **Input/Output:** `input()`, conversão com `float()`
- **Condicionais:** `if` / `elif` / `else`, operadores `and`/`or`, operador `in`
