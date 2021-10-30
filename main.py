import random
from easygui import *

def fileOpen(): #функция открытия файлов
    fileTruth = open("truth.txt","r")
    fileDare = open("dare.txt","r")
    return fileTruth, fileDare
try:
    fileTruth, fileDare = fileOpen()
except:
    print("No file")

def lineToList(): # функция для перевода строк из файлов в отдельные массивы
    truthList = [line.strip() for line in fileTruth]
    dareList = [line.strip() for line in fileDare]
    return truthList, dareList
try:
    truthList, dareList = lineToList()
except:
    print("Error")

#цикл для ввода правильного числа
while True:
    try:
        roundsText = "Сколько раундов Вы хотите сыграть?" # текст в окне ввода числа
        roundsTitle = "Раунды" # заголовок окна ввода числа
        roundsDefInt = 10 # значение по умолчанию 
        roundsLower = 0 # минимальное значение
        roundsUpper = 100 # максимальное значение
        rounds = integerbox(roundsText, roundsTitle, roundsDefInt, roundsLower, roundsUpper) # создание окна
        break #конец цикла
    except:
        print("Нужно ввести число!")

while True: #цикл для ввода количества игроков
    try:
        playersText = "Сколько игроков будет играть?"
        playersTitle = "Игроки"
        playersDefInt = 2
        playersLower = 0
        playersUpper = 20
        players = integerbox(playersText, playersTitle, playersDefInt, playersLower, playersUpper) # создание окна
        break   #конец цикла
    except:
        print("Нужно ввести число!") 
    
playersNames = [] #массив для имён

for playerNum in range(players):
    playerNameText = ("Введите имя игрока #"+str(playerNum + 1)) # текст в окне ввода
    playerNameTitle = "Имя игрока "+str(playerNum + 1) # заголовок окна ввода
    playerName = enterbox(playerNameText, playerNameTitle) # создание окна
    playersNames.append(playerName) # добавление в конец списка

okButton = "Продолжить"

for game in range(rounds): # цикл раундов
    roundMessage = "Раунд #" + str(game + 1)
    roundTitle = "Раунд #" + str(game + 1)
    roundOkBtn = "Начать"
    msgbox(roundMessage, roundTitle, roundOkBtn)
    for player in playersNames: #цикл выбора игрока
        while True: # цикл ввода правильного значения
            selectMessage = player
            selectTitle = "Выбор"
            selectButtons = ['Правда','Действие']
            select = boolbox(selectMessage, selectTitle, selectButtons)
            truth = random.choice(truthList)#случайный выбор из массива
            dare = random.choice(dareList) #случайный выбор из массива
            if select == 1: # если выбор правда
                msgbox(truth, okButton) # случайный выбор из массива
                break
            elif select == 0:
                msgbox(dare, okButton)
                break
            else:
                msgbox("Error")

        while True: # цикл проверки выполнено или нет
            completedMessage = "Выполнено или провалено"
            completedTitle = "Результат"
            completedButtons = ['Выполнено', 'Провалено']
            completed = boolbox(completedMessage, completedTitle, completedButtons)
            if completed == 1:
                msgbox("Молодец", okButton)
                break
            elif completed == 0:
                msgbox("НЕ молодец",okButton)
                break
            else:
                msgbox("Error")

msgbox("Спасибо за игру!", okButton)

