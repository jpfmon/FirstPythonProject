# value1t = input("Enter a value: ")
#
# if value1t.isnumeric():
#     value1 = int(value1t)
# else:
#     value1 = int(input("Enter numeric value: "))
#
# value2 = int(input("Enter a value: "))
#
# print("1 - Add")
# print("2 - Substract")
# print("3 - Divide")
# print("4 - Multiply")
#
# selection = int(input("Choose Operation: "))
#
# if selection == 1:
#     print(value1 + value2)
# elif selection == 2:
#     print(value1 - value2)
# elif selection == 3:
#     print(value1 / value2)
# else:
#     print(value1 * value2)
#
#
# def funcion(x):
#     for i in range(1,x+1):
#         for j in range(1,i+1):
#             print(j,end=" ")
#         print()
#
# continuar = True
#
# while continuar:
#     cant = int(input("Cuantos numeros?"))
#     if cant > 50:
#         print("Por favor, no tanto. Algo menos de 50")
#     if cant <= 50:
#         continuar = False
#
# funcion(cant)

s = "hola"

def myfunc(s):
    index = 1
    s_new = ""
    for char in s:
        if(index%2==0 and index != 0):
            s_new = s_new + char.upper()
        else:
            s_new = s_new + char.lower()
        index += 1
    return s_new

print(myfunc("Antropomorphism"))