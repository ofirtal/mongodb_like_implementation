import json
import sys
from mongodblike_implementation_class import BinTree

inventory = [
    {"name": "ab", "qty": 15, "price": 2.99},
    {"name": "cd", "qty": 5, "price": 3.99},
    {"name": "ij", "qty": 3, "price": 1.99},
    {"name": "ij", "qty": 15, "price": 1.99},
    {"name": "xy", "qty": 20, "price": 1.99}
]


def refactor_query(expression):
    exp = expression.replace('\$', '')
    str_data_dict = json.loads(exp)
    print('this is the main str: ', str_data_dict, '\n')
    return str_data_dict


def find(query, db):
    updated_query_str = refactor_query(query)
    mytree = BinTree(updated_query_str)
    mytree.node_val_to_action(db)


def main():
    query = sys.argv[1]
    find(query, db=inventory)


if __name__ == "__main__":
    main()