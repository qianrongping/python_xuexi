students = [
    {'name': 'rubin', 'age': 18},
    {'name': 'jack', 'age': 19},
    {'name': 'ruse', 'age': 20}
]
# 按age值升序排列
# students.sort(key=lambda x: x['age'])
# print(students)

# 按age值降序排列
students.sort(key=lambda x: x['age'], reverse=True)
print(students)
print('124')