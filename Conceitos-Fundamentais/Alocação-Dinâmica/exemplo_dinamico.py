"""
Exemplo de Alocação Dinâmica de Memória em Python

Neste exemplo, demonstramos como funciona a alocação dinâmica usando:
1. Listas que crescem dinamicamente
2. Dicionários
3. Objetos de classes
4. Alocação dinâmica de arrays
"""

class Funcionario:
    def __init__(self, nome, cargo, salario):
        # Atributos de instância são alocados dinamicamente quando o objeto é criado
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.beneficios = []  # Lista vazia que pode crescer dinamicamente
    
    def adicionar_beneficio(self, beneficio):
        # A lista cresce dinamicamente conforme adicionamos itens
        self.beneficios.append(beneficio)
    
    def calcular_salario_total(self):
        valor_beneficios = sum(b["valor"] for b in self.beneficios)
        return self.salario + valor_beneficios
    
    def exibir_info(self):
        print(f"\nInformações do Funcionário:")
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário base: R${self.salario:.2f}")
        
        if self.beneficios:
            print("Benefícios:")
            for b in self.beneficios:
                print(f"  - {b['nome']}: R${b['valor']:.2f}")
        
        print(f"Salário total: R${self.calcular_salario_total():.2f}")


def exemplo_lista_dinamica():
    print("\nExemplo de Lista com Alocação Dinâmica:")
    
    # Lista vazia (inicialmente não ocupa espaço para elementos)
    tarefas = []
    
    # À medida que adicionamos elementos, a memória é alocada dinamicamente
    print("Adicionando tarefas à lista...")
    tarefas.append("Estudar programação")
    print(f"Lista após adicionar 1 item: {tarefas}")
    
    tarefas.append("Fazer exercícios")
    tarefas.append("Preparar apresentação")
    print(f"Lista após adicionar mais itens: {tarefas}")
    
    # Removendo um item (a memória pode ser liberada)
    tarefa_removida = tarefas.pop(1)
    print(f"Item removido: {tarefa_removida}")
    print(f"Lista após remover um item: {tarefas}")
    
    # Adicionando muitos itens de uma vez
    print("Adicionando mais 5 tarefas...")
    for i in range(5):
        tarefas.append(f"Nova tarefa {i+1}")
    
    print(f"Lista final com {len(tarefas)} tarefas:")
    for i, tarefa in enumerate(tarefas):
        print(f"  {i+1}. {tarefa}")


def exemplo_dicionario_dinamico():
    print("\nExemplo de Dicionário com Alocação Dinâmica:")
    
    # Dicionário vazio
    produto = {}
    
    # Adicionando campos dinamicamente
    produto["id"] = 1001
    produto["nome"] = "Notebook"
    produto["preco"] = 4500.00
    
    print("Dicionário após adicionar campos iniciais:")
    for chave, valor in produto.items():
        print(f"  {chave}: {valor}")
    
    # Adicionando mais campos
    produto["especificacoes"] = {
        "processador": "Intel i7",
        "memoria": "16GB",
        "armazenamento": "512GB SSD"
    }
    
    # Adicionando uma lista dinâmica dentro do dicionário
    produto["avaliacoes"] = []
    
    # Adicionando itens à lista dentro do dicionário
    produto["avaliacoes"].append({"usuario": "Carlos", "nota": 4.5})
    produto["avaliacoes"].append({"usuario": "Maria", "nota": 5.0})
    
    print("\nDicionário final com estruturas aninhadas:")
    print(f"Produto: {produto['nome']}")
    print(f"Preço: R${produto['preco']:.2f}")
    print("Especificações:")
    for chave, valor in produto["especificacoes"].items():
        print(f"  {chave}: {valor}")
    
    print("Avaliações:")
    for av in produto["avaliacoes"]:
        print(f"  {av['usuario']}: {av['nota']} estrelas")


def exemplo_array_dinamico():
    print("\nExemplo de Array com Tamanho Dinâmico:")
    
    # Solicitando ao usuário o tamanho do array
    try:
        tamanho = int(input("Digite o tamanho do array que deseja criar: "))
        
        # Array criado dinamicamente com base na entrada do usuário
        numeros = [0] * tamanho
        print(f"Array criado com {tamanho} posições.")
        
        # Preenchendo o array
        for i in range(tamanho):
            numeros[i] = i * 10
        
        print("Array preenchido:")
        print(numeros)
        
    except ValueError:
        print("Por favor, digite um número válido.")


# Função principal para demonstrar diferentes exemplos
def main():
    print("EXEMPLO DE ALOCAÇÃO DINÂMICA EM PYTHON")
    print("=" * 40)
    
    # Criando objetos dinamicamente
    print("Criando funcionários (objetos alocados dinamicamente)...")
    
    # A cada chamada de Funcionario(), um novo objeto é alocado dinamicamente na memória
    funcionario1 = Funcionario("Ana Silva", "Desenvolvedora", 6000.00)
    funcionario2 = Funcionario("Carlos Santos", "Gerente de Projetos", 8500.00)
    
    # Adicionando benefícios (listas dentro dos objetos crescem dinamicamente)
    funcionario1.adicionar_beneficio({"nome": "Vale Refeição", "valor": 500.00})
    funcionario1.adicionar_beneficio({"nome": "Plano de Saúde", "valor": 300.00})
    
    funcionario2.adicionar_beneficio({"nome": "Vale Refeição", "valor": 500.00})
    funcionario2.adicionar_beneficio({"nome": "Plano de Saúde", "valor": 450.00})
    funcionario2.adicionar_beneficio({"nome": "Bônus", "valor": 1000.00})
    
    # Exibindo informações dos funcionários
    funcionario1.exibir_info()
    funcionario2.exibir_info()
    
    # Exemplos adicionais
    exemplo_lista_dinamica()
    exemplo_dicionario_dinamico()
    
    # Exemplo com entrada do usuário
    # Descomente a linha abaixo se quiser testar este exemplo
    # exemplo_array_dinamico()
    
    print("\nObservação importante:")
    print("Em Python, todas as estruturas de dados são alocadas dinamicamente no heap.")
    print("O garbage collector gerencia automaticamente a liberação de memória")
    print("quando não há mais referências aos objetos alocados.")


if __name__ == "__main__":
    main()
