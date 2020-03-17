# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print('Enter the three lengths of a triangle')

side_1 = int(input('a:'))
side_2 = int(input('b:'))
side_3 = int(input('c:'))

if side_1 == side_2 and side_2 == side_3:
    print(f'A triangle with sides of {side_1}, {side_2} & {side_3} is an equalateral triangle')
elif side_1 != side_2 and side_2 != side_3 and side_1 != side_3:
    print(f'A triange with sides of {side_1}, {side_2} & {side_3} is an scalene triangle')
else:
    print(f'A triangle with sides of {side_1}, {side_2} & {side_3} is a isoceles triangle')
