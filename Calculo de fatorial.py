numero = int(input('Número: ')) # Pergunta um número inteiro para a pessoa
if numero > 0: # Verifica se o número é positivo e executa as funções abaixo
    fatorial = 1 # Cria uma variável com o nome fatorial e o valor 1
    for item in range(1, numero + 1): # Cria um laço de repetição para somar os valores
        fatorial = fatorial * item # Substitui a antiga variável fatorial
    print(fatorial) # Escreve na tela a nova variável fatorial com a multiplicação indicada na linha 5
else: # Se o valor for negativo 
    print('Qq') # Vai mostrar isso aqui na tela :P

    