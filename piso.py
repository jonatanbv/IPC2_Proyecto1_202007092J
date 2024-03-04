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
        self.anterior = None

    def mostrar_informacion_pisos(self):
        print(f'Nombre: {self.nombre}\nColumnas: {self.columnas}\nFilas: {self.filas}\nPrecio Voltear: {self.precio_voltear}')
        print(f'Precio intercambiar: {self.precio_intercambiar}\nPatron actual: {self.patron_actual}\nPatron final: {self.patron_final}')



class Lista_pisos:
    def __init__(self):
        self.head = None

    def agregar_piso(self, nombre, columnas, filas, precio_voltear, precio_intercambiar, patron_actual, patron_final):
        new_nodo = Piso(nombre, columnas, filas, precio_voltear, precio_intercambiar, patron_actual, patron_final)
        if self.head is None:
            self.head = new_nodo
            return 
        last_nodo = self.head
        while last_nodo.siguiente:
            last_nodo = last_nodo.siguiente
        last_nodo.siguiente = new_nodo
        new_nodo.anterior = last_nodo

    def anteponer_piso(self, nombre, columnas, filas, precio_voltear, precio_intercambiar, patron_actual, patron_final):
        new_nodo = Piso(nombre, columnas, filas, precio_voltear, precio_intercambiar, patron_actual, patron_final)
