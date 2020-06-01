class Imprimir:
    def generarFA(self,a1,b,c,cliente,ITBMS,Descuento):
        division="_________________________________________________________________"
        return ("\n"+division+"\nFerreteria el gran Almacen    FA000"+str(c)+"\nRuc:qw123        DV:1200    Telefono:236-7000\nCliente: "+cliente+
        "\nCant      Desc.         P.Uni     P.total"+str(a1)+"\n*Subtotal----------"+str(b)+
        "\nItmbs----------"+str(round(ITBMS,2))+"\nDescuento----------"+str(round(Descuento,2))+"\nTotal:"+str(round(((b-Descuento)+ITBMS),2))+"\n"+division)
    
    def generarCo(self,a1,b,c,cliente,numeroTel):
        division="_________________________________________________________________"
        return ("\n"+division+"\nFerreteria el gran Almacen    CO000"+str(c)+"\nRuc:qw123        DV:1200    Telefono:236-7000\nCliente: "+cliente+
        "  Telefon de Repaldo:"+numeroTel+"\nCant      Desc.         P.Uni     P.total"+str(a1)+"\n*Subtotal---------------------"+str(b)+
        "\n"+division)
    
    def generarCR(self,a1,b,c,cliente,ITBMS,Descuento):
        division="_________________________________________________________________"
        return ("\n"+division+"\nFerreteria el gran Almacen    CR000"+str(c)+"\nRuc:qw123        DV:1200    Telefono:236-7000\nCliente: "+cliente+
        "\nCant      Desc.         P.Uni     P.total"+str(a1)+"\n*Subtotal----------"+str(b)+
        "\nItmbs----------"+str(round(ITBMS,2))+"\nDescuento----------"+str(round(Descuento,2))+"\nTotal:"+str(round(((b-Descuento)+ITBMS),2))+"\n"+division)
    

