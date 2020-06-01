from principal_pasarela import pasarela_first
#Aqui viene la pasarela
class pasarela:

    def __init__(self,monto):
        print("10-Efectivo\n11-Cheque\n12-Tarjeta en sitio\n13- Tarjeta en línea")
        self.metodo_de_pago=int(input("Indique el metodo de pago"))
        self.monto=monto
    
    def tipos_de_pago(self):
        if(self.metodo_de_pago==10):
            loop=0
            while(loop!=1):
                ingreso=float(input("Ingrese la cantidad : "))
                if(ingreso<self.monto):
                    print("Nuevamente...")
                    loop=0
                elif(ingreso>=self.monto):
                    loop=1
                    cambio=ingreso-self.monto
            return "Su cambio es ",cambio
        elif(self.metodo_de_pago==11):
            cantidad_cheque=input("Ingrese la cantidad de cheque :")
            return "Cheque aceptado correctamente"
        elif(self.metodo_de_pago==12):
            print("Pase la Tarjeta")
            return "Tarjeta Validada exitosamente"
        elif(self.metodo_de_pago==13):
            pasarela_first(1)
            return "Pago Validado Correctamente"
    
  
    
    




            


