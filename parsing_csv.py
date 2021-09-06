import csv


def parse_csv(csv_file):
    day_cost = 0
    day_credit = 0
    csv_reader = csv.DictReader(csv_file.split("\n"), delimiter=',')

    for row in csv_reader:
        day_cost += float(row['cost'])
        day_credit += float(row['credit'])

    return day_cost + day_credit
