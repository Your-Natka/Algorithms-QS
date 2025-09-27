# def merge_two_lists(list1, list2):
#     """Зливає два відсортовані списки в один відсортований список"""
#     merged = []
#     i = j = 0
#     while i < len(list1) and j < len(list2):
#         if list1[i] < list2[j]:
#             merged.append(list1[i])
#             i += 1
#         else:
#             merged.append(list2[j])
#             j += 1
#     # Додаємо залишки
#     merged.extend(list1[i:])
#     merged.extend(list2[j:])
#     return merged

# def merge_k_lists(lists):
#     """Об’єднує k відсортованих списків в один відсортований список"""
#     if not lists:
#         return []
#     while len(lists) > 1:
#         merged_lists = []
#         # Зливаємо списки парами
#         for i in range(0, len(lists), 2):
#             list1 = lists[i]
#             list2 = lists[i+1] if i+1 < len(lists) else []
#             merged_lists.append(merge_two_lists(list1, list2))
#         lists = merged_lists
#     return lists[0]

# # Приклад використання
# lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
# merged_list = merge_k_lists(lists)
# print("Відсортований список:", merged_list)

def merge_lists(list1, list2):
    # Індекси для ітерації по спискам
    i, j = 0, 0
    merged_list = []
    # Проходимо по обох списках і додаємо менший елемент до результуючого списку
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    # Додаємо залишки елементів, якщо вони є
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    return merged_list


def merge_k_lists(lists):
    if not lists:
        return []
    # Починаємо з першого списку
    result_list = lists[0]
    # Послідовно злиття всіх списків з результуючим
    for i in range(1, len(lists)):
        result_list = merge_lists(result_list, lists[i])
    return result_list


if __name__ == "__main__":
    # Приклад виклику функції
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)
