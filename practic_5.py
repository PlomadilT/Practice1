print(task_1)
numbers = int(input())
for i in range(1, 31):
 print(numbers)

 print(task_2)
exam_st_date = (11, 12, 2014)
print( f'The examination will start from : {exam_st_date[0]} / {exam_st_date[1]} / {exam_st_date[2]}',)

print(task_3)
numbers = int(input())
print('list: ', numbers)
print('tuple:', numbers)

print(task_4)
def common_data(list1, list2):
 result = False
 for x in list1:
  for y in list2:
   if x == y:
    result = True
    return result


print(common_data([1, 2, 3, 4, 5]))
print(common_data([1, 2, 3, 4, 5]))

print(task_5)
bus_stop_1 = ([[10,0],[3,5],[5,8]])
bus_stop_2 = ([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]])
bus_stop_3 = ([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]])
people = 0
for bus_stos in bus_stop:
 people += bus_stop[0]
 people -= bus_stop[1]
 return people
print(people_in_bus(bus_stop_1))
print(people_in_bus(bus_stop_2))
print(people_in_bus(bus_stop_3))
