meu_dicionario = {
    "codigo_1": "Python",
    "codigo_2": "Java",
    "codigo_3": "PHP"
}


print("Conteúdo do dicionário:", meu_dicionario)


print("Tipo de dados do dicionário:", type(meu_dicionario))


valor_chave_linguagem = meu_dicionario.get("codigo_1")
print("Valor da chave 'linguagem' (código 1):", valor_chave_linguagem)


print("Tamanho do dicionário:", len(meu_dicionario))


dicionario_frutas = {
    1: {"nome": "limão", "tipo": "ácida"},
    2: {"nome": "laranja", "tipo": "ácida"},
    3: {"nome": "manga", "tipo": "semiácida"},
    4: {"nome": "maçã", "tipo": "semiácida"},
    5: {"nome": "banana", "tipo": "doce"},
    6: {"nome": "mamão", "tipo": "doce"}
}


print("Chave 1 - Nome:", dicionario_frutas[1]["nome"], ", Tipo:", dicionario_frutas[1]["tipo"])


print("Chave 2 - Nome:", dicionario_frutas[2]["nome"], ", Tipo:", dicionario_frutas[2]["tipo"])

for chave, valores in dicionario_frutas.items():
    print(f"Chave {chave} - Nome: {valores['nome']}, Tipo: {valores['tipo']}")