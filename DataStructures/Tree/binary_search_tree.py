from DataStructures.Tree import bst_node as bst

def new_map():
    return {"root":None}

def insert_node(root,key,value):
    if root is None:
        return bst.new_node(key,value)
    
    if key == root["key"]:
        root["value"] = value
    elif key < root["key"]:
        root["left"] = insert_node(root["left"], key, value)
    else:
        root["right"] = insert_node(root["right"], key, value)
        
    left_size = 0
    if root["left"] is not None:
        left_size = root["left"]["size"]

    right_size = 0
    if root["right"] is not None:
        right_size = root["right"]["size"]

    root["size"] = 1 + left_size + right_size
    
    return root

def put(my_bst, key, value):
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    return my_bst
    