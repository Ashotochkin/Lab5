string = input("Введите любую строку, программа найдёт сколько там цифр:\n")
c = 0
for i in string:
    if i.isdigit():
        c+=1
print(f'Количество цифр в строке равно: {c}')