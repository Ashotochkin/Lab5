def isNumb(x: str) -> bool:
    try:
        float(x)
        return True
    except ValueError:
        return False
            
while True:
    print('-'*50)
    
    string = input("Введите любую строку, программа найдёт сколько там цифр:\n")
    
    numbCount = 0
    for i in string:
        if isNumb(i):
            numbCount+=1
    
    print(f'\n\033[32m\033[1mКоличество цифр равно {numbCount}\033[0m' if numbCount>0 else '\n\033[31m\033[1mЦифр нет \033[0m:(')

    if input("\nещё раз? (y/n)\n").lower() not in ["y", 'да']:
        break

print("Усё")

