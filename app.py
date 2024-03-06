import xml.etree.ElementTree as ET
from piso import*


lista_pisos_registrados = Lista_pisos()



def leerXML2(ruta):
    tree = ET.parse(ruta)
    print(tree)
    root = tree.getroot()

    for piso in root.findall('piso'):
        nombre = piso.attrib
        nombre = str(nombre['nombre'])
        columnas = piso.find('C').text
        filas = piso.find('R').text
        voltear = piso.find('F').text
        intercambiar = piso.find('S').text

        patrones = piso.find('patrones')
        patron_inicial = patrones[0].text
        patron_final = patrones[1].text
        patron_inicial = patron_inicial.replace('\n', '')
        patron_final = patron_final.replace('\n', '')

        lista_pisos_registrados.insertar_piso(nombre, columnas,filas, voltear, intercambiar, patron_inicial, patron_final)

 #------------------------ GENERADOR GRAPHIVZ-----------------------   
def generarTablaGraphviz(archivo, columna, fila, patron):
    for i in range(fila):
        archivo.write("<TR>")
        for j in range(columna):
            color = ''
            if patron[i+j]=='N':
                color='black'
            else:
                color='White'
            archivo.write(f'<TD bgcolor="{color}" border="1">   </TD>')
                
        archivo.write('</TR>')




def generarGraphviz(ruta, columna, fila, patron):

    with open(ruta, 'w') as archivo:
        archivo.write("""digraph G{
fontname="Helvetica,Arial,sans-serif"
node [fontname="Helvetica,Arial,sans-serif"]
edge [fontname="Helvetica,Arial,sans-serif"]

a0 [shape=none label=<""")
        
        archivo.write('<TABLE border="0" cellspacing="10" cellpadding="10">')

        generarTablaGraphviz(archivo, columna, fila, patron)
        
        archivo.write('</TABLE>')
        archivo.write(""">];

LKD [
		fontsize = 20,
		label = "lable",
		shape = plain,
		style = ""]

        
}""")
        


generarGraphviz('tablas.dot', 4, 3, 'BNNNBBBNNNB')


 #------------------------ GENERADOR GRAPHIVZ-----------------------   



        
def voltear_piso():
    print('se voltero un piso')

def intercambiar_piso():
    print('se intercambio un piso')

def definir_cadena(patron_inicial, patron_final):

    negro_inicio = 0
    negro_final = 0

    for inicio in patron_inicial:
        if inicio == 'N':
            negro_inicio=negro_inicio+1
    for final in patron_final:
        if final == 'N':
            negro_final=negro_final+1

    if negro_final==negro_inicio:
        print('se puede usar intercambiar sin necesidad de voltear')









leerXML2('pisos.xml')
lista_pisos_registrados.mostrar_pisos()
lista_pisos_registrados.mejor_precio()
        

        


