# Alocação Dinâmica de Memória

A alocação dinâmica de memória é um método de alocação onde o espaço de memória para variáveis é alocado durante a execução do programa, conforme necessário. Este tipo de alocação oferece mais flexibilidade comparado à alocação estática.

## Características Principais

1. **Tempo de Alocação**: Ocorre em tempo de execução.
2. **Localização na Memória**: As variáveis são armazenadas na região de memória chamada "Heap" (Monte).
3. **Duração**: A memória alocada permanece disponível até ser explicitamente liberada (em linguagens como C/C++) ou até que não haja mais referências a ela (em linguagens com garbage collection).
4. **Gerenciamento de Memória**: 
   - Em linguagens como C/C++: Gerenciada manualmente pelo programador
   - Em linguagens como Python, JavaScript, Java: Gerenciada automaticamente pelo garbage collector
5. **Tamanho Flexível**: O tamanho da memória alocada pode ser determinado durante a execução e pode variar.

## Exemplos de Uso

- Estruturas de dados cujo tamanho não é conhecido em tempo de compilação
- Listas, árvores, grafos e outras estruturas que crescem ou diminuem
- Objetos criados com operadores como `new` em C++/Java
- Arrays de tamanho variável
- Objetos complexos em linguagens orientadas a objetos

## Vantagens

- Flexibilidade quanto ao tamanho da memória alocada
- Capacidade de criar e destruir objetos conforme necessário
- Melhor utilização da memória disponível
- Ideal para estruturas de dados complexas e de tamanho variável

## Desvantagens

- Acesso mais lento à memória comparado à alocação estática
- Possibilidade de vazamentos de memória (especialmente em linguagens sem garbage collector)
- Fragmentação da memória ao longo do tempo
- Overhead adicional para gerenciamento da memória

## Aplicação

A alocação dinâmica é essencial para aplicações que trabalham com grandes volumes de dados ou estruturas cujo tamanho varia significativamente durante a execução. É amplamente utilizada em programação orientada a objetos e em estruturas de dados avançadas.

Veja o arquivo [`exemplo_dinamico.py`](./exemplo_dinamico.py) para um exemplo prático de alocação dinâmica em Python.
