my_list = [5, 7, 11, 13, 15, 20, 25]
new_list = []

for elem in my_list:
    if elem > 10:
        new_list.append(elem)

average = sum(new_list) / len(new_list)
print(average)