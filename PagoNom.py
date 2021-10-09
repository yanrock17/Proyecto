from datetime import datetime 
import os 


#reinvertimos la fecha
def inv_fecha(fech):
    fechn = datetime.strptime(fech,'%d/%m/%Y')
    return datetime.strftime(fechn,'%Y-%m-%d')

#se hace el calculo del Bono1 y Bono2
def pagar(basesueldo,h,v1,v2):
    
    if int(h) <= 5:
        SuelNu= float(basesueldo) + float(basesueldo) / 0.05 * float(v1)
    else:
        SuelNu= float(basesueldo) + float(basesueldo) / 1.5 * float(v2)
    return float(SuelNu)

#datos a solicitar para calcular los bonos segun horas extras semanales
B1= input('Intoduzca Bono General:')
B2 = input('Intoduzca Bono Eficiencia:')


fichero= open("Pago_Nom.py", "w")

#Leeo el archivo txt
with open("Pago.txt", "r") as pago:
    for linea in pago:

        campo = linea.split()

        
        if campo[0].isdigit():
            fech = inv_fecha(campo[1])
            sueld = pagar(campo[4].replace("$",""),campo[5],B1,B2)
        else:
            fech = campo[1]
            sueld = campo[3]

        
      
        fichero.write(campo[0]+" ")
        fichero.write(fech+" ")
        fichero.write(campo[2]+" ")
        fichero.write(campo[3]+" ")
        fichero.write(campo[4]+" ")
        

       
        if campo[0].isdigit():
            fichero.write(campo[5]+" ")
            fichero.write(str(sueld))
            fichero.write(os.linesep)
        else:
            fichero.write(os.linesep)
           
        

    fichero.close()





