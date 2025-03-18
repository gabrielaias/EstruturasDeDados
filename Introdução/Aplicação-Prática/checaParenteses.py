class Pilha:
    def __init__(self):
        self.elementos = []

    def empilhar(self, valor):
        self.elementos.append(valor)

    def desempilhar(self):
        if self.elementos:
            return self.elementos.pop()
        return None

    def esta_vazia(self):
        return len(self.elementos) == 0

def verifica_parenteses(expressao):
    pilha = Pilha()
    
    for char in expressao:
        if char == '(':
            pilha.empilhar(char)
        elif char == ')':
            if pilha.esta_vazia():  # Não há '(' para combinar
                return False
            pilha.desempilhar()  # Remove o '(' correspondente
    
    return pilha.esta_vazia()  # Se a pilha estiver vazia, está balanceado

# Testes
expressoes = [
    "(a + b) * (c - d)",  # True
    "((a + b)",           # False
    "(a + (b * c))",     # True
    ")a + b(",            # False
]

for expr in expressoes:
    resultado = verifica_parenteses(expr)
    print(f"Expressão: {expr} -> Balanceada: {resultado}")
