tabela_juros = {
    1: 0,
    3: 10,
    6: 15,
    9: 20,
    12: 25
}

entrada = input("Digite o valor da dívida: R$ ")
if entrada != "":
    valor_divida = float(entrada)
    
    for parcela, juros in tabela_juros.items():
        valor_juros = valor_divida * (juros / 100)
        valor_total = valor_divida + valor_juros
        valor_parcela = valor_total / parcela

        print("Total: R$ {:.2f} Juros: R$ {:.2f} Número de parcelas: {} Valor da Parcela: R$ {:.2f}".format(valor_total, valor_juros, parcela, valor_parcela))
else:
    print("Digite um valor válido!")