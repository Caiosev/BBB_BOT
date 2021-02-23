import time
import pyautogui

print("iniciando votação")
votos = 0

print(" ____   ____   ____   ____    ___  _____ ")
print("|  _ \ |  _ \ |  _ \ |  _ \  / _ \(_   _)")
print("| |_) )| |_) )| |_) )| |_) )| | | | | |  ")
print("|  _ ( |  _ ( |  _ ( |  _ ( | | | | | |  ")
print("| |_) )| |_) )| |_) )| |_) )| |_| | | |  ")
print("|____/ |____/ |____/ |____/  \___/  |_|  ")
print("By: @caiosev")
time.sleep(2)
while True:

    print("Aguarde....")
    nome_voto = pyautogui.locateOnScreen('nome.png')
    if nome_voto == None:
        print("Nome NAO encontrado")
        break
    if nome_voto:
        print("Nome encontrado")
        point = pyautogui.center(nome_voto)
        pyautogui.click(point)
        check = pyautogui.locateOnScreen('check.png')
        if check == None:
            print("Captcha NAO Encontrado")
            check = pyautogui.locateOnScreen('check.png')
        if check:
            print("Captcha Encontrado")
            pointCheck = pyautogui.center(check)
            pyautogui.click(pointCheck)
            time.sleep(5)
            pyautogui.hotkey('F5')
            print("Voto Computado")
            votos = votos + 1
            print("Voce votou: ", votos, "vezes")
            time.sleep(5)




