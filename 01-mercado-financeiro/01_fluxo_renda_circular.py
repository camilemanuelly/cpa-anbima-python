ALIQUOTA_IMPOSTO = 0.20
PROPENSAO_CONSUMO = 0.80
caixa_empresa = 5000
caixa_familiar = 0
caixa_governo = 0
salario_bruto = 1000
gasto_publico = 300
imposto_renda = ALIQUOTA_IMPOSTO * salario_bruto
salario_liquido = salario_bruto - imposto_renda
consumo_familiar = PROPENSAO_CONSUMO * salario_liquido

for mes in [1, 2 ,3]:
    caixa_empresa = caixa_empresa - salario_bruto
    caixa_familiar = caixa_familiar + salario_liquido - consumo_familiar
    caixa_governo = caixa_governo + imposto_renda - gasto_publico
    caixa_empresa = caixa_empresa + consumo_familiar + gasto_publico
    print(f"No mês {mes}: | Empresa: {caixa_empresa} | Família: {caixa_familiar} | Governo: {caixa_governo}")
