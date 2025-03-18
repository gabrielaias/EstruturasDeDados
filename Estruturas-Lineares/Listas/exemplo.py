class Lista:
    def __init__(self):
        self.elementos = []

    def inserir(self, valor, posicao=None):
        if posicao is None:
            self.elementos.append(valor)  # Insere no final
        else:
            self.elementos.insert(posicao, valor)

    def remover(self, posicao):
        if 0 <= posicao < len(self.elementos):
            return self.elementos.pop(posicao)
        return None

    def acessar(self, posicao):
        if 0 <= posicao < len(self.elementos):
            return self.elementos[posicao]
        return None

# Exemplo de uso
lista = Lista()
lista.inserir("Acordar")
lista.inserir("Café")
lista.inserir("Exercício", 1)
print(lista.elementos)  # ['Acordar', 'Exercício', 'Café']
lista.remover(0)
print(lista.elementos)  # ['Exercício', 'Café']
