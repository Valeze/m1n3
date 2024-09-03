
lista_mesclada = [1, 2, 3, "Olá, Python", True, 12.6]


print("Conteúdo da lista:", lista_mesclada)


lista_mesclada.append(["Lista aninhada"])


print("Conteúdo da lista após append:", lista_mesclada)


lista_mesclada.insert(4, 5)


print("Conteúdo da lista após insert:", lista_mesclada)

print("Tamanho da lista:", len(lista_mesclada))


del lista_mesclada[1]


print("Conteúdo da lista após remoção:", lista_mesclada)

nova_lista_mesclada = lista_mesclada[:4]


print("Conteúdo da nova lista:", nova_lista_mesclada)