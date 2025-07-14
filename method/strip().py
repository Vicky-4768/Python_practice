from Func_lib import open_file

# Run this script to open the HTML file in the default web browser
open_file("C:\\Users\\Rampage\\Desktop\\Python_prac\\method\\html\\strip().html")



# The strip() method remove leading and traling whitespace.
    # Ex.
fruit = "   banana   "
print(f"i want to eat {fruit}!") # outhput - i want to eat    banana    !
fruit1 = fruit.strip()
print(f"i want to eat {fruit1}!") # outhput - i want to eat banana! 


# you can specify any charector to remove, if not, white space will remove.
    # Ex. 
fruit = "qq,,,ffbanana,,,ssdds"
print(f"i want to eat {fruit}!") # outhput - i want to eat    banana    !
fruit1 = fruit.strip("sdq,f")
print(f"i want to eat {fruit1}!") # outhput - i want to eat banana! 

