from reportlab.platypus import (Table, TableStyle)
from reportlab.lib import colors
from reportlab.pdfgen import canvas


def informeFactura(clien, produ):
    informe = canvas.Canvas("Factura" + clien[0][0] + ".pdf")

    estiloTexto = informe.beginText()
    estiloTexto.setFont("Times-Bold", 16)
    estiloTexto.setTextOrigin(100, 800)

    suma = 0

    cadena = "Factura para " + clien[0][1] + " con DNI: " + clien[0][0] + "."

    estiloTexto.textLines(cadena)
    estiloTexto.moveCursor(10, 50)

    estiloTexto.setFont("Times-Roman", 12)

    guion = ["Socio: " + clien[0][1] + " " + clien[0][2] + " con CodBarras: " + clien[0][6] + " ."]

    datos = [["Codigo Barras Producto", "CodBarrasPelicula", "Nombre", "Precio", "Tipo", "Procedencia", "Año Publicacion"]]

    datos.append(["1214","2145","Juan","25€","DVD","Usado","2004"])


    tabla = Table(datos, colWidths=85, rowHeights=30)
    tabla.setStyle(TableStyle(
        [
            ('BACKGROUND', (0, 0), (-1, 0), colors.black),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('BOX', (0, 0), (-1, -1), 1, colors.black),
            ('INNERGRID', (0, 0), (-1, -1), 1, colors.grey),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]
    ))

    for linha in guion:
        estiloTexto.textOut(linha)
    estiloTexto.moveCursor(0, 15)

    estiloTexto.setFillGray(0.5)

    estiloTexto.setFont("Times-Bold", 16)
    cadena2 = "Precio total a pagar: " + str(suma) + "€"
    estiloTexto.textLines(cadena2)
    estiloTexto.moveCursor(10, 50)

    informe.drawText(estiloTexto)
    tabla.wrap(10, 50)
    tabla.drawOn(informe, 0, 550)
    informe.showPage()
    informe.save()
