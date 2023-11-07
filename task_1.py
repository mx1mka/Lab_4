class Triangle:
    def is_true(self, a, b, c):
        if (a+b>c and b+c>a and a+c>b):
            print(f"Треугольник со сторонами равными {a}, {b} и {c} существует.")
        else:
            print(f"Треугольник со сторонами равными {a}, {b} и {c} не существует.")
    def square(self, a, b, c):
        p = (a + b + c)/2
        s= (p * (p - a) * (p-b) * (p-c)) ** 0.5
        print(f"Площадь треугольника со сторонами равными {a}, {b} и {c} равна: {s}")
    def perimeter(self, a, b, c):
        print(f"Периметр треугольника со сторонами равными {a}, {b} и {c} равен: {a+b+c}")

a = int(input("Введите сторону а треугольника:"))
b = int(input("Введите сторону b треугольника:"))
c = int(input("Введите сторону а треугольника:"))
tr = Triangle()
tr.is_true(a, b, c)
tr.square(a, b, c)
tr.perimeter(a, b, c)