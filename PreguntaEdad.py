# Programa que pregunta la edad del usuario y te dejará pasar si eres mayor y si eres menor te pedirá una edad más alta


while True:
    try:
        edad = int(input("Ingrese su edad"))
    except ValueError:
        print("No ingrese letras. Solo se admiten números")
        continue
    if edad <= 17:
        print("No puede pasar. Edad Incorrecta o eres menor")
        continue
    else:
        print("Bienvenido al club. Pase adelante", "su edad es de: \n" + str(edad))
        break

