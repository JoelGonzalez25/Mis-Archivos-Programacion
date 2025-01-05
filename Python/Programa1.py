# print("Hola Mundo")
# print("Estoy aprendiendo Python")

# nombre = "Joel"
# print(nombre)


# if (5 > 3 or 3 > 4):
#     print("verdadero")
# else:
#     print("falso")
# with open("tablas_multiplicar.txt", "w") as archivo:
#     for tabla in range(1, 11):
#         archivo.write(f"Tabla del {tabla}:\n")
#         for i in range(1, 11):
#             archivo.write(f"{tabla} x {i} = {tabla * i}\n")
#         archivo.write("\n")
for tabla in range(5, 13):
    print(f"Tabla del {tabla}:")
    for i in range(1, 13):
        print(f"{tabla} x {i} = {tabla * i}")
    print()