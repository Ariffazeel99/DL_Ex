from pattern import Checker, Circle, Spectrum
from generator import ImageGenerator

if __name__ == "__main__":
    ch = Checker(250, 25)
    ch.draw()
    ch.show(headless=True)

    cir = Circle(200, 25, (100, 30))
    cir.draw()
    cir.show(headless=True)

    spec = Spectrum(1024)
    spec.draw()
    spec.show(headless=True)


    ig = ImageGenerator(r"C:\Users\Ayesha Siddiqui\DL_Ex\exercise0_material\src\data\exercise_data",
                        r"C:\Users\Ayesha Siddiqui\DL_Ex\exercise0_material\src\data\Labels.json", 10, [200, 200, 3],
                        shuffle=True, rotation=True, mirroring=True)
    ig.show(headless=False)
