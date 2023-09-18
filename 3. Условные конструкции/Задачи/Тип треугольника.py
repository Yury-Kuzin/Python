first_side_triangle = int(input("Введите первую сторону треугольника: "))
second_side_triangle = int(input("Введите вторую сторону треугольника: "))
third_side_triangle = int(input("Введите третью сторону треугольника: "))
if first_side_triangle + second_side_triangle <= third_side_triangle or \
        first_side_triangle + third_side_triangle <= second_side_triangle or \
        second_side_triangle + third_side_triangle <= first_side_triangle:
    print("Impossible")
else:
    h = max(first_side_triangle, second_side_triangle, third_side_triangle)
    c1 = min(first_side_triangle, second_side_triangle, third_side_triangle)
    c2 = first_side_triangle + second_side_triangle + third_side_triangle - (h + c1)
    if h ** 2 == c1 ** 2 + c2 ** 2:
        print("Rectangural")
    elif h ** 2 > c1 ** 2 + c2 ** 2:
        print("Obtuse")
    else:
        print("Acute")
