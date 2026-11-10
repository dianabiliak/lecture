class Stadion:

    def __init__(self, name = "Без назви", number_of_spectators = 0, lighting_power = 0, year_opened = 0, location = "невідомо"):
        self.__name = name
        self.__number_of_spectators = number_of_spectators
        self.__lighting_power = lighting_power
        self.year_opened = year_opened
        self.location = location

    def get_number_of_spectators(self):
        return self.__number_of_spectators
    def get_name(self):
        return self.__name
    def get_lighting_power(self):
        return self.__lighting_power

    def __str__(self):
        return f"Назва стадіону: {self.__name}, кількість глядачів: {self.__number_of_spectators}, сила освітлення: {self.__lighting_power}, рік відкриття: {self.year_opened}, місто розташування: {self.location}"

    def __repr__(self):
        return f"Stadion(name='{self.__name}', number_of_spectators={self.__number_of_spectators}, lighting_power={self.__lighting_power}, year_opened= {self.year_opened}, location= '{self.location}'"

    def __del__(self):
        print(f"Об'єкт {self.__name} видалено з пам'яті")

    def __add__(self, value):
        if isinstance(value, int):
            return Stadion(self.__name, self.__number_of_spectators + value, self.__lighting_power, self.year_opened, self.location)
        return NotImplemented


def main():
    st1 = Stadion()
    st2 = Stadion("Україна", 28000, 1200, 1653, "Львів")
    st3 = Stadion("Локомотив", 1631, 500, 1925, "Київ")
    print(st1)
    print(st2)
    print(st3)
    print(st1 + 20)
if __name__ == "__main__":
    main()