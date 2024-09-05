temperatures = [
  {'city': "Paris", 'continent': "Europe", "temperature": "12"},
  {'city': "Los Angeles", 'continent': "North America", "temperature": "22"},
  {'city': "Paris", 'continent': "Asia", "temperature": "18"},
  {'city': "New York", 'continent': "North America", "temperature": "14"},
  {'city': "Sao Paulo", 'continent': "South America", "temperature": "25"},
  {'city': "Toronto", 'continent': "North America", "temperature": "2"}
]

# Variable to store sum of temperatures and count of North American cities
sum_of_temp = 0
count_of_na_cities = 0

for temp in temperatures:
    if temp['continent'] == 'North America':  # Check if the continent is North America
        temp_value = int(temp['temperature'])  # Convert temperature to an integer
        sum_of_temp += temp_value
        count_of_na_cities += 1

# Calculate the average temperature for North American cities
if count_of_na_cities > 0:
    average_temp = sum_of_temp / count_of_na_cities
    print(f"The average temperature of North American cities is: {average_temp}")
else:
    print("No North American cities found.")
