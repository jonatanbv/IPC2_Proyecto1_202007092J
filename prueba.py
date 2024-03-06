patron1 = 'NBNBNB'
patron2 = 'NNNBBB'
filas = 2
columnas = 3
length= len(patron1) - 1


for i in range(length):
    for j in range(length):
        if patron2[j]!=patron1[j]:
            print(patron1[j])
            if patron1[j+1]==patron2[j+1]:
                print('intercambiar')
            else:
                
            
                

