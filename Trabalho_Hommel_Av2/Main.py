from Reader import filter_Data
import ortools

origins, destinies, data = filter_Data("Trabalho_Hommel_Av2\\Input.txt")

for section in data:
    print(section, data[section])