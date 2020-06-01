from validaciones import PaymentGateway as PaymentG
import os

def pasarela_first(self):
    "Validación de tipo de transaccion "
    vad1 = False
    while(vad1 != "true"):
    
        transaccion=input("Ingrese el tipo de Transaccion: ")
        validacion = PaymentG.do_sale(0,transaccion)
        if(validacion == 1 or validacion == 2 or validacion == 3):
            vad1 = True
            break
        else:
            os.system("cls")
            print(validacion)
            print("Nuevamente")
            vad1 = False
    vad2 = False
    while(vad2 != "true"):
        monto=float(input("Ingrese el monto de la transacción "))
        validacion_2 = PaymentG.validacion_monto(0,monto)
        if(validacion_2 == 1):
         vad2 = True
         break
        else:
            os.system("cls")
            print("Valor de transacción fuera de rango ingrese nuevamente")
            print("Nuevamente")
            vad2 = False

    vad3 = False
    while(vad3 != "True"):
        tarjeta_ingresada=input("Ingrese la tarjeta de Crédito ")
        tarjeta=PaymentG.tarjeta_Credito(0,tarjeta_ingresada)
        if(tarjeta == "Visa" or tarjeta == "MasterCard" or tarjeta == "American Express"):
         vad3 = True
         break
        else:
            os.system("cls")
            print("error500\nEsta no es una tarjeta permitida")
            print("Nuevamente")
            vad3 = False
       
    print("Retorno ",validacion,"---Tipo de Tarjeta ",tarjeta)


