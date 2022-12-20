from province import *

class Country:
    def __init__(self, country_name):
        self.__country = country_name
        self.__count = 0
        self.__dic = {}
        self.__dic['Punjab'] = Province('Punjab')
        self.__dic['Sindh'] = Province('Sindh')
        self.__dic['Balochistan'] = Province('Balochistan')
        self.__dic['KPK'] = Province('KPK')

    def __str__(self):
        s = f"<<<<< {self.__country} {self.__count} Cities >>>>>\n"
        for obj in self.__dic.values():
            s += f"{obj}\n"
        return s


    def add_city(self, province_name, obj):
        for i, j in self.__dic.items():
            if i.lower() == province_name.lower():
                j.add_city(obj)
                self.__count += 1

    def print_city_count_province_wise(self):
        for i, j in self.__dic.items():
            print(f"Count in {i} is {j.get_province_count()}")

    def get_cities_with_2017_population(self):
        s = f"<<<<< {self.__country} >>>>>\n"
        for j in self.__dic.values():
            s += f"{j.get_cities_2017_population()}\n"
        return s
