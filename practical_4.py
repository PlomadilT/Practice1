# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
x = 2 + 3
print(x)
x = 120 / 20
print(x)

x = 3
y = 2
print(0 < x)
print(0 > y)
print(x == y)  # не можу зрозуміти як задати умову для знаків, а не чисел.

x = y = z = 5
print (x)
print (y)
print (z)
x = 2
y = 6
z = -2
print (x == y)
print (x == z)
print (y == z)

x = 3
y = 4
z = y
print(y == z)
x != y

x1 = 2.7
x2 = 1.9
y1 = 2.3
y2 = 4.1
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2)** 0.5
print (distance)
print('whether the first point is above the second', y1 < y2)
def quadrant(x1, y2):
    if (y1 >= 0):
        if (x1 >= 0):
            print(return 1)
        else:
            print(return 2)

        if (x1 >= 0):
            print(return 4)
        else:
            print(return 3)
print( quadrant(x1, y1))
print(quadrant(x1, y1) == quadrant(x2, y2))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
