import random

Estados_Capitais = [
    {"Acre": "Rio Branco"},
    {"Alagoas": "Maceió"},
    {"Amapá": "Macapá"},
    {"Amazonas": "Manaus"},
    {"Bahia": "Salvador"},
    {"Ceará": "Fortaleza"},
    {"Distrito Federal": "Brasília"},
    {"Espírito Santo": "Vitória"},
    {"Goiás": "Goiânia"},
    {"Maranhão": "São Luís"},
    {"Mato Grosso": "Cuiabá"},
    {"Mato Grosso do Sul": "Campo Grande"},
    {"Minas Gerais": "Belo Horizonte"},
    {"Pará": "Belém"},
    {"Paraíba": "João Pessoa"},
    {"Paraná": "Curitiba"},
    {"Pernambuco": "Recife"},
    {"Piauí": "Teresina"},
    {"Rio de Janeiro": "Rio de Janeiro"},
    {"Rio Grande do Norte": "Natal"},
    {"Rio Grande do Sul": "Porto Alegre"},
    {"Rondônia": "Porto Velho"},
    {"Roraima": "Boa Vista"},
    {"Santa Catarina": "Florianópolis"},
    {"São Paulo": "São Paulo"},
    {"Sergipe": "Aracaju"},
    {"Tocantins": "Palmas"}
]
rodadas = 0
pontos = 0
jogando = True

while jogando:
    # Escolhe um estado-capital aleatório
    estado_capital_aleatorio = random.choice(Estados_Capitais)
    estado, capital = list(estado_capital_aleatorio.items())[0]
    
    # Pergunta ao usuário sobre a capital do estado
    rodadas +=1
    resposta = input(f"Rodada {rodadas}. Qual a capital de {estado}? ")
    
    # Verifica se a resposta está correta
    if resposta.lower() == capital.lower():
        pontos += 1
        print("Resposta correta! Pontos:", pontos)
    else:
        print(f"Resposta incorreta! A capital de {estado} é {capital}. Pontos:", pontos)
    
    # Pergunta ao usuário se deseja continuar jogando
    sair = input("Deseja continuar jogando? (s/n): ").strip().lower()
    if sair != 's':
        jogando = False

porc = pontos / rodadas * 100
print("Jogo encerrado. Porcentagem de acertos:", porc)
