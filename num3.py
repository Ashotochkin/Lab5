def f() -> list:
    while True:
        try:
            return [int(input(f'Введите число №{i}: ')) for i in range(1, 1+int(input('Введите количество элементов списка: ')))]
        except:
            print('ДОЛЖНО ВВОДИТЬСЯ ЧИСЛО!!!')
       
def l():
    print('-'*50)
    
def L():
    print('_'*50)
 
while True:
    L()
    L()
    a = f()
    l()
    print(f'Список равен:\n{a}\n')
    print("Количество нулей равно", len(list(filter(lambda x: x == 0, a))), end='\n\n')
    index_min_num = a.index(min(a))
    print("Сумма элементов после минимального равна", sum(a[index_min_num+1:]), end='\n\n')
    l()
    if input('Хотите попробовать ещё раз? (да/нет или y/n): ').lower() not in ('да', 'y'):
        break