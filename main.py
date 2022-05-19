pizza=input("¡desea que su pizza sea vegetariana  o normal?:")
print("la pizza viene con mozarrela y tomate")
v="vegetariana"
nv="normal"
if pizza==v:
    print("su pizza vegetariana tiene para agregar: pimiento y tofu")
    ingredientes=input("ingrese que ingrediente desea:")
    print(f" su pizza es  {v} con {ingredientes}")
elif pizza==nv:
    print("su pizza normal tiene para agregar: ")
    ingredientes = input("ingrese que ingrediente desea:")
    print(f" su pizza es  {nv} con {ingredientes}")
else:
    print("lo que ingreso no es correcto")





