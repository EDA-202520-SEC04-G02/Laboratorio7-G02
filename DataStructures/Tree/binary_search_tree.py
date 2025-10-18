from DataStructures.Tree import bst_node as bst

def default_compare(a,b):
    if a == b:
        return 0
    return -1 if a < b else 1

def new_map():
    return {"root":None}

def insert_node(root, key, value):
    if root is None:
        return bst.new_node(key, value)

    cmp = default_compare(key, root["key"])
    if cmp == 0:
        root["value"] = value
    elif cmp < 0:
        root["left"] = insert_node(root["left"], key, value)
    else:
        root["right"] = insert_node(root["right"], key, value)

    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root

def put(my_bst, key, value):
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    return my_bst

def get_node(root,key):
    
    if root is None:
        return None
    
    if key == root["key"]:
        return root

    elif key < root["key"]:
        return get_node(root["left"],key)
    else:
        return get_node(root["right"],key)
    
def get(my_bst,key):
    
    return get_node(my_bst["root"],key)

def size_tree(root):
    if root is None:
        return 0
    return root["size"]

def size(my_bst):
    return size_tree(my_bst["root"])
    