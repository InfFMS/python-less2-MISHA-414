a_1, b_1, a_2, b_2=map(int, input().split())
if b_1<a_2:
    print('пустое множество')
elif b_1==a_2  or a_1==b_2:
    print(b_1)
elif a_1>=a_2 and b_1<=b_2:
    print(f'[{a_1};{b_1}]')
elif a_1<=a_2 and b_1>=b_2:
    print(f'[{a_2};{b_2}]')
elif a_1>=a_2 and b_1<=b_2:
    print(f'[{a_1};{b_1}]')
elif a_1<=a_2:
    print(f'[{a_2};{b_1}]')
elif a_1>=a_2:
    print(f'[{a_1};{b_2}]')