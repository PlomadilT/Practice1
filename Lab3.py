integer  = [ ]
for i in range(2):
    integers.append(int(input(f'intger {i} :)))
print('Formatted int numbers:'%5i f' % i))

floats = []
for i in range(4):
    floats.append(float(input('Enter %i real number: ' % (i + 1))))
print('Formatted real numbers with floating point: \n%s' % '\n'.join('%10f' % number for number in floats))
print('Formatted real numbers with fixed point: \n%s' % '\n'.join('%7.4f' % number for number in floats))

print('Formatted string: %4s' % input('Enter random string: ')[:3])

boolean = True
print('Formatted boolean: %s' % boolean)