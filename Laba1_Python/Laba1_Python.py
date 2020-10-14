import math

squareArea = 20
print("Square Area - ", squareArea)
squareSide = math.sqrt(squareArea)
radius = squareSide/2
print("Circle inscribed in Square Area - ", round(math.pow(radius,2)*3.14, 1))
smallSquareSide = math.sqrt(2)*radius
smallSquareArea = math.pow(smallSquareSide,2)
print("Square Inscribed In Circle Area - ", round(smallSquareArea,1))
a = squareArea/smallSquareArea
print("The area of the insribed square is ",round(a,1)," times less than given square area")

