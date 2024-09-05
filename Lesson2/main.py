import csv

# Content already exists
try:
  
  with open("Lesson2/weather.csv","r") as file:
    csv_reader = csv.DictReader(file)
    
    for line in csv_reader:
      print(f"It is {line['temperature']} degrees celsius in {line['city']},{line['country']}")
    
except KeyError:
  print("Temperature header not in the file")