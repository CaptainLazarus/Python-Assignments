from statistics import median
size = int(input("Enter the size of array  "))
arr = []
for i in range(size):
	ele = int(input())
	arr.append(ele)
mean = sum(arr)/len(arr)
Median = median(arr)
count_ = 0
for i in arr:
	if arr.count(i) > count_:
		count_ = arr.count(i)
		k = i
mode = k	
print("The Mean , Median , Mode are {} ,{} ,{} respectively".format(mean,Median,mode))			