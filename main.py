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