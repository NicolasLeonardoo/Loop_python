print("Escolha o tipo de investimento: \n1. CDB \n2. LCI \n3. LCA")

try:
    tipo_investimento = int(input("Digite o tipo de investimento (1, 2 ou 3): "))

    match tipo_investimento:
        case 1:
            valor_resgate = float(input("Digite o valor a ser resgatado: R$ "))
            dias_investidos = int(input("Digite o número de dias que o valor permaneceu investido: "))
            aliquota_ir = 0
            
            if dias_investidos <= 180:
                aliquota_ir = 22.5
            elif 181 <= dias_investidos <= 360:
                aliquota_ir = 20
            elif 361 <= dias_investidos <= 720:
                aliquota_ir = 17.5
            else:
                aliquota_ir = 15
                
            valor_imposto = valor_resgate * (aliquota_ir / 100)
            print(f"O valor do imposto de renda a ser pago é: R$ {valor_imposto}")
        case 2 | 3:
            print("Investimento isento de impostos!")
        
        case _:
            print("Selecione um tipo de investimento válido! (1, 2 ou 3).")

except ValueError:
    print("Erro: Por favor, digite apenas um numero (1, 2 ou 3).")