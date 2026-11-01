def without_round_brackets(string: str) -> str:
    str1 = ''
    depth = 0
   
    for i in string:
        if i == '(':
            if depth == 0:
                str1+='()'
            depth+=1
        elif i == ')':
            if depth > 0:
                depth-=1
        else:
            if depth == 0:
                str1+=i        
                
    return str1

while True:
    print('-'*50)

    print(f"\n\033[1m\033[32m{without_round_brackets(input('\nВведите любую строку, программа отчистит её от текста в скобках ():\n'))}\033[0m")


    if input("\nещё раз? (y/n)\n").lower() not in ["y", 'да']:
        break

print("Усё")
