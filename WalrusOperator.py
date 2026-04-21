a = True
print(a:= False) # it will assign False to a and then print the value of a

# Using walrus operator in while loop
numbers = [1,2,3,4,5]
while(n:= len(numbers))> 0:
    print(numbers.pop())

foods = list()
while(food:=input("What food do you like? ")!="quit"):
    foods.append(food)
print("You like these foods:",foods)
    