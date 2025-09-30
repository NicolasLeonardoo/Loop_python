dias_semana = ["segunda-feira", "terca-feira", "quarta-feira", "quinta-feira", "sexta-feira"]
contagem_votos = {
    "segunda-feira": 0,
    "terça-feira": 0,
    "quarta-feira": 0,
    "quinta-feira": 0,
    "sexta-feira": 0
}

colaboradores = int(input("Informme o número de colaboradores: "))
if colaboradores < 1:
    print("Digite um número valido de colaboradores")

for i in range(colaboradores):
    voto = input(f"Informe o dia da sua preferencia (segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira): ").lower()
    if voto in dias_semana:
        contagem_votos[voto] += 1
    else:
        print("Dia da semana inválido!")

votos_vencedor = -1
vencedores = []

for dia, votos in contagem_votos.items():
    if votos > votos_vencedor:
        votos_vencedor = votos
        vencedores = [dia]
    elif votos == votos_vencedor:
        vencedores.append(dia)
if len(vencedores) == 1 and votos_vencedor > 0:
    print(f"O dia escolhido pelos colaboradores é {vencedores[0]}")
elif len(vencedores) > 1:
    print(f"Houve um empate entre os dias {vencedores}")
else:
    print("Nenhum voto foi computado!")