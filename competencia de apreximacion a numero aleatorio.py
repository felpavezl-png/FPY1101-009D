from random import randint

numero=int(input("Ingrese un numero del 1 al 100: "))
competencia=randint(1,100)
print("tu rival escogio",competencia)
meta=randint(1,100)

num1=numero-meta
num2=competencia-meta

if abs(num1)>abs(num2):
    print("el numero era", meta, "el mas cercano es:",competencia)
elif abs(num1)<abs(num2):
    print("el numero era", meta, "el mas cercano es:",numero)
else:
    print("los numeros estan a la misma distancia de:",meta)