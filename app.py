
list1 = ["abc","34","verdad","40","male"]

datoabuscar = str(input("Favor digitar el dato a buscar: "))

'''
Realizar una función recursiva que permita
identificar si exite el dato a buscar
'''

def recurso (datoabuscar):
    if datoabuscar == 0:
        return False
    else:
        return datoabuscar in list1

print(recurso(datoabuscar))



      
