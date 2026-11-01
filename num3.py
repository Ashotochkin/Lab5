def num(i):
    while True:
        try:
            return float(input(f'Введите число №{i}: '))
        except ValueError:
            print('\n\033[1m\033[31mЭТО ДОЛЖНО БЫТЬ ЧИСЛО\033[0m\n')

def list_nums():
    while True:
        try:
            return [num(i) for i in range(1, 1+int(input('Введите количество элементов списка: ')))]
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
    zeroCount = len(list(filter(lambda x: x == 0, a)))
    print("* \033[1m\033[32mКоличество нулей равно {}\033[0m\n".format(zeroCount) if zeroCount>0 else "\033[1m\033[31m* Нулей нет\033[0m\n")
    print("* \033[1mСумма элементов после первого минимального равна {}\033[0m".format(sum(a[a.index(min(a))+1:])), end='\n\n')
    l()
    if input('Хотите попробовать ещё раз? (да/нет или y/n): ').lower() not in ('да', 'y'):
        break