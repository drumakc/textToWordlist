import os.path
import re #для работы с регулярными варажениями

if os.path.isfile('input.txt'):
    fileInput = open('input.txt', 'r')
    #fileInput = open('input.txt', 'r', encoding='UTF8')
    tempInput = fileInput.read()
    fileInput.close()
    print('Файл input.txt прочитан в fileInput.')

    #remove punctuation marks
    tempInput = tempInput.replace('.', '')
    print('Удалил точки.')
    tempInput = tempInput.replace(',', '')
    print('Удалил запятые.')
    tempInput = tempInput.replace(':', '')
    print('Удалил двоеточия.')
    tempInput = tempInput.replace(';', '')
    print('Удалил знаки - точка с запятой.')
    tempInput = tempInput.replace('!', '')
    print('Удалил восклицательные знаки.')
    tempInput = tempInput.replace('?', '')
    print('Удалил вопросительные знаки.')
    tempInput = tempInput.replace('"', '')
    print('Удалил двойные кавычки.')
    tempInput = tempInput.replace('#', '')
    print('Удалил #')
    
    tempInput = tempInput.split()

    if os.path.isfile('output.txt'):
        fileOutput = open('output.txt', 'r', encoding='UTF8')
    else:
        fileOutput = open('output.txt', 'w', encoding='UTF8')
        fileOutput.close()
        fileOutput = open('output.txt', 'r', encoding='UTF8')

    tempOutput = fileOutput.read().split()
    fileOutput.close()

    print('Файл output.txt прочитан в tempOutput')
    print('Начал удалять дубликаты')

    #remove duplicates
    noDuplicates = []
    for i in tempInput:
        if len(i) > 7:
            if i not in tempOutput:
                noDuplicates.append(i)
                print(i)

    print('Дубликаты удалены')
    print('Начал добавлять результат в temp')
    temp = ''
    for i in noDuplicates:
        temp += i + '\n'
        print(i)

    print('Добавляю результат в файл output.txt')
    fileOutput = open('output.txt', 'a', encoding = "utf8")
    fileOutput.write(temp)
    fileOutput.close()

    print('Удаляю файл input.txt')
    os.remove('input.txt')

    print()
    print('XXXXXXX  XX    XX')
    print('XX   XX  XX   XX')
    print('XX   XX  XX XX')
    print('XX   XX  XXX')
    print('XX   XX  XX XX')
    print('XX   XX  XX  XX')
    print('XX   XX  XX   XX')
    print('XXXXXXX  XX    XX')
else:
    print('Файл input.txt не найден.')
    


