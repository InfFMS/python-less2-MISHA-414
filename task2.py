num=int(input())
if num>12 or num<1:
    print('Неверный номер месяца')
elif num in [3,4,5]:
    print('Весна')
elif num in [6,7,8]:
    print('Лето')
elif num in [9,10,11]:
    print('Осень')
else:
    print('Зима')

