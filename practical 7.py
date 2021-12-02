# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
print(task2)
def isPalindrome(s):
    return s == s[::-1]
s = "malayalam"
ans = isPalindrome(s)
if ans:
    print("True")
else:
    print("False")

print(task4)
def LongestWordLength(str):
    n = len(str)
    res = 0;
    curr_len = 0
 for i in range(0, n):
        if (str[i] != ' '):
            curr_len += 1
        else:
            res = max(res, curr_len)
            curr_len = 0
  return max(res, curr_len)
print(LongestWordLength)

print(task5)
n = int(input())
result = 0
for i in n:
   if int(i) % 2 != 0:
    result += int(i)
print(result)

print(task6)
n = str(bin(int(s)))[2:]
result = 0
for i in n:
    result += int(i)
print(result)








# See PyCharm help at https://www.jetbrains.com/help/pycharm/
