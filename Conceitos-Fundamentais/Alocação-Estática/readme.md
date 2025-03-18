# Alocação Estática de Memória

A alocação estática de memória é um método de alocação onde o espaço de memória para variáveis é definido durante a compilação do programa, antes mesmo da execução. Este tipo de alocação tem características específicas que a distinguem da alocação dinâmica.

## Características Principais

1. **Tempo de Alocação**: Ocorre em tempo de compilação.
2. **Localização na Memória**: As variáveis são armazenadas na região de memória chamada "Stack" (Pilha).
3. **Duração**: A memória alocada estaticamente permanece disponível durante todo o tempo de vida da função onde foi declarada.
4. **Gerenciamento de Memória**: A liberação da memória é automática e ocorre quando a variável sai de escopo.
5. **Tamanho Fixo**: O tamanho da memória alocada é fixo e não pode ser alterado durante a execução.

## Exemplos de Uso

- Variáveis locais em funções
- Arrays de tamanho fixo
- Variáveis globais
- Variáveis estáticas em funções

## Vantagens

- Acesso mais rápido à memória
- Gerenciamento de memória simplificado (automático)
- Menor risco de vazamentos de memória
- Melhor para alocações de tamanho conhecido e fixo

## Desvantagens

- Inflexibilidade quanto ao tamanho da memória alocada
- Não é adequada para estruturas de dados cujo tamanho varia durante a execução
- Pode causar estouro de pilha (stack overflow) se muitas variáveis forem alocadas

## Aplicação

A alocação estática é ideal para variáveis de tamanho pequeno e conhecido, como inteiros, floats, e pequenos arrays. É também mais eficiente quando o programa não precisa de flexibilidade quanto ao tamanho das estruturas de dados.

Veja o arquivo `exemplo_estatico.py` para um exemplo prático de alocação estática em Python.
