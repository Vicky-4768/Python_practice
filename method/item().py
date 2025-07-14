
from Func_lib import open_file

# Run this script to open the HTML file in the default web browser
open_file("C:\\Users\\Rampage\\Desktop\\Python_prac\\method\\html\\item.html")


#Exercise items()
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(x) # Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

"""
The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.
This view object will reflect any changes done to the dictionary, see example below.
"""
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

car["year"] = 2018

print(x) # Output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2018)])