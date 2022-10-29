import sys
file_a = open('file.txt', 'r') # Открытие нашего файла
strings = [line.strip() for line in file_a] # .strip() для того чтобы не было "\n" в файле

string = ''
for i in strings: # Сбор всех строк в одну строку
    string += i + ' '

end_sentence = '.!?' # Символы, являющиеся концом предложения
indices = [] # Массив, хранящий индесы начала и концов предложений (включительно)
save_i = 0
for count in range(3): # Счетчик предложений
    start, end = -1, -1 # Индексы, хранящие начала и конец предложения (включительно)
    for i in range(save_i, len(string)):
        if start == -1:
            start = i
        else:
            for j in end_sentence: # j - символ-конец предложения
                if string[i] == j: # Равен ли символ из строки символу-концу предложения?
                    end = i
                    break
        if end != -1:
            break

    if start != -1 and end != -1:
        indices.append([start, end])
        save_i = end+1
    else:
        print("В файле меньше 3 предложений!")
        sys.exit()

indices.reverse() # Разворачиваем массив

for ind in indices:
    print(string[ind[0] : ind[1]+1], end = ' ')
