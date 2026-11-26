caixa_empresa = 5000
caixa_familiar = 0
caixa_governo = 0
salario = 1000
imposto = 0.20 * salario
salario_comDesconto = salario - imposto
gasto_familiar = 0.80 * salario_comDesconto

for mes in [1, 2 ,3]:
    caixa_empresa = caixa_empresa - salario
    caixa_familiar = caixa_familiar + salario_comDesconto - gasto_familiar
    caixa_governo = caixa_governo + imposto
    caixa_empresa = caixa_empresa + gasto_familiar
    print(f"No mês {mes}: | Empresa: {caixa_empresa} | Família: {caixa_familiar} | Governo: {caixa_governo}")
