def input_data():
    import csv
    head = ['Фамилия', 'Имя', 'Отчество', 'Телефон']
    line = []
    for i in head:
        enter = input(f'Введите {i} ')
        if i == head[3]:
            if enter.isdigit() == False:
                print('Введены не верные данные')
                break
        else:
            if enter.isalpha() == False:
                print('Введены не верные данные')
                break
        line.append(enter)
    if len(line) == 4:
        with open('phonebook.csv', 'a', encoding="utf-8") as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerow(line)
