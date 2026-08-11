import math

# Input variables
x1 = float(input("Enter x1: "))         
y1 = float(input("Enter y1: "))

# Input variables
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))


# Calculate the distance between the two points
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Display the calculated distance
print("The distance between the two points is:", distance)

#Using a library is more practical than writing all calculations because it saves time by using easy to use functions. It saved time and made the distance calculation clean and easy to read. If I wrote all calculations from scratch, it would've probably took a long time and I would've made mistakes.
