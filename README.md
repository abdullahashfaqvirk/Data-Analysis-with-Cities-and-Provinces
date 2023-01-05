# Data Analysis with Cities and Provinces

In this project, you will use data from the cities.csv file to create classes representing cities and provinces, and perform various operations on them.

## Classes

The following classes have been defined in this project:

* **City**: a class representing a city. It has the data members city_name, population_1972, population_1981, population_1998, and population_2017, and has the member functions __init__, __str__, and getters for all data members.
* **Province**: a class representing a province. It has the data members province_name, cities_count, and cities, and has the member functions __init__, __str__, add_city, get_count, and get_cities_with_2017_population.
* **Country**: a class representing a country. It has the data members country_name, cities_count, and provinces, and has the member functions __init__, __str__, add_city, print_city_count_province_wise, and get_cities_with_2017_population.

## Getting Started

To use this project, follow these steps:

* Create instances of the City class, passing in the city name and population data for the city as arguments to the __init__ method.
* Create instances of the Province class, passing in the province name as an argument to the __init__ method.
* Use the add_city method of the Province class to add city instances to the province.
* Create an instance of the Country class, passing in the country name as an argument to the __init__ method.
* Use the add_city method of the Country class to add city instances to the country, specifying the province name as an argument.
* Use the __str__ method of the Province and Country classes to display the details of the provinces and countries, respectively.
* Use the print_city_count_province_wise method of the Country class to display the number of cities in each province.
* Use the get_cities_with_2017_population method of the Province and Country classes to display the cities in the provinces or country with a population in 2017.
