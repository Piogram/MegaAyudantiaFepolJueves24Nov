L = [ 'ATTTGCTTGCTATTTAAACCGGTTATGCATAGCGC','ATTTGCTTGCTATTTAAACCGGTTATGCATAGC', 'ATTAGCCGCTATCGA' ]
R = 'CG'

for S in L: #'ATTTGCTTGCTATTTAAACCGGTTATGCATAGCGC'
    inv = S[::-1]
    mitadIndex = len(inv) // 2
    segundaMitad = inv[mitadIndex:]
    contRMitad= segundaMitad.count(R)
    contTodo = inv.count(R)
    # print("segundaMitad:",segundaMitad)
    
    if contRMitad==2 and contTodo>=3 :
        print("Secuencia:", S)
        indexBusqueda = 0
        posiciones=[]
        for i in range(contTodo):
            index = inv.index(R,indexBusqueda)
            # print("index",index)
            posiciones.append(index)
            indexBusqueda= index + len(R)
        print("Indices:",posiciones)
    #CGCGATACGTATTGGCCAAATTTATCGTTCGTTTACG








        












