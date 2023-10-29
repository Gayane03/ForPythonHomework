import random

'''a = [1, 2, 3, 4, 5]
b = [i * 2 for i in a]
number=random.shuffle([1,2,3,4])
print(number)'''

matrix=[]

for _ in range(5):
   row=[]
   for _ in range(5):
      row.append(random.randint(0,10))
   matrix.append(row)   


   for item in matrix:
      print(row)
