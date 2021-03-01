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
time.sleep(2) # Delay de 2 Seg
while True:

    print("Aguarde....")
    nome_voto = pyautogui.locateOnScreen('nome.png') #Localizando imagem na sua tela e colocando na variavel
    if nome_voto == None: # Se a imagem nao for encontrada 
        print("Nome NAO encontrado") 
        break
    if nome_voto: # Se a imagem for encontrada
        print("Nome encontrado")
        point = pyautogui.center(nome_voto) # Recebendo a cooodenadas das imagem e colocando o mouse em cima
        pyautogui.click(point) # Fazendo evento de Click
        check = pyautogui.locateOnScreen('check.png') # Localizando Captcha na Tela
        if check == None: # Se Captcha nao for encontrado
            print("Captcha NAO Encontrado")
            check = pyautogui.locateOnScreen('check.png') # Tentando Localizar Captcha Novamente
        if check: # Se Captcha for encontrado
            print("Captcha Encontrado")
            pointCheck = pyautogui.center(check) # Apontando o mouse para o Captch
            pyautogui.click(pointCheck) # Evento de Clipe
            time.sleep(5) # Delay de 5 seg para atulizar a pag 
            pyautogui.hotkey('F5') # atualizando a pag
            print("Voto Computado")
            votos = votos + 1 # Computando Quantidade de votos
            print("Voce votou: ", votos, "vezes")
            time.sleep(5) # Delay de 5 seg




