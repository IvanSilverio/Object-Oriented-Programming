import os
#import datetime


#print (os.listdir ("arquivos"))
#print (datetime.date.today())

lista_arquivos = os.listdir ("arquivos")

for arquivo in lista_arquivos:

    if ".txt" in arquivo:
        if '22' in arquivo:
            os.rename (f"arquivos/{arquivo}", f"arquivos/22/{arquivo}")
            print ("Movimentar para a pasta 22")

        elif '23' in arquivo:
            os.rename (f"arquivos/{arquivo}", f"arquivos/23/{arquivo}")
            print ("Movimentar para a pasta 23")
        