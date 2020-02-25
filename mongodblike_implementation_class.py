from mongodblike_implementation_utilities import math_operators, range_operators,\
    and_or, operators_dict


class BinNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

    def find_in_node(self, data):
        if self.value == data:
            print('item: ~{}~ was found! yay'. format(data))
            return True
        else:
            if self.left:
                BinTree.find_in_tree(self.left, data)
            elif self.right:
                BinTree.find_in_tree(self.right, data)
            return False

    def get_value(self):
        return self.value

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right


class BinTree:
    def __init__(self, query_dict):
        if isinstance(query_dict, dict):
            op_value = [*query_dict][0]

            if op_value in and_or:
                root_val = op_value
                left_c = BinTree(query_dict[op_value][0])
                right_c = BinTree(query_dict[op_value][1])
            else:
                root_val = [*query_dict[[*query_dict][0]]][0]
                left_c = BinTree(op_value)
                right_c = BinTree(query_dict[[*query_dict][0]][[*query_dict[[*query_dict][0]]][0]])

            self.root = BinNode(root_val, left_c, right_c)
        else:
            self.root = BinNode(query_dict)

    def get_value(self):
        return self.root.value

    def get_left(self):
        return self.root.left

    def get_right(self):
        return self.root.right

    # (Left, Root, Right):
    def inorder_print(self):
        if self.root.left:
            self.root.left.inorder_print()
        print(self.root.value)
        if self.root.right:
            self.root.right.inorder_print()

    # (Root, Left, Right) :
    def preorder_print(self):
        print(self.root.value)
        if self.root.left:
            self.root.left.preorder_print()
        if self.root.right:
            self.root.right.preorder_print()

    # (Left, Right, Root)
    def postorder_print(self):
        if self.root.left:
            self.root.left.postorder_print()
        if self.root.right:
            self.root.right.postorder_print()
        print(self.root.value)

    def get_height(self):
        if self.root.left is None or self.root.right is None:
            return 0
        else:
            left_height = self.root.left.get_height()
            right_height = self.root.right.get_height()

        return 1 + max(left_height, right_height)

    def level_print(self):
        levels = {}

        def insert(node,
                   level):
            if level in levels.keys():
                levels[level].append(node.root.value)
                if node.root.left:
                    insert(node.root.left, level + 1)
                if node.root.right:
                    insert(node.root.right, level + 1)
            else:
                levels[level] = [node.root.value]
                if node.root.left:
                    insert(node.root.left, level + 1)
                if node.root.right:
                    insert(node.root.right, level + 1)
        insert(self, 0)
        print(levels)
        return levels

    def run_on_dict(self, item):
        if self.root.value == 'and':
            return self.root.left.run_on_dict(item) and self.root.right.run_on_dict(item)
        elif self.root.value == 'or':
            return self.root.left.run_on_dict(item) or self.root.right.run_on_dict(item)
        elif self.root.value in math_operators:
            if isinstance(self.root.right.get_value(), str):
                # for end cases where the name is str and not an int
                return operators_dict['{}str'.format(self.root.value)]((item[self.root.left.get_value()]),
                                                       (self.root.right.get_value()))
            return operators_dict[self.root.value]((item[self.root.left.get_value()]),
                                                   float(self.root.right.get_value()))
        elif self.root.value in range_operators:
            return operators_dict[self.root.value](float(item[self.root.left.get_value()]),
                                                   list(self.root.right.get_value()))
        else:
            print("unknown command in query")
            return False

    def node_val_to_action(self, db):
        items_found = 0
        for item in db:
            if self.run_on_dict(item):
                print(item)
                items_found += 1

        if items_found == 0:
            print('No items found')
        else:
            print('Total of {} items found'.format(items_found))


    def revers_level_print(self):
        levels_dict = self.level_print()
        h = self.get_height()
        for i in range(h, -1, -1):
            print(i, ' ; ', levels_dict[i])

    def find_in_tree(self, data):
        print('self.root', self.root.value)
        if self.root:
            BinNode.find_in_node(self.root, data)
        else:
            print('item: ~{}~ NOT FOUND :( '.format(data))
            return False
