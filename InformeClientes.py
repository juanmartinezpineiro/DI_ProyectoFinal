
from reportlab.pdfgen import canvas
import webbrowser as wb

def informeCliente(clien):
    """
    Descripcion


    """
    informe=canvas.Canvas("InformedoCliente"+clien[0][0]+".pdf")

    estiloTexto=informe.beginText()
    estiloTexto.setFont("Times-Bold", 16)
    estiloTexto.setTextOrigin(100,800)



    cadena="Informe sobre la información basica del cliente con DNI: "+clien[0][0]+"."

    estiloTexto.textLines(cadena)
    estiloTexto.moveCursor(10, 50)

    estiloTexto.setFont("Times-Roman",12)

    guion = ["El socio " + clien[0][1] +" "+clien[0][2]+ ",tiene  un "+clien[0][3]+" titulado "+clien[0][7],
             "con código de barras "+clien[0][5]+" publicado en "+clien[0][6]]
    wb.open_new("./")



    for linha in guion:
        estiloTexto.textOut(linha)
        estiloTexto.moveCursor(0,15)

    estiloTexto.setFillGray(0.5)
    informe.drawText(estiloTexto)
    informe.showPage()
    informe.save()



