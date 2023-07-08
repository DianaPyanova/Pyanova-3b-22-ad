coordinates = [(1, 2), (3, 4), (-1, 5), (6, -3)]
new_list = []
for coordinate in coordinates:
    x, y = coordinate[0], coordinate[1]
    new_list.append((x ** 2 + y ** 2) ** 0.5)

new_list.sort()
print(new_list)