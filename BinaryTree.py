import copy


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class TNode:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            temp = Node(data)
            temp.next = self.head
            self.head = temp

    def pop(self):
        if self.head:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return temp.data
        else:
            return None

    def is_empty(self):
        return self.head is None

    def traverse(self):
        if self.head:
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.next
        return


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


def traverse_breadth_first_search(top):
    trav_bfs = Queue()
    trav_bfs.enqueue(top)

    while not trav_bfs.is_empty():
        node = trav_bfs
        top = node.dequeue()

        print(top.data)

        if top.left:
            node.enqueue(top.left)
        if top.right:
            node.enqueue(top.right)


def traverse_depth_first_search(top):
    if top is None:
        return

    trav_dps = Stack()
    trav_dps.push(top)

    while not trav_dps.is_empty():
        node = trav_dps.pop()

        if node is not None:
            print(node.data)
            if node.right is not None:
                trav_dps.push(node.right)
            if node.left is not None:
                trav_dps.push(node.left)


def display_tree(top, lvl=0):
    if top is None:
        return
    display_tree(top.right, lvl + 1)
    print("{} {}".format('   ' * lvl, top.data))
    display_tree(top.left, lvl + 1)


def insert_node(top, data):
    if top is None:
        top = TNode(data)
    else:
        if data < top.data:
            if top.left is None:
                top.left = TNode(data)
            else:
                insert_node(top.left, data)
        else:
            if top.right is None:
                top.right = TNode(data)
            else:
                insert_node(top.right, data)


def leaves(top):
    if top is None:
        return 0
    if top.left is None and top.right is None:
        return 1
    else:
        return leaves(top.left) + leaves(top.right)


def count_nodes_on_levels(top, lvl=0, lvl_counts={}):
    if top is None:
        return
    if lvl not in lvl_counts:
        lvl_counts[lvl] = 0

    lvl_counts[lvl] += 1
    count_nodes_on_levels(top.left, lvl + 1, lvl_counts)
    count_nodes_on_levels(top.right, lvl + 1, lvl_counts)

    return lvl_counts


def closest_leaf(top, path=[], leaf_depth=float('inf'), lf_list=[]):
    if top is None:
        return
    path.append(top.data)

    if not top.left and not top.right:
        if len(path) < leaf_depth:
            leaf_depth = len(path)
            lf_list.clear()
            lf_list.append(top.data)
        elif len(path) == leaf_depth:
            lf_list.append(top.data)

    else:
        closest_leaf(top.left, path, leaf_depth, lf_list)
        closest_leaf(top.right, path, leaf_depth, lf_list)
    path.pop()

new_root = # insert desired value here
insert_node(new_root, 3)
insert_node(new_root, 2)
insert_node(new_root, 1.75)
insert_node(new_root, 3.75)
insert_node(new_root, 6)
insert_node(new_root, 7)
display_tree(new_root)
