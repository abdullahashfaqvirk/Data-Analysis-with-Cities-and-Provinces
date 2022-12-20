from city import *

class Province:
    def __init__(self, province_name):
        self.__province = province_name
        self.__count = 0
        self.__arr = []

    def __str__(self):
        s = f"***** {self.__province}\t{self.__count} Cities *****\n{'-'*45}\n"
        for obj in self.__arr:
            s += f"{obj}\n"
        return s

    def add_city(self, obj):
        self.__count += 1
        self.__arr.append(obj)

    def get_cities_2017_population(self):
        s = f"*** {self.__province}\t{self.__count} Cities ***\n{'-'*40}\n"
        for obj in self.__arr:
            s += f"{obj.get_city_name().ljust(20)}\t{obj.get_pop_2017()}\n"
        return s

    def get_province_count(self):
        return self.__count
