# YAML - Yet Another Markup Language (Adv. and more readable version of JSON)

from pyaml import yaml

car_info = { "name" : "Mercedes", "model" : "Benz", "year" : 2023, 'price': 100000000}

# Serialization to YAML string

yaml_string = yaml.dump(car_info, sort_keys=False)

print(yaml_string)

# Serialization to YAML File

with open('emp.yaml', 'w') as f:
    yaml.dump(car_info, f)

# De-Serialization from YAML string

new_car = yaml.safe_load(yaml_string)

print(type(new_car))


# Serialization from YAML file

with open("emp.yaml", 'r') as f:
    new_car1 = yaml.safe_load(f)

print(type(new_car1))
