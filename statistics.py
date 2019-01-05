import json
from collections import Counter


def parse_json_sales(file_path):
    with open(file_path) as file:
        file_sales = file.read()
        data_sales = json.loads(file_sales)
    return data_sales


def count_sales(data):
    sales_stats = Counter(data)
    ordered_stats = sales_stats.most_common()
    return ordered_stats


def print_sales_statistics(order):
    for name, count in order:
        print('{} - {}'.format(name, count))


if __name__ == '__main__':
    data = parse_json_sales('./sales_log.json')
    order = count_sales(data)
    print_sales_statistics(order)
