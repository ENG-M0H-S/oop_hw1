# إنشاء Dynamic Array
students = [10, 20, 30, 40]
print("المصفوفة الأصلية:", students)



# الإضافة في النهاية 
students.append(50)
print("بعد الإضافة في النهاية (append):", students)

# الإضافة في الوسط 
students.insert(2, 25)  # إضافة 25 في الفهرس 2
print("بعد الإضافة في الوسط (insert at index 2):", students)

# الإضافة في البداية 
students.insert(0, 5)  # إضافة 5 في الفهرس 0 (البداية)
print("بعد الإضافة في البداية", students)



# الحذف باسم العنصر 
students.remove(25)  # يحذف أول occurrence للقيمة 25
print("بعد الحذف بالقيمة", students)

# الحذف بالفهرس 
deleted_value = students.pop(1)  # يحذف العنصر في الفهرس 1
print(f"بعد الحذف بالفهرس (pop index 1): {students}، القيمة المحذوفة: {deleted_value}")

# الحذف من النهاية
last_element = students.pop()  # يحذف آخر عنصر
print(f"بعد الحذف من النهاية (pop): {students}، القيمة المحذوفة: {last_element}")
   


البحث الخطي 
x = 40
if x in students:
    y = students.index(x)
    print(f"العنصر {x} في الموقع",y)
else:
    print(x," غير موجود في المصفوفة")



# التعديل عن طريق الوصول المباشر بالفهرس 
print("قبل التعديل:", students)
students[0] = 15  # تعديل العنصر في الفهرس 0
print("بعد تعديل students[0] = 15:", students)

students[2] = 35  # تعديل العنصر في الفهرس 2
print("بعد تعديل students[2] = 35:", students)





matrix = [
     
    [1, 2],
    [3, 4]
    
]

print(matrix[0][1])  # النتيجة 2
print(matrix[1][1])  # النتيجة 3

matrix.append([5, 6])
print(matrix)  # النتيجة [[1, 2], [3, 4], [5, 6]]# الطباعة النهائية للمصفوفة
# print("المصفوفة النهائية:", students)


matrix [0][0] = 10
print(matrix)  # النتيجة [[10, 2], [3, 4], [5, 6]]# الطباعة النهائية للمصفوفة
# print("المصفوفة النهائية:", students)


print("moh")