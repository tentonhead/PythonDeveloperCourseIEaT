# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, separator=','):
    first_group = first_group.split(separator)
    second_group = second_group.split(separator)
    common = []
    for i in first_group:
        for j in second_group:
            if i == j:
                common.append(i)
    common.sort()
    return common

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common = find_common_participants(participants_first_group,
                                  participants_second_group,
                                  separator='|')
print(common)