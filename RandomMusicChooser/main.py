########################################################################
#                           Made by. Itz_Jiryn                         #                           
# If this ever stops working please contact me so i can fix this file. #
#                             Itz_Jiryn#4780                           #
########################################################################

# Import
import os
import time
import random

t = int(input("Jak dlouho má hudba hrát?(s): "))
numbers = []

while True:
    #Funkce
    def number():
        number = random.randint(1, 15)
        return number

    def songchooser(number):
        if number == 1:
            os.system(r'start wmplayer.exe "C:\Users\jirin\Desktop\Programování\Local\OsobniProjekty\python\randommusicchooser\files\1.mp3"')
            time.sleep(t)
            os.system(r'taskkill /IM wmplayer.exe')
            print("Seikkilova píseň")
        elif number == 2:
            os.system(r'start wmplayer.exe "C:\Users\jirin\Desktop\Programování\Local\OsobniProjekty\python\randommusicchooser\files\2.mp3"')
            time.sleep(t)
            os.system(r'taskkill /IM wmplayer.exe')
            print("Johann Sebastian Bach - Toccata a fuga D-moll")
        elif number == 3:
            os.system(r'start wmplayer.exe "C:\Users\jirin\Desktop\Programování\Local\OsobniProjekty\python\randommusicchooser\files\3.mp3"')
            time.sleep(t)
            os.system(r'taskkill /IM wmplayer.exe')
            print("Georg Fridrich Handel - Halelujah")
        elif number == 4:
            os.system(r'start wmplayer.exe "C:\Users\jirin\Desktop\Programování\Local\OsobniProjekty\python\randommusicchooser\files\4.mp3"')
            time.sleep(t)
            os.system(r'taskkill /IM wmplayer.exe')
            print("Antonio Vivaldi - Jaro")
        elif number == 5:
            os.system(r'start wmplayer.exe "C:\Users\jirin\Desktop\Programování\Local\OsobniProjekty\python\randommusicchooser\files\5.mp3"')
            time.sleep(t)
            os.system(r'taskkill /IM wmplayer.exe')
            print("Wolfgang Amadeus Mozart - Malá noční hudba")
        elif number == 6:
            os.system(r'start wmplayer.exe "C:\Users\jirin\Desktop\Programování\Local\OsobniProjekty\python\randommusicchooser\files\6.mp3"')
            time.sleep(t)
            os.system(r'taskkill /IM wmplayer.exe')
            print("Ludwig van Beethoven - Pro Elišku")
        elif number == 7:
            os.system(r'start wmplayer.exe "C:\Users\jirin\Desktop\Programování\Local\OsobniProjekty\python\randommusicchooser\files\7.mp3"')
            time.sleep(t)
            os.system(r'taskkill /IM wmplayer.exe')
            print("Richard Strauss - Tak pravil Zarathustra")
        elif number == 8:
            os.system(r'start wmplayer.exe "C:\Users\jirin\Desktop\Programování\Local\OsobniProjekty\python\randommusicchooser\files\8.mp3"')
            time.sleep(t)
            os.system(r'taskkill /IM wmplayer.exe')
            print("Franz Schubert - Pstruh")
        elif number == 9:
            os.system(r'start wmplayer.exe "C:\Users\jirin\Desktop\Programování\Local\OsobniProjekty\python\randommusicchooser\files\9.mp3"')
            time.sleep(t)
            os.system(r'taskkill /IM wmplayer.exe')
            print("Ludvig van Beethoven - Osudová symfonie")
        elif number == t:
            os.system(r'start wmplayer.exe "C:\Users\jirin\Desktop\Programování\Local\OsobniProjekty\python\randommusicchooser\files\10.mp3"')
            time.sleep(t)
            os.system(r'taskkill /IM wmplayer.exe')
            print("Antonín Dvořák - Novosvětská symfonie")
        elif number == 11:
            os.system(r'start wmplayer.exe "C:\Users\jirin\Desktop\Programování\Local\OsobniProjekty\python\randommusicchooser\files\11.mp3"')
            time.sleep(t)
            os.system(r'taskkill /IM wmplayer.exe')
            print("Bedřich Smetana - Vltava")
        elif number == 12:
            os.system(r'start wmplayer.exe "C:\Users\jirin\Desktop\Programování\Local\OsobniProjekty\python\randommusicchooser\files\12.mp3"')
            time.sleep(t)
            os.system(r'taskkill /IM wmplayer.exe')
            print("Claude Debussy - Potopená katedrála")
        elif number == 13:
            os.system(r'start wmplayer.exe "C:\Users\jirin\Desktop\Programování\Local\OsobniProjekty\python\randommusicchooser\files\13.mp3"')
            time.sleep(t)
            os.system(r'taskkill /IM wmplayer.exe')
            print("Maurice Ravel - Bolero")
        elif number == 14:
            os.system(r'start wmplayer.exe "C:\Users\jirin\Desktop\Programování\Local\OsobniProjekty\python\randommusicchooser\files\14.mp3"')
            time.sleep(t)
            os.system(r'taskkill /IM wmplayer.exe')
            print("Johann Sebastian Bach - Ave Maria")
        elif number == 15:
            os.system(r'start wmplayer.exe "C:\Users\jirin\Desktop\Programování\Local\OsobniProjekty\python\randommusicchooser\files\15.mp3"') # Road
            time.sleep(t)
            os.system(r'taskkill /IM wmplayer.exe')
            print("Arnold Schonberg - Ten který přežil Waršavu") # Name
            
    # Konstrukce
    number = number()

    songchooser(number)


