import pickle
import os
def save_data(dct):
    with open(file_name, 'wb') as f:
        pickle.dump(dct, f)
 
file_name = 'data'
if file_name not in os.listdir():
    dct = {}
    save_data(dct)
with open('data', 'rb') as f:
    dct = pickle.load(f)
name = input('фио: ')
if name in dct:
    print(f'«Вы нас уже посетили {dct.get(name)} раз»')
else:
    print(f'«Вы успешно зарегистрированы в системе!»')   
dct[name] = dct.setdefault(name, 0) + 1    
save_data(dct)    
print(f'«До новых встреч, {name}».\nЗаранее спасибо!')