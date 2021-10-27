integers = []
for i in range(2):
    integers.append(int(input('Enter %i int number: ' % (i + 1))))
print('Formatted int numbers:\n%s' % '\n'.join('%5i' % number for number in integers))

floats = []
for i in range(4):
    floats.append(float(input('Enter %i real number: ' % (i + 1))))
print('Formatted real numbers with floating point: \n%s' % '\n'.join('%10f' % number for number in floats))
print('Formatted real numbers with fixed point: \n%s' % '\n'.join('%7.4f' % number for number in floats))

print('Formatted string: %4s' % input('Enter random string: ')[:3])

boolean = True
print('Formatted boolean: %s' % boolean)