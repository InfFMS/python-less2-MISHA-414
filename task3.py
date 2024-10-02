old=int(input())
let=[11,12,13,14]
if old==1:
    print('1 год')
elif old%10>=5 or old%10==0 or old in let:
    print(f'{old} лет')
else:
    print(f'{old} года')
