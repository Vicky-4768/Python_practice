# 9-1. Restaurant: Make a class called Restaurant .  
class Restaurant():
# The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type .
    def __init__(self, name, type ):
        self.restaurant_name = name
        self.cuisine_type = type

# Make a method called describe_restaurant() that prints these two pieces of information, 
    def describe_restaurant(self):
        info = (f"{self.restaurant_name} restaurant\nthe {self.cuisine_type} restaurant")
        print(f"{info}".title())

# and a method called open_restaurant() that prints a message indicating that the restaurant is open .
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is available.".title())
        print("thanks for coming".title())

# Make an instance called restaurant from your class . Print the two attributes individually, and then call both methods.
r1 = Restaurant("Jhony", "Italian" )
r1.describe_restaurant()
r1.open_restaurant()
print(r1.restaurant_name)
print(r1.cuisine_type)
# 9-2. Three Restaurants: Start with your class from Exercise 9-1 . Create three different instances from the class, and call describe_restaurant() for each instance .
r2 = Restaurant("ramesh", "southindian")
r3 = Restaurant("max","maxican")
r2.describe_restaurant()
r2.open_restaurant()
r3.describe_restaurant()
r3.open_restaurant()

# 9-3. Users: Make a class called User . Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile .
class User:
    first_name = input("Enter your First Name: ")
    last_name = input("Enter your Last Name: ")
    # age = input(int("Enter your Age: "))
    # std = input(int("Enter your Standard: "))
    # id = input(int("Enter your ID: "))

    

# Make a method called describe_user() that prints a summary of the user’s information . 
    def describe_user(self):
        print(f"user name is {User.first_name}"
              f"\nuser last name is {User.last_name}")
            #   f"\nuser age is {User.age}"
            #   f"\nuser std is {User.std}"
            #   f"\nuser id is {User.id}")

# Make another method called a personalized greeting to the user greet_user() that prints.
    def greet_user(self):
        print(f"Hello {User.first_name} {User.last_name}, welcome to our Chutiyapa.com!")

# Call above methods
    def call_method(self):
        self.describe_user()
        self.greet_user()

# Create several instances representing different users, and call both methods for each user .
u1 = User()
u2 = User()

u1.call_method()






