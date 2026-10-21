students = [
    ("Alice", 78),
    ("Bob", 45),
    ("Charlie", 90),
    ("Diana", 62),
    ("Kent", 30)
]
print("Student Names and Scores:")
for name, score in students:
    print(name, score)


print("\nStudents who scored 60 or above:")
for name, score in students:
    if score >= 60:
        print(name)

passed = 0
for name, score in students:
    if score >= 50:
        passed += 1
print("\nNumber of students who passed:", passed)













products = [
    ("Laptop", 1200),
    ("Mouse", 25),
    ("Keyboard", 45),
    ("Monitor", 300),
    ("USB Cable", 10)
]

def check_price(product):
    return product[1] > 100

expensive_products = list(filter(check_price, products))

print("Products costing more than 100:")
print(expensive_products)














points = [
    (2, 3),
    (-1, 4),
    (5, -6),
    (0, 7),
    (-3, -2)
]

def both_positive(point):
    a, b = point

    return a > 0 and b > 0

positive_points = list(filter(both_positive, points))

print("Points where both values are positive:")
print(positive_points)










employees = [
    ("John", "IT", 50000),
    ("Jane", "HR", 45000),
    ("Mike", "IT", 60000),
    ("Sara", "Finance", 70000)
]

for name, department, salary in employees:
    print("Name:", name)
    print("Department:", department)
    print("Salary:", salary)
    print()

it_employees = []
for name, department, salary in employees:
    if department == "IT":
       it_employees.append((name, department, salary))

print("Employees in the IT department:")
for name, department, salary in it_employees:
    print(name, department, salary)

print("\nIT employees earning more than 55,000:")
for name, department, salary in it_employees:
    if salary > 55000:
        print(name)

