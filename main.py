# Создать классы фигура, прямоугольник, квадрат, круг и эллипс.
# Реализовать методы вычисления площади

class Kvadrat:
    def __init__(self, Storona):
        self.Storona = Storona
        pkv = Storona * Storona
        print("Площадь Квадрата: ", pkv)

kv = float(input("Ведите сторону квадрата: "))
pkv = Kvadrat(kv)


class Pryamougolnik:
    def __init__(self, StoronaA, StoronaB):
        self.StoronaA = StoronaA
        self.StoronaB = StoronaB
        pkv = StoronaA * StoronaB
        print("Площадь прямоугольника: ", pkv)

storonaA = float(input("Ведите сторону прямоугольника А: "))
storonaB = float(input("Ведите сторону прямоугольника Б: "))
ppu = Pryamougolnik(storonaA, storonaB)


class Krug:
    def __init__(self, Radius):
        self.Radius = Radius
        pk = 3.14159 * (Radius * Radius)
        print("Площадь круга: ", pk)

rk = float(input("Ведите радиус круга: "))
pk = Krug(rk)



class Elips:
    def __init__(self, R, r):
        self.R = R
        self.r = r
        pe = 3.14159 * R * r
        print("Площадь элипса: ", pe)

R = float(input("Ведите большую полуось: "))
r = float(input("Ведите введите малую полуось: "))
pe = Elips(R, r)