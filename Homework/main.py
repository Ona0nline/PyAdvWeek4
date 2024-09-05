populations = [
  { 'country': "France", "population": "60000000"},
  { 'country': "Spain", "population": "50000000"},
  { 'country': "USA", "population": "30000000"},
  { 'country': "Australia", "population": "25000000"},
  { 'country': "Canada", "population": "38000000"},
]

# data already here

"""Population count"""

total_population = 0 



for population_figure in populations:
  """Iterating through populations list of dictionary using population figure index"""
  # Leave the original list/dictionary out of it
  population_value = int(population_figure['population'])
  total_population += round(population_value/ 1000000)
  
print(f"The total population is {total_population} million people")  

# Display the total population such as, the total population is 203 million people