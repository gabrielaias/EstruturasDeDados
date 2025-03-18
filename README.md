# Estruturas de Dados em Python

Este repositório contém exemplos, explicações e implementações de diversas estruturas de dados utilizando Python. O objetivo é fornecer um material didático completo para estudantes e desenvolvedores que desejam aprofundar seus conhecimentos neste tema fundamental da ciência da computação.

## 📚 Conteúdo do Repositório

- **[Introdução](#introdução)**: Conceitos básicos e importância das estruturas de dados
- **[Conceitos Fundamentais](#conceitos-fundamentais)**: Alocação de memória estática e dinâmica
- **[Definição e Importância](#definição-e-importância)**: Diferenças entre estruturas lineares e não lineares e seu impacto no desempenho
- **[Estruturas Lineares](#estruturas-lineares)**: Listas, pilhas e filas
- **[Aplicações Práticas](#aplicações-práticas)**: Exemplos reais de uso das estruturas de dados

## 🔍 Introdução

As estruturas de dados são maneiras organizadas de armazenar e gerenciar dados em um computador. Cada estrutura possui características, vantagens e desvantagens específicas, tornando-as mais adequadas para determinados tipos de problemas.

### Importância na Ciência da Computação:

- **Eficiência**: Permite operações otimizadas
- **Organização**: Facilita o gerenciamento de grandes volumes de dados
- **Abstração**: Simplifica o desenvolvimento de algoritmos complexos
- **Reutilização**: Fornece soluções padronizadas para problemas recorrentes
- **Desempenho**: Melhora significativamente a performance do programa

Para mais detalhes, consulte o [README da Introdução](./Introdução/README.md).

## 🧠 Conceitos Fundamentais

### Alocação de Memória

#### Alocação Estática
- **Tempo**: Ocorre em tempo de compilação
- **Local**: Armazenada na Stack (pilha)
- **Duração**: Disponível durante o tempo de vida da função
- **Gerenciamento**: Automático
- **Exemplo**: [exemplo_estatico.py](./Conceitos-Fundamentais/Alocação-Estática/exemplo_estatico.py)

#### Alocação Dinâmica
- **Tempo**: Ocorre em tempo de execução
- **Local**: Armazenada no Heap (monte)
- **Duração**: Disponível até ser liberada ou perder referências
- **Gerenciamento**: Manual ou automático (garbage collector)
- **Exemplo**: [exemplo_dinamico.py](./Conceitos-Fundamentais/Alocação-Dinâmica/exemplo_dinamico.py)

## 📊 Definição e Importância

### Estruturas Lineares vs. Não Lineares

#### Estruturas Lineares
- Organizam dados sequencialmente
- Cada elemento tem um sucessor/antecessor direto
- **Exemplos**: Arrays, Filas, Pilhas, Listas Encadeadas

#### Estruturas Não Lineares
- Não seguem uma sequência única
- Elementos podem estar ligados de várias formas
- **Exemplos**: Árvores, Grafos, Tabelas Hash

### Impacto no Desempenho

A escolha da estrutura correta pode afetar drasticamente o desempenho:
- **Tempo de Execução**: Algoritmos eficientes reduzem o tempo de processamento
- **Uso de Memória**: Algumas estruturas armazenam dados de forma mais compacta

Para um exemplo prático, consulte [desempenho.py](./Definição-Importância/desempenho.py).

## 📋 Estruturas Lineares

### Listas
- Armazenam elementos em sequência
- Permitem inserção, remoção e acesso em qualquer posição
- [Implementação de exemplo](./Estruturas-Lineares/Listas/exemplo.py)

### Pilhas (LIFO)
- Last In, First Out: o último a entrar é o primeiro a sair
- Operações: empilhar, desempilhar, consultar topo
- [Implementação de exemplo](./Estruturas-Lineares/Pilhas/exemplo.py)

### Filas (FIFO)
- First In, First Out: o primeiro a entrar é o primeiro a sair
- Operações: enfileirar, desenfileirar, consultar início
- [Implementação de exemplo](./Estruturas-Lineares/Filas/exemplo.py)

## 🛠️ Aplicações Práticas

### Verificação de Parênteses Balanceados
- Problema comum em compiladores e editores de código
- Utiliza pilha para rastrear parênteses de abertura e fechamento
- [Implementação de exemplo](./Introdução/Aplicação-Prática/checaParenteses.py)

### Outros Casos de Uso no Mundo Real
- **Sistemas de Navegação GPS**: Grafos
- **Redes Sociais**: Grafos, Árvores, Tabelas Hash
- **Sistemas de Busca**: Árvores B, Tabelas Hash, Filas de Prioridade
- **Sistemas Bancários**: Filas, Listas Ligadas, Árvores Balanceadas
- **Processamento de Imagens**: Matrizes, Árvores Quadtree, Grafos
- **Análise de Dados**: DataFrames, Arrays N-dimensionais, Séries Temporais

## 🚀 Como Usar Este Repositório

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/estruturas-dados-python.git
   ```

2. **Navegue pelos diretórios** para encontrar explicações e exemplos de implementação.

3. **Execute os exemplos** para ver as estruturas em funcionamento:
   ```bash
   python Estruturas-Lineares/Pilhas/exemplo.py
   ```

## 📘 Referências Recomendadas

- **Livros**:
  - "Estruturas de Dados e Algoritmos em Python", de Michael T. Goodrich
  - "Python Fluente", de Luciano Ramalho

- **Cursos Online**:
  - Alura: Estrutura de Dados em Python
  - Hashtag Treinamentos: Python para Análise de Dados
  - Rocketseat: Python Ignite - Dominando estruturas de dados

## 🤝 Participantes:

Gabriel Aías
Arthur Gomes
