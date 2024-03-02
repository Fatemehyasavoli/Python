my_list = [1, 2, 5, 4, 5, 3, 5]
element_to_remove = 5
count_removed = 0

while element_to_remove in my_list:
    my_list.remove(element_to_remove)
    count_removed += 1

print("لیست حذف عناصر :", my_list)
print("تعداد عناصر حذفی :", count_removed)
