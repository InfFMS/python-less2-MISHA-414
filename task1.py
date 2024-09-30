n=int(input())
time_star=8*60+30+55*(n-1)
hour_star=time_star//60
min_star=time_star%60
time=time_star+45
hour_fin=time//60
min_fin=time%60

print(f'Время начала урока - {hour_star}:{min_star}, Время конца - {hour_fin}:{min_fin}')