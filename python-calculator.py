def additon(x,y):
    return x + y


def substraction(x,y):
    return x - y


def multiplication(x,y):
    return x * y


def division(x,y):
    if y == 0:
        return print("sayı 0'a bölünemez")
    return x / y


def inputoutput():
    while(True):
        try:
            x = float(input("1. sayıyı girin  "))
            y = float(input("2. sayıyı girin  "))
            return x,y
        except ValueError:
            print("geçersiz bir sayı girdiniz")


    

print("Merhabalar hesap makinesine hoşgeliniz")

while(True):

    print(""" Toplama işlemi için 1'e basın
 Çıkartma işlemi için 2'ye basın
 Çarpma işlemi için 3'e basın
 Bölme işlemi için 4'e basın
 Programdan çıkmak için 5'e basın ...""")

    try:
         userChoice = int(input())
    except ValueError:
        print("1 ile 5 arası sayı giriniz")
        continue

    
    if userChoice == 1:
        x,y = inputoutput()
        print("sonuç :  ", additon(x,y))
    
    elif userChoice == 2:
        x,y = inputoutput()
        print("sonuç :  ", substraction(x,y))
    elif userChoice == 3:
        x,y = inputoutput()
        print("sonuç :  ", multiplication(x,y))
    elif userChoice == 4:
        x,y = inputoutput()
        print("sonuç :  ", division(x,y))
    elif userChoice == 5:
        print("Hoşçakalın")
        break
    else:
        print("yanlış bir seçim yaptınız tekrar deneyin")


