class Piso:
    def __init__(self,nombre, columnas, filas, precio_voltear, precio_intercambiar, patron_actual, patron_final):
        self.nombre = nombre
        self.columnas = columnas
        self.filas = filas
        self.precio_voltear = precio_voltear
        self.precio_intercambiar = precio_intercambiar
        self.patron_actual = patron_actual
        self.patron_final = patron_final
        self.siguiente = None


    def mostrar_informacion_pisos(self):
        print(f'Nombre: {self.nombre}\n\tColumnas:\t\t{self.columnas}\n\tFilas:\t\t\t{self.filas}\n\tPrecio Voltear:\t\t{self.precio_voltear}\n\tPrecio intercambiar:\t{self.precio_intercambiar}\n\tPatron actual:\t\t{self.patron_actual}\n\tPatron final:\t\t{self.patron_final}')



class Lista_pisos:
    def __init__(self):
        self.primer_nodo = None
    
    def insertar_piso(self, nombre, columnas, filas, precio_voltear, precio_intercambiar, patron_actual, patron_final):
        nuevo_nodo = Piso(nombre, columnas, filas, precio_voltear, precio_intercambiar, patron_actual, patron_final)
        nuevo_nodo.siguiente = self.primer_nodo
        self.primer_nodo = nuevo_nodo

    def mejor_precio(self):
        actual = self.primer_nodo
        while actual:
            if actual.precio_intercambiar>actual.precio_voltear:
                print(f'Para: {actual.nombre} es mejor usar voltear\nPrecio intercambiar: {actual.precio_intercambiar} Precio voltear{actual.precio_voltear}')
            elif actual.precio_intercambiar==actual.precio_voltear:
                print(f'Para: {actual.nombre} se pueden usar ambos metodos\nPrecio intercambiar: {actual.precio_intercambiar} Precio voltear{actual.precio_voltear}')
            else:
                print(f'Para: {actual.nombre} es mejor usar intercambiar\nPrecio intercambiar: {actual.precio_intercambiar} Precio voltear{actual.precio_voltear}')
            actual=actual.siguiente



    def mostrar_pisos(self):
        actual = self.primer_nodo
        while actual:
            actual.mostrar_informacion_pisos()
            actual= actual.siguiente
   
