import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("Itroduzca la lingitud"))
contraseña = ""
for i in range(longitud):
    contraseña += random.choice(caracteres)
print(contraseña)
