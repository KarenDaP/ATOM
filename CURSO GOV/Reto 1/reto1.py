from ast import If


hemoglobina=float(input())
genero=int(input())

if(genero==1):
    if(hemoglobina>=0 and hemoglobina<13.2):
        print('Alerta 1')
    elif(hemoglobina>=13.2 and hemoglobina<16.6):
        print('Sin alerta')
    elif(hemoglobina>=16.6):
        print('Alerta 2')
else: 
    if(genero==2):
        if(hemoglobina>=0 and hemoglobina<11.6):
            print('Alerta 1')
        elif(hemoglobina>=11.6 and hemoglobina<15):
            print('Sin alerta')
        elif(hemoglobina>=15):
            print('Alerta 2')
    else:
        print('No es posible generar la alerta')        