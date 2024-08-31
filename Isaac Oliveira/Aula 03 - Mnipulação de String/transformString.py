# Trocando uma palavra dentro de um texto
texto = "Isaac Oliveira"
troca_texto = texto.replace("Oliveira" , "Rafael")
print("Meu nome é:" , troca_texto)

# Deixando todos os caracteres em maiúsculo
texto = "isaacraeus@gmail.com"
texto_maiusculo = texto.upper()
print(texto_maiusculo)

# Deixando todos caracteres em minúsculo
texto = "ISAACRAFAEUS@GMAIL.COM"
texto_minusculo  = texto.lower()
print(texto_minusculo)

# Deixando a primeira letra de cada palavra em Maiúsculo
texto = "meu primeiro curso no senai"
texto_editado1 = texto.title()
print(texto_editado1)

# Deixando a primeira letra da frase em Maiúsculo
texto_editado2 = texto.capitalize()
print(texto_editado2)

# Elimina espaços inúteis 
texto = "         SENAI"
print(f"A palavra:| {texto}| tem {len(texto)} caracteres")

texto_strip = texto.strip()
print(f"A palavra {texto_strip} tem {len(texto_strip)} caracteres")