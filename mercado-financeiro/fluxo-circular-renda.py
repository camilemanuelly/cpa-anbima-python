cx_inicial_empresa = 5000
cx_inicial_familia = 0

salario = 1000

saldo_empresa_pos_salario = cx_inicial_empresa - salario
cx_salario_familia = cx_inicial_familia + salario

gasto_familia = 0.80 * salario
poupanca_familia = 0.20 * salario

total_familia = salario - gasto_familia
retorno_empresa = gasto_familia + saldo_empresa_pos_salario


