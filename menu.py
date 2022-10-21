def main_menu(value):
    match value:
        case 'Start':
            print('Вас приветствует бот телефонного справочника!!!')
            out_line()
        case 'Main':
            print('Выберите пожалуйста пункт меню: \n')
            out_line()
            print('0 - Выход из программы')
            print('1 - Создать новую базу данных справочника')
            print('2 - Внести запись')
            print('3 - Найти запись')
            print('4 - Импорт/экспорт записей')
            out_line()


def search_menu():
    out_line()
    print('Варианты поиска')
    print('1. Найти по фамилии')
    print('2. Найти по номеру телефона')
    out_line()


def import_export_menu():
    out_line()
    print('Варианты')
    print('1. Экспорт из csv в txt файл')
    print('2. Импорт из txt в csv файл')
    out_line()


def file_menu():
    out_line()
    print('Варианты')
    print('1. Подтвердите свой выбор, введите 1')
    out_line()


def out_line():
    print("=" * 50)
