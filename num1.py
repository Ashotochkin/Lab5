string = input("Введите любую строку:\n")
c = 0
for i in string:
    if i.isdigit():
        c+=1
print(f'Количество цифр в строке равно: {c}')