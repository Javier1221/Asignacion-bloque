import qrcode
from PIL import Image
class qr_generador:
    def generarFA(self,a1,b,c,cliente,ITBMS):
        c=c
        qr=qrcode.make("\tFactura #000"+str(c)+"FA\nRuc:qw123        DV:1200    Telefono:236-7000\nCliente: "+cliente+
        "\n*Descripción"+str(a1)+"\n*Subtotal---------------------"+str(b)+"\nItmbs-------------"+str(ITBMS)+
        "\nDescuento--------------aun\nTotal:-------------------"+str(b-ITBMS))
        a="factura_000"+str(c)+".png"
        nombre_imagen = open(a, 'wb')
        qr.save(nombre_imagen)
        return "\tFactura #000"+str(c)+"FA\nRuc:qw123        DV:1200    Telefono:236-7000\nCliente: "+cliente+"\n*Descripción"+str(a1)+"\n*Subtotal---------------------"+str(b)+"Itmbs-------------"+str(ITBMS)+"Descuento--------------aun\nTotal:"+str(b-ITBMS)
    
    def generarCo(self,a1,b,c,cliente):
        c=c
        qr=qrcode.make("\tCotización #000"+str(c)+"CO\nRuc:qw123        DV:1200    Telefono:236-7000\nCliente: "+cliente+"\n*Descripción"+str(a1)+"\n*Subtotal--------------------"+str(b))
        a="cotizacion_000"+str(c)+".png"
        nombre_imagen = open(a, 'wb')
        qr.save(nombre_imagen)
        return "\tCotización #000"+str(c)+"CO\nRuc:qw123        DV:1200    Telefono:236-7000\nCliente: "+cliente+"\n*Descripción"+str(a1)+"\n*Subtotal--------------------"+str(b)



    

