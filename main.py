# Создать классы фигура, прямоугольник, квадрат, круг и эллипс.
# Реализовать методы вычисления площади

class Kvadrat:
    def __init__(self, Storona):
        self.Storona = Storona
        pkv = Storona * Storona
        print("Площадь Квадрата: ", pkv)

kv = float(input("Ведите сторону квадрата: "))
pkv = Kvadrat(kv)
