from Victory import people
print('Добро пожаловать в игру!')
name = input('Как тебя зовут? ')
print("отлично!", name)
answ = input("Ты готов начать игру?")
if answ == 'да':
    people()
elif answ == 'нет':
    print("Ну давай готовься тогда")
else:
    print("Не могу понять, что ты пишешь")