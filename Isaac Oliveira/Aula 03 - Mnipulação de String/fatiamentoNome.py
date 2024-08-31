nome_completo = "Isaac Rafael de Oliveira"
primeiro_nome = nome_completo[:5]
ultimo_nome = nome_completo[15:]
sobrenome = nome_completo[-9:]
print(f"Meu primeiro nome é {primeiro_nome}")
print(ultimo_nome)
print (f"Meu último nome é {sobrenome}")

#quantidade de caracteres do meu nome
qtd_char = len(nome_completo)
print(f"O meu nome tem {qtd_char} caracteres")

#quantidade de letra "a" no meu nome
letra = "a"
qtd_letras_a = nome_completo.count(letra)
print(f"O meu nome tem {qtd_letras_a} letras {letra}")

#Aonde inicia meu último nome
palavra = "Oliveira"
nome_posição = nome_completo.find(palavra)
print(f"Meu último nome {palavra} se inicia na posição {nome_posição}")

#Verificar se existe os seguintes sobrenomes: Silva, Souza, Santos
verifica_nome = sobrenome in nome_completo or "Silva" or "Souza" or "Santos" in nome_completo
print(f"O meu sobrenome {sobrenome} está no texto? {verifica_nome}")
