import xml.etree.ElementTree as ET

def leerXML2(ruta):
    tree = ET.parse(ruta)
    print(tree)
    root = tree.getroot()

    for piso in root.findall('piso'):
        nombre = piso.attrib
        print(str(nombre['nombre']))
        columnas = piso.find('C').text
        filas = piso.find('R').text
        voltear = piso.find('F').text
        intercambiar = piso.find('S').text

        patrones = piso.find('patrones')
        patron_inicial = patrones[0].text
        patron_final = patrones[1].text
        patron_inicial = patron_inicial.replace('\n', '')
        patron_final = patron_final.replace('\n', '')
        

        print(f'\tColumnas:\t\t{columnas}\n\tFilas:\t\t\t{filas}\n\tPrecio voltear\t\t{voltear}\n\tPrecio intercambiar:\t{intercambiar}')
        print(f'\tPatron inicial:\t\t{patron_inicial}')
        print(f'\tPatron iinal:\t\t{patron_final}')


