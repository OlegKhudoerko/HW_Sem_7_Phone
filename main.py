import csv
import menu
import search
import shutil
import os.path
import input_data
import import_export_data
def main():
    menu.main_menu('Start')
    while True:
        menu.main_menu('Main')
        value = input('Выберите пункт меню: ')
        if value != '1' and value != '2' and value != '3' and value != '4' and value != '0':
            continue
        value = int(value)
        match value:
            case 1:
                menu.out_line()
                menu.file_menu()
                value_1 = input('Вся текущая база данных будет перемещена в архив, если уверены введите 1 ')
                if value_1 == '1':
                    if os.path.exists('phonebook.csv') == True:
                        print('Перемещаем все данные, создаем новые')
                    shutil.copy2(r'phonebook.csv', r'phonebook_old.csv')
                    with open('phonebook.csv', 'w', encoding="utf-8") as file:
                        writer = csv.DictWriter(file, fieldnames=['Фамилия', 'Имя', 'Отчество', 'Телефон'],
                                                lineterminator='\n')
                        writer.writeheader()
                else:
                    continue
            case 2:
                menu.out_line()
                print('Ввод новой записи')
                menu.out_line()
                if os.path.exists('phonebook.csv') == False:
                    msg()
                    continue
                input_data.input_data()
            case 3:
                menu.out_line()
                print('Поиск записи')
                menu.out_line()
                if os.path.exists('phonebook.csv') == False:
                    msg()
                    continue
                menu.search_menu()
                value_1 = input('Выберите пункт ')
                if value_1 == '1':
                    search_string = {}
                    name = input('Введите фамилию ')
                    if name.isalpha() == False:
                        msg_err()
                        continue
                    search_string = search.search_data('Фамилия', name)
                elif value_1 == '2':
                    search_string = []
                    name = input('Введите номер телефона ')
                    if name.isdigit() == False:
                        msg_err()
                        continue
                    search_string = search.search_data('Телефон', name)
                else:
                    continue
                print(search_string)
            case 4:
                menu.out_line()
                print('Импорт/экспорт записей')
                menu.out_line()
                menu.import_export_menu()
                value_1 = input('Выберите пункт ')
                if value_1 == '1':
                    if os.path.exists('phonebook.csv') == False:
                        msg()
                        continue
                    import_export_data.export_to_txt()
                elif value_1 == '2':
                    if os.path.exists('phonebook.csv') == False:
                        msg()
                        continue
                    import_export_data.import_to_csv()
                else:
                    continue
            case 0:
                break

def msg():
    print("База данных не сформирована!.. Выберети пункт меню номер 1")
def msg_err():
    print("Ошибка! Введено не верное значение")

main()
