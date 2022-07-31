import logging

def main():
    
    #Configuración:
    logging.basicConfig(filename="app.log", level="DEBUG")
    
    #Variables utilizadas:
    datos_bibliotecas= ""

    
    
    #Información de diagnostico:
    
    logging.error("El archivo ya fue creado, borrarlo si se desea ejecutar de neuvo el programa.", datos_bibliotecas)
    logging.info("Los archivos se han creado con éxito.")
    
if __name__=="__main__":
    main()