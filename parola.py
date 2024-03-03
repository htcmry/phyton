import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk =  int(input("Şifre Uzunluğunu Giriniz."))
 
parola = ""
for i in range(uzunluk):
    parola += random.choice(karakterler)

print(parola)
