x_elefante, y_elefante = map(int, input().split())
x, y = map(int, input().split())
dx=max(x, x_elefante)-min(x, x_elefante)
dy=max(y, y_elefante)-min(y, y_elefante)
if dx==dy:
    print('Yes')
else:
    print('No')