import csv


def search_data(field, name_string):
    reader = {}
    result_search = []
    with open('phonebook.csv', 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row[field] == name_string:
                result_search += row.values()
        if result_search == []:
            print('Запись отсутствует')
        return result_search
