""" Programa que recibe dos parámetros: un fichero de texto y una cadena que le indica qué información va extraer del
 mismo, después muestra por la pantalla los datos extraídos.

Los posibles valores del segundo parámetro y la información que extrae es:

DNI: extrae los DNIs.
IP: extrae las direcciones IP.
MAT: extrae matrículas de coche con formato 0000XXX.
HEX: extrae números hexadecimales. Entendemos que las letras entre A y F son en mayúsculas y el número empieza con #.
FEC: extrae fechas con formato dd/mm/aaaa.
TWT: extrae usuarios de twitter: empieza por @ y puede contener letras mayusculas y minusculas, numeros, guiones y
 guiones bajos.
El programa tiene que ser en relación a su complejidad y número de líneas lo más eficiente posible.

Autor: Angel Fernández Ariza
Fecha: 2022-2023
"""
import re

def extraer_datos(archivo, tipo):
    try:
        expresiones_reg = {
            'DNI': r'\d{8}[A-HJ-NP-TV-Z]',
            'IP': r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b',
            'MAT': r'\d{4}[A-Z]{3}',
            'HEX': r'#[0-9A-F]+',
            'FEC': r'\d{2}/\d{2}/\d{4}',
            'TWT': r'@\w+'
        }

        with open(archivo, 'r') as archivo:
            contenido = archivo.read()
            contenido_encontrado = re.findall(expresiones_reg[tipo], contenido)
            for i in contenido_encontrado:
                print(i)
    except KeyError:
        return "Valor introducido no válido"
    except FileNotFoundError:
        return "El archivo introducido no existe o no se ha encontrado"

