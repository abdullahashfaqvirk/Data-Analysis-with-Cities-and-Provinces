from province import *
from city import *


def main():
    punjab = Province('Punjab')

    file = open("cities.csv","rb")
    f = file.read()
    # print(f[:92])
    lines = f.decode("utf-8").split('\n')
    # print(lines[:2])
    for line in lines:
        if line == '':
            break

        s = line.split(',')

        if s[1] == 'Punjab':
            punjab.add_city(City(s[0], int(s[2]), int(s[3]), int(s[4]), int(s[5])))
    file.close()

    print(punjab)
    # print(punjab.get_cities_2017_population())

main()
