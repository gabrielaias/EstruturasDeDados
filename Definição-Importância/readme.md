# Definição e Importância das Estruturas de Dados no Desenvolvimento

## 1. Diferença entre Estruturas de Dados Lineares e Não Lineares

### Estruturas de Dados Lineares  
As estruturas **lineares** organizam os dados de forma sequencial, onde cada elemento tem um sucessor e/ou antecessor direto.

**Exemplos:**  
- **Arrays (Listas em Python)** → `lista = [1, 2, 3, 4]`
- **Filas (Queue)** → FIFO (*First In, First Out*)
- **Pilhas (Stack)** → LIFO (*Last In, First Out*)
- **Listas Encadeadas (Linked List)** → Cada nó aponta para o próximo

**Uso comum:** Quando a ordem dos elementos é importante, como buffers de mensagens ou histórico de páginas visitadas.

---

### Estruturas de Dados Não Lineares  
Aqui, os dados não seguem uma sequência única. Os elementos podem estar ligados de várias formas, formando estruturas mais complexas.

**Exemplos:**  
- **Árvores (Tree)** → Usadas em sistemas de arquivos e bancos de dados
- **Grafos (Graph)** → Modelam redes sociais e mapas de rotas
- **Tabelas Hash (Hash Tables)** → Mapeiam chaves para valores com busca eficiente

**Uso comum:** Quando há necessidade de representações complexas, como redes e hierarquias.

---

## 2. Impacto das Estruturas de Dados no Desempenho

As estruturas de dados são fundamentais para o desempenho dos programas. A escolha correta pode tornar o código muito mais eficiente.

### Comparação de desempenho  
Um código sem estrutura de dados eficiente pode ser muito mais lento. Exemplo:

- **Sem estrutura adequada:** Listas percorridas manualmente para buscas.
- **Com estrutura adequada:** Uso de dicionários (tabelas hash) para buscas rápidas.

### Impacto no desempenho  
- **Tempo de Execução:** Algoritmos eficientes podem reduzir tempo de processamento.
- **Uso de Memória:** Algumas estruturas armazenam dados de forma mais compacta.

🚀 **Exemplo prático:** Veja o código [`desempenho.py`](./desempenho.py) neste repositório.
