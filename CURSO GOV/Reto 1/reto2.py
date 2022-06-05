numeroPacientes=int(input("Ingrese numero de pacientes: "))
pacientesLeidos=0
mujeresAlerta1=0
mujeresAlerta2=0
mujeresSinAlerta=0
hombresAlerta1=0
hombresAlerta2=0
hombresSinAlerta=0

while(pacientesLeidos!=numeroPacientes):
    hemoglobina=float(input("Ingrese hemoglobina: "))
    genero=int(input("Ingrese genero: "))
    while(genero!=1 and genero!=2):
        genero=int(input("Ingrese genero: "))
    if(genero==1):
        if(hemoglobina>=0 and hemoglobina<13.2):
            mujeresAlerta1+=1
        elif(hemoglobina>=13.2 and hemoglobina<16.6):
            mujeresSinAlerta+=1
        elif(hemoglobina>=16.6):
            mujeresAlerta2+=1
    else: 
        if(genero==2):
            if(hemoglobina>=0 and hemoglobina<11.6):
                hombresAlerta1+=1
            elif(hemoglobina>=11.6 and hemoglobina<15):
                hombresSinAlerta+=1
            elif(hemoglobina>=15):
                hombresAlerta2+=1
    pacientesLeidos+=1
    
print(mujeresAlerta1)
print(mujeresAlerta2)
print(mujeresSinAlerta)
print(hombresAlerta1)
print(hombresAlerta2)
print(hombresSinAlerta)

