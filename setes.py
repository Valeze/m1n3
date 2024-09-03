
set_inicial = {11, 12, 13, 14}


print("Conteúdo do set inicial:", set_inicial)


set_inicial.add(15)


print("Conteúdo do set após add:", set_inicial)


set_inicial.update({1, 2, 3, 4, 5})


print("Conteúdo do set após update:", set_inicial)


set_inicial.discard(13)


print("Conteúdo do set após discard:", set_inicial)


novo_set = {20, 21, 23, 1, 2}


print("Conteúdo do novo set:", novo_set)


uniao = set_inicial.union(novo_set)
print("União dos sets:", uniao)

intersecao = set_inicial.intersection(novo_set)
print("Interseção dos sets:", intersecao)


diferenca = set_inicial.difference(novo_set)
print("Diferença entre os sets (set_inicial - novo_set):", diferenca)


dif_simetrica = set_inicial.symmetric_difference(novo_set)
print("Diferença simétrica entre os sets:", dif_simetrica)