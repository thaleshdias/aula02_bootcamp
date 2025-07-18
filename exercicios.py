# EXERCÍCIOS DE INTEIROS AULA 02
#1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.


#primeiro_valor = int(input("Digite um valor inteiro: "))
#segundo_valor = int(input("Digite outro valor inteiro: "))
#valor_final = primeiro_valor + segundo_valor
#print(f"Você inseriu o valor {primeiro_valor} e em sequência o valor {segundo_valor}. A soma destes valores é igual a {valor_final}!")


#2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

#valor_entrada = int(input("Digite um valor inteiro: "))
#CONSTANTE_DIVISAO = int(5)
#valor_resto = valor_entrada % CONSTANTE_DIVISAO
#print(f"O resto da divisão do valor inserido por 5 é: {valor_resto}")



#3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

#vlr_entrada01 = int(input("Digite o primeiro valor: "))
#vlr_entrada02 = int(input("Digite o segundo valor: "))
#vlr_final = vlr_entrada01 * vlr_entrada02
#print(f"A multiplicação de {vlr_entrada01} por {vlr_entrada02} é igual a: {vlr_final}")


#4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

#vlr_entrada01 = int(input("Digite o primeiro valor inteiro: "))
#vlr_entrada02 = int(input("Digite o segundo valor inteiro: "))
#vlr_final = vlr_entrada01 // vlr_entrada02
#print(f"A divisão inteira de {vlr_entrada01} por {vlr_entrada02} é igual a: {vlr_final}")


#5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

#vlr_entrada = int(input("Digite o valor inteiro: "))
#vlr_final = vlr_entrada **2
#print(f"O quadrado de {vlr_entrada} é {vlr_final}")

#EXERCICIOS DE FLOAT AULA 2

#6. Escreva um programa que receba dois números flutuantes e realize sua adição.

#vlr_entrada01 = float(input("Digite o primeiro valor: "))
#vlr_entrada02 = float(input("Digite o segundo valor: "))
#vlr_total = vlr_entrada01 + vlr_entrada02
#print(f"A soma dos dois valores inseridos é {vlr_total}")

#7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

#vlr_entrada01 = float(input("Digite o primeiro valor: "))
#vlr_entrada02 = float(input("Digite o segundo valor: "))
#vlr_total = (vlr_entrada01 + vlr_entrada02) / 2
#print(f"A média dos valores {vlr_entrada01} e {vlr_entrada02} é igual a: {vlr_total}")


#8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

#vlr_base = float(input("Digite o valor base: "))
#vlr_potencia = float(input("Digite o valor da potencia: "))
#vlr_total = vlr_base**vlr_potencia
#print(f"A potencia do número {vlr_base} é igual a: {vlr_total}")



#9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

#vlr_celcius = float(input("Digite a temperatura em Celcius (somente número): "))
#vlr_fahrenheit = (vlr_celcius * 1.8) + 32
#print(f"O valor de {vlr_celcius} ºC em Fahrenheit é equivalente a {vlr_fahrenheit} ºF")


#10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

#CONSTANTE_PI = float(3.1415)
#vlr_raio = float(input("Digite o valor do raio do círculo: "))
#vlr_area = (vlr_raio**2) * CONSTANTE_PI
#print(f"A área do círculo é {vlr_area} com base no raio {vlr_raio} que você informou!")

#EXERCICIOS DE STRING AULA 2

#11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

#str_entrada = input("Digite o texto a ser convertido para letras maiusculas: ")
#print(str_entrada.upper())


#12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

#nome_completo = input("Digite o seu nome completo: ")
#print(nome_completo.lower())

#13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

#frase_completa = input("Digite uma frase: ")
#print(frase_completa.strip())


#14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

#data_formatada = input("Digite a data no formato: DD/MM/YYYY: ")
#data_separada = data_formatada.split('/')
#print(data_separada)


#15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

#primeira_string = input('Digite uma frase: ')
#segunda_string = input('Digite outra frase: ')
#print(primeira_string + " " + segunda_string)


#EXERCICIOS BOOLEANOS AULA 2

#16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

#vlr_entrada01 = input("Você gosta de carne (True ou False): ")
#vlr_entrada02 = input("Você gosta de batata (True ou False): ")
#resultado_and = vlr_entrada01 and vlr_entrada02
#print(resultado_and)

#17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

#vlr_entrada01 = input("Você gosta de carne (True ou False): ")
#vlr_entrada02 = input("Você gosta de batata (True ou False): ")
#resultado_or = vlr_entrada01 and vlr_entrada02
#print(resultado_or)

#18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

#vlr_entrada = input("Insira um valor booleano (True ou False): ")
#resultado_not = not vlr_entrada
#print(resultado_not)

#19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

#vlr_entrada01 = float(input("Digite o primeiro número: "))
#vlr_entrada02 = float(input("Digite o segundo número: "))
#vlr_resultado = vlr_entrada01 == vlr_entrada02
#print(vlr_resultado)


#20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

vlr_entrada01 = float(input("Digite o primeiro número: "))
vlr_entrada02 = float(input("Digite o segundo número: "))
vlr_resultado = vlr_entrada01 != vlr_entrada02
print(vlr_resultado)