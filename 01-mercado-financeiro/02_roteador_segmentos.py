def classificar_operacao(moeda, tipo_ativo, prazo_dias):
    moeda = moeda.strip().upper()
    tipo_ativo = tipo_ativo.strip().upper()

    if moeda != "BRL":
        return "Mercado de Câmbio"
    elif tipo_ativo == "TITULO_PUBLICO" and prazo_dias <= 1:
        return "Mercado Monetário"
    elif tipo_ativo in ["EMPRESTIMO", "CAPITAL_GIRO", "FINANCIAMENTO", "CREDITO_PESSOAL"]:
        return "Mercado de Crédito"
    elif tipo_ativo in ["NOTAS_PROMISSORIAS", "ACOES", "DEBENTURES", "FUNDO_INVESTIMENTO"]:
        return "Mercado de Capitais"
    else:
        return "Não se encaixa em nenhum dos 4 mercados financeiros"
