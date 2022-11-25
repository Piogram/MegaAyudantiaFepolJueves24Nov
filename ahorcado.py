import random as rd
#Modulo random Piogram
palabras=["Axell","Piogram",
    "David","Gabriela", "Andres",
    "Capuchino","Fernando"]
secreto = rd.choice(palabras).lower()
print("secreto:",secreto)
vocales="aeiou"
letra = rd.choice(secreto)
while letra not in vocales:
    letra = rd.choice(secreto)
print("Letra:", letra)

pista=[]
for caracter in secreto:
    if caracter != letra:
        pista.append("-")
    else:
        pista.append(letra)

turnos= 2 * len(secreto)  #10
while turnos!=0 and "".join(pista) != secreto:
    print("".join(pista))
    adivina = input("Ingrese una letra: ").lower()#E
    if adivina in secreto:
        for i in range(len(secreto)):#ESPOLE
            letraSecreto = secreto[i] #E
            if adivina == letraSecreto:
                #E--O-E
                pista[i] = adivina
    turnos-=1   #turnos = turnos - 1   

if "".join(pista) == secreto:
    print("Ganó")
else:
    print("Perdió")

empleo= (2 * len(secreto)) - turnos
print("Turnos que empleó:",empleo )





        




