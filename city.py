class City:
    def __init__(self, name, pop1972, pop1981, pop1998, pop2017):
        self.__city_name = name
        self.__pop_1972 = pop1972
        self.__pop_1981 = pop1981
        self.__pop_1998 = pop1998
        self.__pop_2017 = pop2017
    
    def __str__(self):
        return f"{self.__city_name.ljust(20)}\t{self.__pop_1972}\t{self.__pop_1981}\t{self.__pop_1998}\t{self.__pop_2017}"

    def get_city_name(self):
        return self.__city_name
    
    def get_pop_1972(self):
        return self.__pop_1972
    
    def get_pop_1981(self):
        return self.__pop_1981
    
    def get_pop_1998(self):
        return self.__pop_1998
    
    def get_pop_2017(self):
        return self.__pop_2017
