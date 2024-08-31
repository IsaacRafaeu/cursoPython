# # Desafio 02
numero_inteiro = int (input("Digite um valor de 0 a 10: "))
antecessor = numero_inteiro - 1
sucessor = numero_inteiro + 1
print(f"O sucessor é igual a {sucessor}")
print(f"O antecessor é igual a {antecessor}")

# # Desafio 03
hum_numero = int (input("Digite um valor de 0 a 10: "))
dobro = hum_numero * 2
triplo = hum_numero ** 3
quadrado = hum_numero ** 2
print(f"O  valor dobro é igual a {dobro}") 
print(f"O valor do triplo é igual a {triplo}") 
print(f"O valor do quadrado é igual a {quadrado}") 

#Desafio 04
nota_1 = float (input("Digite o valor da nota 1: "))
nota_2 = float (input("Digite o valor da nota 2: "))
soma = nota_1 + nota_2
media = soma / 2
print(f"A média é igual a {media}")

# #Desafio 05
dinheiro_real = float(input("Digite o valor que possui na carteira: "))
dolar = 5
conversao = dinheiro_real / dolar
print(f"Você pode comprar {conversao:.2f} dólares.") 

# Desafio 03
import math
hum_numero = int (input("Digite um valor de 0 a 10: "))
dobro = hum_numero * 2
triplo = hum_numero ** 3
quadrado = hum_numero ** 2
raiz = math.sqrt(hum_numero) 
print(f"propriedade do {hum_numero} \n Dobro: {dobro} \n Triplo: {triplo} \n Quadrado: {quadrado} \n Raiz quadrada {raiz:.2f}")
print(f"O  valor dobro é igual a {dobro}") 
print(f"O valor do triplo é igual a {triplo}") 
print(f"O valor do quadrado é igual a {quadrado}") 
print(f"Raiz quadrada é igual a {raiz:.2f}")