
dicionario = {1: {'nome': 'Maria', 'idade': 26, 'nacionalidade': 'brasileira'}}


dicionario.update({
    2: {'nome': 'João', 'idade': 30, 'nacionalidade': 'português'},
    3: {'nome': 'Ana', 'idade': 22, 'nacionalidade': 'espanhola'}
})


print("Dicionário atualizado:", dicionario)


dicionario_copia = dicionario.copy()


elemento_removido = dicionario.pop(2)
print("Elemento removido:", elemento_removido)
print("Dicionário após remoção com 'pop':", dicionario)


ultimo_elemento_removido = dicionario.popitem()
print("Último elemento removido:", ultimo_elemento_removido)
print("Dicionário após remoção com 'popitem':", dicionario)


dicionario.clear()
dicionario_copia.clear()

print("Dicionário original após 'clear':", dicionario)
print("Cópia do dicionário após 'clear':", dicionario_copia)

novas_chaves = [1, 2, 3]
novo_dicionario = dict.fromkeys(novas_chaves, "Valor padrão")


print("Novo dicionário - items:", novo_dicionario.items())

print("Novo dicionário - chaves:", novo_dicionario.keys())


print("Novo dicionário - valores:", novo_dicionario.values())