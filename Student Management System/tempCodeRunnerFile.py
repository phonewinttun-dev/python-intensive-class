def search_item(id_to_find, items):
    for item in items:
        if item['ID'] == id_to_find:
            return item
    else:
        return None
