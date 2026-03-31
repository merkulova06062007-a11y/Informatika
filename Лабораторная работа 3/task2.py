def find_common_participants(str1, str2, separator=','):

    list1 = str1.split(separator)
    list2 = str2.split(separator)

    common_set = set(list1) & set(list2)

    common_list = sorted(list(common_set))

    return common_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, "|")
print(f'Общие участники: {result}')