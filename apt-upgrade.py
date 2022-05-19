import os
import time

os.system("sudo apt update")
time.sleep(1)
List1w = open("List1.txt", "w")
List1w.close()
os.system("logsave List1.txt sudo apt list --upgradable")
os.system("clear")

List1r = open("List1.txt", "r")
List1r = List1r.read().split("/")

List2w = open("List2.txt", "w")
List2w.write("")
List2w.close()

for i in List1r:
    List2a = open("List2.txt", "a")
    List2a.write(i+"\n")

List2r = open("List2.txt", "r")
List2r = List2r.read().split("\n")

count = 1
List3w = open("List-upgrade.txt", "w")
List3w.write("")
List3w.close()

for i in List2r:
    result = count % 2
    if result==0:
        List3a = open("List-upgrade.txt", "a")
        List3a.write(str(i)+"\n")
        List3a.close()
    elif result==1:
        print("")
    count=count+1

try:
    List3r = open("List-upgrade.txt", "r")
    List3r = List3r.read().split("\n")
    List3r.pop(0)
    List3r.remove('')
    os.remove("List1.txt")
    os.remove("List2.txt")
    os.system("clear")
except ValueError:
    os.system("clear")
    os.system("echo '' && echo ' \033[1;31mNo hay actualizaciones disponibles'")
    os.remove("List1.txt")
    os.remove("List2.txt")
    os.remove("List-upgrade.txt")
    time.sleep(3)
    os.system("clear")
    os.system("bash Salida/Error.sh")
    exit()

i = 0
while True:
    num = len(List3r)
    num = int(num)-2
    os.system("echo '' && echo ' \\033[1;39mHay \\033[1;32m{} \\033[1;39mactualizaciones disponibles'".format(num))
    sn = str(input("\n ¿Desea continuar? [S/n] "))
    if sn in ["SI","Si","S","s",""]:
        break
    elif sn in ["NO","No","N","n"] or i == 2:
        os.system("clear")
        os.remove("List-upgrade.txt")
        os.system("bash Salida/Gracias.sh")
        exit()
    else:
        os.system("clear")
    i=i+1

os.system("clear")

for i in List3r:
    if i == (''):
        pass
    else:        
        os.system("apt install {}".format(i))
        os.system("echo '' && echo '\\033[1;32m {} \\033[1;39m a ha actualizado correctamente'".format(i))
        time.sleep(0.75)
        os.system("clear")
os.remove("List-upgrade.txt")
os.system("bash Salida/Gracias.sh")
exit()
