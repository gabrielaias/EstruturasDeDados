import time

# Código sem uso eficiente de estrutura de dados
def busca_inocente(lista, elemento):
    for item in lista:
        if item == elemento:
            return True
    return False

# Código otimizado usando conjunto (hash table)
def busca_otimizada(conjunto, elemento):
    return elemento in conjunto

# Criando uma grande lista e conjunto
dados_lista = list(range(10**6))
dados_conjunto = set(dados_lista)

elemento_procurado = 999999

# Testando tempo de execução
inicio = time.time()
busca_inocente(dados_lista, elemento_procurado)
print("Busca em Lista:", time.time() - inicio, "segundos")

inicio = time.time()
busca_otimizada(dados_conjunto, elemento_procurado)
print("Busca em Conjunto:", time.time() - inicio, "segundos")
