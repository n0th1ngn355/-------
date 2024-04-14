a = []
with open('train_data_1.txt', "r", encoding='UTF-8') as f:
    a = f.readlines()
res = []
for i in a:
    res.append(i)
    x,y = i.split(':')
    res.append(f'{x.capitalize()}:{y.capitalize()}')
    res.append(f'{x}.:{y}')

with open('train_aug1.txt', 'w', encoding='UTF-8') as f:
    f.writelines(res)