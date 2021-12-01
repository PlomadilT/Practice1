# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
print(task#1)
str = input ( "enter a string: " )
counter = 0 for s in str :
      counter = counter + 1
print ( "the length of the input line:" , counter )

print(task#2)
def string_both_ends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

print(string_both_ends('w3resource'))
print(string_both_ends('w3'))
print(string_both_ends('w'))

print(task#3)
def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]
  return str1
print(change_char('restart'))

print(task#4)
def reverse_string(str1):
    if len(str1) % 4 == 0:
       return ''.join(reversed(str1))
    return str1
print(reverse_string('abcd'))
print(reverse_string('python'))

print(task#5)
incoming_data = input()
words = {for words in incoming_data, .split(',')}
print(",".join(words))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
