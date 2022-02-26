nivelAgua = int(input("Digita la cantidad de agua de la represa: "))
print(f"la cantidad de agua es {nivelAgua}")

print("hola mundo")

if(nivelAgua < 200):
    print('no tengo agua')
elif(nivelAgua >= 200 and nivelAgua < 450):
    print('todo bien... energia funcionando')
else:
    print('ojo con caucasia')