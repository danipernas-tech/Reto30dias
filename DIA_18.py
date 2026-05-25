
frase = input("Dime una frase: ")

def borde (frase):
    for i in range (len(frase) + 4):
        print("*", end="")
    print()

borde(frase)
print(f"* {frase} *")
borde(frase)


