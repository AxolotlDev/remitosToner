# Este es un pequeño proyecto de programa para leer los remitos PDF de entrega de toners, 
# creando un txt donde se encuentre la informacion para generar el ticket de cambio para 
# el mismo.
# A futuro la idea es automatizar el programa para que rellene los campos dentro de la aplicacion web de tickets.

import fitz


print("Ingrese el número de Remito y presione Enter.");
remito = input();
pdfRemito = remito + ".pdf";

