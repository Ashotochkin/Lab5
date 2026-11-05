def num(i):
    while True:
        try:
            return float(input(f'Введите число №{i}: '))
        except ValueError:
            print('\n\033[1m\033[31mЭТО ДОЛЖНО БЫТЬ ЧИСЛО\033[0m\n')

def list_nums():
    while True:
        try:
            list_num = []
            for i in range(1, 1+int(input('Введите количество элементов списка: '))):
                list_num.append(num(i))
            return list_num
        except ValueError:
            print('\n\033[1m\033[31mА где это находится в натуральных числах?\033[0m\n')

def l():
    print('-'*50)
    
def L():
    print(f"{'_'*50}\n"*2)

while True:
    L()
    a = list_nums()
    
    print(f'\n* Список равен:\033[1m\033[32m\n{a}\033[0m\n')
    
    zeroCount = 0
    for i in a:
        if i == 0:
            zeroCount+=1
    
    
    print("* \033[1m\033[32mКоличество нулей равно {}\033[0m\n".format(zeroCount) if zeroCount>0 else "\033[1m\033[31m* Нулей нет\033[0m\n")
    
    min_a = (a[0], 0)
    enum = 0
    for i in a[1:]:
        enum+=1
        if i < min_a[0]:
            min_a = (i, enum)
    
    sum_after_min_a = 0
    for i in a[min_a[1]+1:]:
        sum_after_min_a+=i
    
    
    
    print("* \033[1mСумма элементов после первого минимального равна {}\033[0m".format(sum_after_min_a), end='\n\n')
    l()
    if input('Хотите попробовать ещё раз? (да/нет или y/n): ').lower() not in ('да', 'y'):
        break

print('Усё')