ALIQUOTA_IMPOSTO = 0.20
PROPENSAO_CONSUMO = 0.80
PROPENSAO_POUPANCA = 0.20

def fluxo_circular_renda(meses=3):
    caixa_empresa = 5000
    caixa_familiar = 0
    caixa_governo = 0

    salario_bruto = 1000
    gasto_publico = 300

    imposto_renda = ALIQUOTA_IMPOSTO * salario_bruto
    salario_liquido = salario_bruto - imposto_renda
    consumo_familiar = PROPENSAO_CONSUMO * salario_liquido
    poupanca_familiar = PROPENSAO_POUPANCA * salario_liquido

    for mes in range(1, meses + 1):
        caixa_empresa_inicial = caixa_empresa
        caixa_empresa = caixa_empresa - salario_bruto

        caixa_familiar_inicial = caixa_familiar
        caixa_familiar = caixa_familiar + salario_liquido

        caixa_governo_inicial = caixa_governo
        caixa_governo = caixa_governo + imposto_renda

        caixa_familiar = caixa_familiar - consumo_familiar
        caixa_governo = caixa_governo - gasto_publico
        caixa_empresa = caixa_empresa + consumo_familiar + gasto_publico

        if caixa_empresa < caixa_empresa_inicial:
            empresa_agente = "Deficitário"
        elif caixa_empresa > caixa_empresa_inicial:
            empresa_agente = "Superavitário"
        else:
            empresa_agente = "Neutro"

        if caixa_familiar < caixa_familiar_inicial:
            familiar_agente = "Deficitário"
        elif caixa_familiar > caixa_familiar_inicial:
            familiar_agente = "Superavitário"
        else:
            familiar_agente = "Neutro"

        if caixa_governo < caixa_governo_inicial:
            governo_agente = "Deficitário"
        elif caixa_governo > caixa_governo_inicial:
            governo_agente = "Superavitário"
        else:
            governo_agente = "Neutro"

        print(f"No mês {mes}: | Empresa: {caixa_empresa} | Família: {caixa_familiar} | Governo: {caixa_governo}")
        print(f"No mês em questão, a Empresa foi um Agente {empresa_agente}, o grupo Familiar foi um Agente {familiar_agente} e o Governo foi um Agente {governo_agente}")

fluxo_circular_renda(6)
