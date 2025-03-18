class Pilha:
    def __init__(self):
        self.elementos = []

    def empilhar(self, valor):
        self.elementos.append(valor)

    def desempilhar(self):
        if self.elementos:
            return self.elementos.pop()
        return None

    def consultar_topo(self):
        if self.elementos:
            return self.elementos[-1]
        return None

# Exemplo de uso
pilha = Pilha()
pilha.empilhar("Página1")
pilha.empilhar("Página2")
print(pilha.elementos)  # ['Página1', 'Página2']
pilha.empilhar("Página3")
print(pilha.consultar_topo())  # 'Página3'
pilha.desempilhar()
print(pilha.elementos)  # ['Página1', 'Página2']
