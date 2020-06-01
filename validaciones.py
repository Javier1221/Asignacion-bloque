class PaymentGateway:
    def do_sale(self,tipo_transaccion):
        type_ = " "
        if(tipo_transaccion == "auth"):
            type_ = 1
        elif(tipo_transaccion == "capture"):
            type_ = 2
        elif(tipo_transaccion == "sale"):
            type_ = 3   
        elif(type_ != 1 or type_ != 2 or type_ !=3 ):
            type_ = "Error 50 \n Esto no es una transacción permitida" 
        
        return type_
    
    monto = 0
    def validacion_monto(self,dinero_ingresado):
        if(dinero_ingresado > 1 and dinero_ingresado < 150000):
            monto = 1 
        else:    
            monto = 0
        return monto
    
    def tarjeta_Credito(self,tarjeta):
        
        if(tarjeta[0] == "4"):
            tipo_T = "Visa"           
        elif(tarjeta[0] == "5"):
            tipo_T = "MasterCard"            
        elif(tarjeta[0] == "6"):
            tipo_T = "American Express"         
        elif(tarjeta[0] != "4" or tarjeta[0] != "5" or tarjeta[0] != "6"):
            tipo_T = "Error 500\n Esta no es una tarjeta permitida"
     
        return tipo_T
