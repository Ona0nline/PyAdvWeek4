temperatures = [10, 12, 14, 15]

print(temperatures)
temperatures[1] = 22
print(temperatures)
temperatures.append(19)
print(f"{temperatures[4]}\n\n\n")


# Print the list

# Modify an existing temperature

# Print the modified item

# Add a temperature to the list
# Print the the newly added item


forecast = {
  "Monday": { "temperature": 21, "condition": "Rainy"},
  "Tuesday": { "temperature": 20, "condition": "Sunny"},
  "Wednesday": { "temperature": 23, "condition": "Cloudy"},
  "Thursday": { "temperature": 24, "condition": "Sunny"},
}

print(f"{forecast}\n\n\n")
forecast['Wednesday']['temperature'] = 25
# print(forecast['Wednesday'])
forecast['Wednesday']['condition'] = "Sunny"
print(forecast["Wednesday"])

# Adding a new dictionary to a list of dictionaires
forecast['Friday'] = {"temperature": 27, 'condition': "Cloudy"}
print(forecast)

# Print the dictionary

# Modify Wednesdays temperature to 25 and Sunny

# Print Wednedays temperature

# Add forecast for Friday, 27, Cloudy

# Print Friday temperature such as "Friday's temperature will be 27 degrees and cloudy