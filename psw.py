import random
import pyperclip as pc

def main():
    print("")
    print("+--------------------+")
    print("| PASSWORD GENERATOR |")
    print("+--------------------+")
    print("")
    print("Genera una password con almeno una lettera maiuscola, una minuscola, un numero e un simbolo.")
    print("Al termine la password viene copiata neglia appunti.")
    print("L'utente può scegliere se salvare la password in un file di testo.")
    print("")
    while True:
       lunghezza = eval(input("Specificare la lunghezza della password: "))
       if lunghezza < 8:
           print("Una Password sicura deve avere almeno 8 caratteri.")
       elif lunghezza >= 25:
            print("ESAGERATO!")
       else:
            break
        
    generator(lunghezza)

def generator(y):
    x = True
    psw = []
    charType = []
    i = 0
    for i in range(0, y):
        charType.append("a")
        psw.append("a")
        
    while x == True:
        for i in range(0,y):
            charType[i] = random.randrange(1,5)
        for i in range(0,y):
            if charType[i] == 1:
                randomLower = random.randrange(97,124)
                psw[i] = chr(randomLower)
            elif charType[i] == 2:
                randomUpper = random.randrange(65,91)
                psw[i] = chr(randomUpper)
            elif charType[i] == 3:
                randomNum = random.randrange(48,58)
                psw[i] = chr(randomNum)
            elif charType[i] == 4:
                randomSpecial = random.randrange(33,48)
                psw[i] = chr(randomSpecial)
            
        (x, y) = validator(psw, y)

def validator(psw, y):
    lower = 0
    upper = 0
    num = 0
    special = 0

    for i in range(0,y):
        if ord(psw[i]) >= 97 and ord(psw[i]) <= 122:
           lower += 1
        elif ord(psw[i]) >= 65 and ord(psw[i]) <= 90:
           upper += 1
        elif ord(psw[i]) >= 48 and ord(psw[i]) <= 57:
           num += 1
        elif ord(psw[i]) >= 33 and ord(psw[i]) <= 47:
           special += 1  

    if lower > 0  and upper > 0 and num > 0 and special > 0 :
        print("La password è stata generata e validata.")
        print("La password generata è: " + ''.join(psw))
        pc.copy(''.join(psw))
        print("")
        print("Password copiata negli appunti.")
        print("")
        salvaPSW(psw)
        return (False, y)
    else:
        return (True, y)

def salvaPSW (psw):
    save = input("Si desidera salvare la password? y/n: ")
    if save == "y" :
        name = input("Dare un nome alla password: ")
        f = open("psw.txt", "a")
        f.write("\n" + name + " : " + ''.join(psw))
        f.close()
    else:
        exit()

main()