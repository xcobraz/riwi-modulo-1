"""
Una tienda ofrece un descuento del 15% bajo estas condiciones:

    El cliente debe gastar más de $100 en su compra.

    Además, debe cumplir al menos una de estas opciones:

        Ser miembro del programa de fidelidad o

        No gastar más de $200 (para evitar combinar descuentos)

Si no se cumplen estas condiciones, no se aplicará ningún descuento.
"""

# Variables
es_miembro = True
total_compra = 120

# Operadores lógicos y not
#se cambio un and por or y un or por and ademas el simbolo > estaba al reves se cambio por un <
if total_compra > 100 and (es_miembro==True or  total_compra < 200):
    print("Descuento del 15% aplicado 🎉")
else:
    print("Sin descuento 😢")