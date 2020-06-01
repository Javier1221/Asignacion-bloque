from generador_qr import qr_generador as generador #Si desea generar un codigo Qr de la factura 
from BD_productos import productos as Busqueda 
from impresiones import Imprimir as Imprimir
from pasarela import pasarela 
import os

class facturacion:
    
    def facturar(self):
        cliente=""
        numero_factura=+1
        cliente=input("Ingrese Nombre del cliente :")
        numero_telefono=input("Número de contacto :")
        descripcion_productos,subtotal=Busqueda.busqueda_de_producto(1)
        ITBMS=subtotal*0.07
        descuento=0
        cotizacion=int(input("Ha realizado cotización 1(Sí) 2(No): "))
        if(cotizacion==1):
            if(subtotal>=100 and subtotal<200):
              descuento=subtotal*0.10
            elif(subtotal>=200 and subtotal<600):
              descuento=subtotal*0.15
        elif(cotizacion==2):
            descuento=0
        monto=(subtotal-descuento)+ITBMS
        factura=Imprimir.generarFA(1,descripcion_productos,subtotal,numero_factura,cliente,ITBMS,descuento)
        print(factura)
        P1=pasarela(monto)
        pago=P1.tipos_de_pago()
        print(pago)
        Recibo=Imprimir.generarCR(1,descripcion_productos,subtotal,numero_factura,cliente,ITBMS,descuento)
        print(Recibo)


######## Realización de la Cotización ###########    
class Cotizacion:
    def cotizacion(self):
        acumulador=+1
        cliente=""
        facturar=0
        descuento=0
        cliente=input("Ingrese Nombre del cliente :")
        numero_telefono=input("Número de contacto :")
        descripcion_productos,subtotal=Busqueda.busqueda_de_producto(1)
        cotizado=Imprimir.generarCo(1,descripcion_productos,subtotal,acumulador,cliente,numero_telefono)
        print(cotizado)
        facturar=int(input("Desea realizar el pago 1(Sí)      2(No) :"))
        if(facturar==1):
          if(subtotal>=100 and subtotal<200):
              descuento=subtotal*0.10
          elif(subtotal>=200 and subtotal<600):
              descuento=subtotal*0.15
          ITBMS=subtotal*0.07
          monto=(subtotal-descuento)+ITBMS
          factura=Imprimir.generarFA(1,descripcion_productos,subtotal,acumulador,cliente,ITBMS,descuento)
          print(factura)
          P1=pasarela(monto)
          pago=P1.tipos_de_pago()
          print(pago)
          Recibo=Imprimir.generarCR(1,descripcion_productos,subtotal,acumulador,cliente,ITBMS,descuento)
          print(Recibo)
        elif(facturar==2):
            print("Cotización Finalizada")

        


##Iniciando el programa 
if __name__ == "__main__":
   menu=0
   factura=facturacion()
   cotizar=Cotizacion()
  
   while(menu!=3):
       print("\n\nFERRETERIA GRAN ALMACEN\n__________________")
       menu=int(input("|1-Cotización    |\n|2-Facturar      |\n|3-Salir         |\n|________________|\n="))
       
       if(menu==1):
           os.system("cls")
           print("\n Proceso de Cotización")
           cotizar.cotizacion()
       elif(menu==2):
           os.system("cls")
           print("\n Proceso de Facturación ")
           factura.facturar()
       elif(menu==3):
            menu=3
   print("Ya la valiste")









        
        



       
        



