import os.path
import re #для работы с регулярными варажениями

fileInput = open('input.txt', 'r')
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
tempInput = tempInput.split()

if (os.path.isFile('output.txt')):
    fileOutput = open('output.txt', 'r')
else:
    fileOutput = open('output.txt', 'w')

tempOutput = fileOutput.read().split()
fileOutput.close()

print('Файл output.txt прочитан в tempOutput')
print('Начал удалять дубликаты')

#remove duplicates
noDuplicates = []
for i in tempInput:
    if len(i) > 7:
        if (i not in noDuplicates) and (i not in tempOutput):
            noDuplicates.append(i)
            print(i)

print('Дубликаты удалены')
print('Начал добавлять результат в temp')
temp = ''
for i in noDuplicates:
    temp += i + '\n'
    print(i)

print('Добавляю результат в файл output.txt')
fileOutput = open('output.txt', 'a')
fileOutput.write(temp)
fileOutput.close()

print()
print('XXXXXXX  XX    XX')
print('XX   XX  XX   XX')
print('XX   XX  XX XX')
print('XX   XX  XXX')
print('XX   XX  XX XX')
print('XX   XX  XX  XX')
print('XX   XX  XX   XX')
print('XXXXXXX  XX    XX')