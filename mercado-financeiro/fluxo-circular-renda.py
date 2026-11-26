caixaInicial_empresa = 5000
caixaInicial_familiar = 0
caixaInicial_governo = 0
salario_semDesconto = 1000
imposto = 0.20 * salario_semDesconto
salario_comDesconto = salario_semDesconto - imposto
gasto_familiar = 0.80 * salario_comDesconto
poupanca_familia = 0.20 * salario_comDesconto
gasto_publico = 300


# Após pagamento do salário.
caixa_empresa = caixaInicial_empresa - salario_semDesconto
caixa_familiar = salario_semDesconto - imposto
caixa_governo = caixaInicial_governo + imposto

# Circulação.
caixaFinal_familiar = caixa_familiar - gasto_familiar
caixaFinal_governo = imposto - 300 # Houve gasto público.
caixaFinal_empresa = caixa_empresa + gasto_familiar + gasto_publico
