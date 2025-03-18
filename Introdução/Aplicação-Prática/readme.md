# Aplicação Prática: Verificação de Parênteses Balanceados

## Descrição do Problema
O problema consiste em verificar se uma expressão contém parênteses balanceados, ou seja, se cada parêntese de abertura '(' tem um correspondente de fechamento ')' na ordem correta. Isso é comum em compiladores e editores de código.

### Exemplos
- Válido: `(a + b) * (c - d)` → Resultado: True
- Inválido: `((a + b)` → Resultado: False

## Solução
Utilizamos uma **pilha** (LIFO) para resolver o problema:
1. Para cada '(' encontrado, empilhamos na pilha.
2. Para cada ')' encontrado, desempilhamos e verificamos se há um '(' correspondente.
3. No final, a pilha deve estar vazia para a expressão ser válida.

## Implementação
A solução está no arquivo [`verifica_parenteses.py`](./verifica_parenteses.py), onde implementamos uma classe Pilha e uma função para verificar o balanceamento.
