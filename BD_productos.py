class productos:
   
    indice=0
   
    def busqueda_de_producto(self):
        productos=[["Carretilla       ",40.00],
        ["Pala             ",08.99],
        ["Tornillos        ",00.99]
        ,["Pintura          ",09.50]
        ,["Alicate          ",03.45]
        ,["Cemento          ",09.00]
        ,["Carreola 12 pies ",14.00]
        ,["Carreola 10 pies ",10.00]
        ,["Martillo         ",05.99]
        ,["Clavos           ",01.00]
        ,["Arena            ",00.65]
        ,["Piedra           ",00.60]
        ,["Puerta           ",35.00]
        ,["Tablilla         ",08.00]
        ,["Alambre Dulce    ",01.00]
        ,["Palaustre        ",03.00]
        ,["Lija             ",01.00]
        ,["Nivel            ",05.00]
        ,["Cinta métrica    ",05.00]
        ,["LLana            ",06.00]
        ,["Flota            ",04.00]
        ]
        z=0
        codigos=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        indice=0
        salir=0
        productos_buscados=[None]*30
        subtotal=0
        A=""
        while salir!=2:
            buscador=int(input("Ingrese el valor del código de producto :"))
            if buscador in codigos:
                z=codigos.index(buscador)
                print("El producto es ",productos[z][0]," =",productos[z][1])
                cantidad=int(input("Ingrese la Cantidad del producto :"))
                #productos_buscados[indice]=[str(productos[z][0]),str(cantidad),"",str(productos[z][1]*cantidad)]
                productos_buscados[indice]=[str(cantidad)+"  "+str(productos[z][0])+"{:^10}".format(str(round(productos[z][1],2)))+"  "+str(round((productos[z][1]*cantidad),2))]
                indice+=1
                subtotal=subtotal+(productos[z][1]*cantidad)
            salir=int(input("1-Seguir____2-Salir :"))
            #Fin While 
        for i in range(len(productos_buscados)):
            if(productos_buscados[i]!= None):
                 string_encontrados = str(productos_buscados[i]) 
                 #eu="".join([str(_) for _ in encontrados[i]])
                 A=A+("\n"+string_encontrados)
                 
        return A,subtotal
        

##Practicando
# 
# 
# 
# 
#  
#obj=productos()
#encontrados,subtotal=obj.busqueda_de_producto()
#print(encontrados)
#print("El subtotal",subtotal)
#acum=0
#A="Factura"
#def convertTuple(tup): 
  #  str =  ''.join(tup) 
 #   return str
  
#for i in range(len(encontrados)):
   # if(encontrados[i]!= None):
    #    string_encontrados = str(encontrados[i]) 
     #   #eu="".join([str(_) for _ in encontrados[i]])
      #  A=A+("\n"+string_encontrados)
    

#print(A)


#print(encontrados)
'''
while(encontrados[acum]!=None):
    
    print(encontrados[acum],"//")
    acum=+1
v_econtrados=[None]*acum
i=0
while(encontrados[i]!=None):
   
    v_econtrados[i]=encontrados[i]
    i=+1
print("Mi arreglo a enviar es: ",v_econtrados)
'''



    

