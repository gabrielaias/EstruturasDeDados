class Fila:
    def __init__(self):
        self.elementos = []

    def enfileirar(self, valor):
        self.elementos.append(valor)

    def desenfileirar(self):
        if self.elementos:
            return self.elementos.pop(0)
        return None

    def consultar_inicio(self):
        if self.elementos:
            return self.elementos[0]
        return None

# Exemplo de uso
fila = Fila()
fila.enfileirar("Doc1")
fila.enfileirar("Doc2")
print(fila.elementos)  # ['Doc1', 'Doc2']
fila.desenfileirar()
print(fila.elementos)  # ['Doc2']
print(fila.consultar_inicio())  # 'Doc2'
