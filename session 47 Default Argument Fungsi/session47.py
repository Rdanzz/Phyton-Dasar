# Default Argument

def greet(name="User"):
    print(f"Hello, {name}!")

greet()
greet("Alice")

# Keyword Argument
def greet_with_age(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet_with_age(name="Alice", age=25)
greet_with_age(age=30, name="Bob")
