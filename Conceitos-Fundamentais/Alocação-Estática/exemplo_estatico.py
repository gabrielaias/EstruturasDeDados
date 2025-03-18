# Variável global (alocada estaticamente durante todo o programa)
TAXA_IMPOSTO = 0.15

def calcular_salario():
    # Variáveis locais (alocadas estaticamente dentro da função)
    salario_base = 5000.0         # Float: tipicamente 8 bytes
    horas_extras = 10             # Int: tipicamente 4 bytes
    valor_hora_extra = 50.0       # Float: tipicamente 8 bytes
    
    # Array de tamanho fixo (lista com 12 elementos)
    # Alocação estática, pois o tamanho é conhecido no início
    meses_do_ano = ["Janeiro", "Fevereiro", "Março", "Abril", 
                    "Maio", "Junho", "Julho", "Agosto", 
                    "Setembro", "Outubro", "Novembro", "Dezembro"]
    
    # Matriz 3x3 (fixa)
    matriz_fixa = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    # Cálculo usando as variáveis alocadas estaticamente
    valor_extras = horas_extras * valor_hora_extra
    salario_bruto = salario_base + valor_extras
    salario_liquido = salario_bruto * (1 - TAXA_IMPOSTO)
    
    print(f"Mês atual: {meses_do_ano[4]}")  # Acessando um elemento do array fixo
    print(f"Salário base: R${salario_base:.2f}")
    print(f"Valor de horas extras: R${valor_extras:.2f}")
    print(f"Salário bruto: R${salario_bruto:.2f}")
    print(f"Salário líquido após impostos: R${salario_liquido:.2f}")
    print(f"Elemento da matriz: {matriz_fixa[1][1]}")  # Acessando elemento da matriz

def demonstrar_memoria_estatica():
    # Tupla (imutável e tamanho fixo)
    dias_semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo")
    
    # Variáveis de tipos primitivos
    idade = 30                 # Int: 4 bytes
    altura = 1.75              # Float: 8 bytes
    nome = "João"              # String: tamanho fixo
    esta_ativo = True          # Boolean: 1 byte
    
    print("\nDemonstração de variáveis com alocação estática:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Altura: {altura}m")
    print(f"Está ativo: {esta_ativo}")
    print(f"Dia da semana: {dias_semana[2]}")

# Execução do programa
if __name__ == "__main__":
    print("EXEMPLO DE ALOCAÇÃO ESTÁTICA EM PYTHON")
    print("=" * 40)
    calcular_salario()
    demonstrar_memoria_estatica()
