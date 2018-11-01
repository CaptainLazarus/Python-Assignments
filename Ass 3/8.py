size = int(input("Enter the size of array  "))
arr = []
for i in range(size):
	ele = input()
	arr.append(ele)

index = int(input("Enter the index value of element you want to remove "))
arr.pop(index)
print("Array after popping out element -->>  ",arr)