string = input('Введите любую строку:\n')

b = True
str1 = ''

for i in string:
    if i == "(":
        b = False
        str1 += i
    elif i == ')':
        b = True
        str1 += i
    elif b:
        str1 += i
print(str1)