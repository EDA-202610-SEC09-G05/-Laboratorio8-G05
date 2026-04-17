
from DataStructures.Tree import rbt_node as rn

def new_map():
    rbt = {
        'root': None,
        'type': 'RBT'
    }
    return rbt

def default_compare(key, element):
    if key == element['key']:
        return 0
    elif key > element['key']:
        return 1
    else:
        return -1
    
def is_red(node_rbt):
    if node_rbt is None:
        return False
    return node_rbt['color'] == rn.RED

def size_tree(root):
    if root is None:
        return 0
    return root['size']

def rotate_left(node_rbt):
    x = node_rbt['right']
    node_rbt['right'] = x['left']
    x['left'] = node_rbt

    x['color'] = node_rbt['color']
    node_rbt['color'] = rn.RED

    x['size'] = node_rbt['size']
    node_rbt['size'] = 1 + size_tree(node_rbt['left']) + size_tree(node_rbt['right'])

    return x

def rotate_right(node_rbt):
    x = node_rbt['left']
    node_rbt['left'] = x['right']
    x['right'] = node_rbt

    x['color'] = node_rbt['color']
    node_rbt['color'] = rn.RED

    x['size'] = node_rbt['size']
    node_rbt['size'] = 1 + size_tree(node_rbt['left']) + size_tree(node_rbt['right'])

    return x

def flip_node_color(node_rbt):
    if node_rbt['color'] == rn.RED:
        node_rbt['color'] = rn.BLACK
    else:
        node_rbt['color'] = rn.RED
    return node_rbt


def flip_colors(node_rbt):
    flip_node_color(node_rbt)
    flip_node_color(node_rbt['left'])
    flip_node_color(node_rbt['right'])
    return node_rbt

def insert_node(root, key, value):
    if root is None:
        return rn.new_node(key, value)

    cmp = default_compare(key, root)

    if cmp == 0:
        root['value'] = value
    elif cmp < 0:
        root['left'] = insert_node(root['left'], key, value)
    else:
        root['right'] = insert_node(root['right'], key, value)

    if is_red(root['right']) and not is_red(root['left']):
        root = rotate_left(root)

    if is_red(root['left']) and is_red(root['left']['left']):
        root = rotate_right(root)

    if is_red(root['left']) and is_red(root['right']):
        root = flip_colors(root)

    root['size'] = 1 + size_tree(root['left']) + size_tree(root['right'])
    return root