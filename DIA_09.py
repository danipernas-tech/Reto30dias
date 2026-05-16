
frase = input("Dime una frase: ")
caracteres = 0
espacios = 0
vocales = 0
consonantes = 0
#lista_vocales = ["a", "e", "i", "o", "u"]
vocal_a = 0
vocal_e = 0
vocal_i = 0
vocal_o = 0
vocal_u = 0

for i in frase.lower():
    caracteres += 1
    if i == " ":
        espacios += 1
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vocales += 1
        if i == "a": 
            vocal_a += 1
        if i == "e": 
            vocal_e += 1
        if i == "i": 
            vocal_i += 1
        if i == "o": 
            vocal_o += 1
        if i == "u": 
            vocal_u += 1
    if  i != "a" and i != "e" and i != "i" and i != "o" and i != "u" and i != " ":
        consonantes += 1
print(f"\nCaracteres: {caracteres}")
print(f"Espacios: {espacios}")
print(f"Vocales: {vocales}")
if vocal_a > 0:
    print(f"    -Vocal a: {vocal_a} veces")
if vocal_e > 0:
    print(f"    -Vocal e: {vocal_e} veces")
if vocal_i > 0:
    print(f"    -Vocal i: {vocal_i} veces")
if vocal_o > 0:
    print(f"    -Vocal o: {vocal_o} veces")
if vocal_u > 0:
    print(f"    -Vocal u: {vocal_u} veces")
print(f"Consonantes: {consonantes}")
print(f"Frase invertida: {frase[::-1]}")
if frase == frase[::-1]:
    print("Es un palindromo simple")