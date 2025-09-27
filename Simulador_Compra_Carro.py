entrada = input("Digite o preço do carro: ")

if entrada != "":
    valor_carro = float(entrada)
    desconto_vista = 0.20
    acrescimo_parcelado = 0

    print("O preço final á vista com desconto 20% é: R$ {}".format( valor_carro - (valor_carro * desconto_vista)))

    for i in range(6, 61, 6):
        acrescimo_parcelado += 0.03
        valor_final_parcelado = valor_carro + (valor_carro *    acrescimo_parcelado)
        print("O preço parcelado em {} X é de R$ {:.2f} com parcelas de R$ {:.2f}".format(i, valor_final_parcelado,valor_final_parcelado / i))

else:
    print("Nenhum valor foi inserido, digite um valor válido!")