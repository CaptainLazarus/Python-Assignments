size = int(input("Enter the size of array  "))
arr = []
for i in range(size):
	ele = input()
	arr.append(ele)

k = input("Enter the element ")
print(arr.count(k))