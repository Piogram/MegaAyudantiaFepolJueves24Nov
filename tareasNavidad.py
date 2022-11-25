tareas = [
    "pintar soldados", 
    "hornear galletas", 
    "armar muñecos", 
    "cortar papel de regalo"
    ]
inicio = [678, 800, 240, 423]
duracion = [300, 900, 456, 112]
fin = []
#fin:  [978, 1700, 696, 535]
for i in range(len(tareas)): #0
    minIni = inicio[i] #678
    minDuracion= duracion[i] #300
    minFin = minIni + minDuracion
    fin.append(minFin)

# print('fin: ', fin);
#fin:  [978, 1700, 696, 535]
finCumplen= []
for minuto in fin: #978
    if minuto <= 1440:
        finCumplen.append(minuto)

#[978, 696, 535]
finCumplen.sort()
#[535, 696, 978]
cont=1
print("Tareas del Día")
for minuto in finCumplen: #535
    index = fin.index(minuto) # 3
    tarea = tareas[index]
    print("{}. {}".format(cont,tarea))
    cont+=1 #cont = cont + 1






