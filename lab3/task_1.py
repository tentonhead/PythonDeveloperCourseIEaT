# TODO Напишите функцию для поиска индекса товара
def first_entry(items_list, item):
    """Returns first found index of item. None if item is absent."""
    for i in range(len(items_list)):
        if items_list[i] == item:
            return i
        else:
            continue
    return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = first_entry(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
