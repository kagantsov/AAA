from operator import add


class Color:
    """Класс, работющий с RGB"""
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'
    MAX_LEVEL = 255
    MIN_LEVEL = 0

    def __init__(self, red_level, green_level, blue_level):
        """Конструктор"""
        self._validate_level(red_level)
        self._validate_level(green_level)
        self._validate_level(blue_level)
        self.rgb = (red_level, green_level, blue_level)

    def _validate_level(self, level):
        """Проверка входящих значений на соответствие формату RGB"""
        if level > self.MAX_LEVEL or level < self.MIN_LEVEL:
            raise ValueError(f'RGB should be in range {self.MIN_LEVEL, self.MAX_LEVEL}')

    def __repr__(self):
        """Точка, покрашенная в заданный цвет"""
        return (f'{self.START};{self.rgb[0]};{self.rgb[1]};'
                f'{self.rgb[2]}{self.MOD}●{self.END}{self.MOD}')

    def __eq__(self, other):
        """Сравнение заданных цветов"""
        if isinstance(other, self.__class__):
            return self.rgb == other.rgb
        return False

    def __add__(self, other):
        """Смешивание заданных цветов"""
        if isinstance(other, self.__class__):
            return self.__class__(*map(add, self.rgb, other.rgb))  # use add or lambda x, y: x + y
        return False

    def __hash__(self):
        """Вывод уникальных цветов через set"""
        return hash(self.rgb)

    def __mul__(self, contrast):
        """Уменьшение контраста по формле для изменения яркости"""
        if not (isinstance(contrast, float) or isinstance(contrast, int)):
            raise TypeError(f"{type(contrast)} != float")

        if not 0 <= contrast <= 1:
            raise ValueError(f"Contrast should be between 0 and 1, got {contrast}")

        cl = -256 * (1 - contrast)
        f = 259 * (cl + 255) / (255 * (259 - cl))

        new_red_level = int(round(f * (self.rgb[0] - 128)) + 128)
        new_green_level = int(round(f * (self.rgb[1] - 128)) + 128)
        new_blue_level = int(round(f * (self.rgb[2] - 128)) + 128)

        return self.__class__(new_red_level, new_green_level, new_blue_level)

    def __rmul__(self, contrast):
        """Вывод цвета, с измененной яркостью"""
        return self.__mul__(contrast)


if __name__ == '__main__':
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    orange1 = Color(255, 165, 0)
    orange2 = Color(255, 165, 0)
    color_list = [red, green, orange1, orange2]
    c = 0.9

    print(red)
    print(red == green)
    print(red != green)
    print(red + green)
    print(set(color_list))
    print(red * c)
