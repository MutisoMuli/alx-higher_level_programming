def delete_at(my_list, idx):
    if 0 <= idx < len(my_list):
        my_list.pop(idx)
    return my_list
