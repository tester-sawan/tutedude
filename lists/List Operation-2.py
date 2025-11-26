# List operations - extend, remove, pop
#1. extend() - Add multiple element in  a list
fruit = ["apple","Banana"]
print(fruit)
fruit.extend(["Grapes","Orange"])
print(fruit)
#2. remove() - remove an specified element
fruit.remove("Orange")
print(fruit)
#3. pop() - remove the element based on index position and returns the deleted element.
removed_element = fruit.pop(2)
print(fruit)
print(removed_element)
