def import_to_csv():
    import csv
    txtfile = "phone.txt"
    csvfile = "phonebook.csv"
    with open(txtfile, 'r', encoding="utf-8") as infile, open(csvfile, 'a', encoding="utf-8") as outfile:
        lines = infile.readlines()
        for line in lines:
            writer = csv.writer(outfile, lineterminator='\n')
            writer.writerow((line.strip()).split(sep=','))


def export_to_txt():
    import csv
    txtfile = "phone_.txt"
    csvfile = "phonebook.csv"
    with open(csvfile, 'r', encoding="utf-8") as infile, open(txtfile, 'w', encoding="utf-8") as outfile:
        reader = csv.DictReader(infile)
        for row in reader:
            # print(row.values())
            outfile.writelines((map(lambda s: s + ',', row.values())))
            outfile.writelines('\n')
