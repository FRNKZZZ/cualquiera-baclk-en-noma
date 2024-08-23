print("HELLO WORLD")

nnotas=(int(input("Ingrese numero de notas a promediar")))
sumanotas=0

print("HELLO WORLD")

for i in range(0,nnotas):
    nota=(float(input("Ingrese nota")))
    sumanotas=sumanotas+nota

Nfinal=sumanotas/nnotas
print("Nota final: ",Nfinal)

if Nfinal>3.9:
    print("HELLO WORLD")
    print("Usted esta aprovado")
else:
    print("HELLO WORLD")
    print("Usted esta desaprovado")