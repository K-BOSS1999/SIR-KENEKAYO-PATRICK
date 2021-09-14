//BinarySearch_In_python//

def BinarySearch (list1, key):
	start = 0
	end = len (list1)-1
	found = False
	while start<= end and not found:
	      mid = (start + end)//2
	      if key == list1[mid]:
	      	found = True
	      elif key>list1[mid]:
	      	start = mid+1
	      else:
	      	end = mid -1
	if found == True:
		print('key is found ')
	else:
		print('key is not found')

list1 = [5,7,9,13,32,32,42,54,56,88]
print(list1)
key = int(input('enter the key: '))
BinarySearch(list1,key)



//Linear_Search_in_python//
def search (list1,key):
	list2 = [ ]
	flag = False  
	for i in range(len(list)):
		if key == list1[i]:
			flag = True
			list2.append(i)
			
			
	if flag == True:
		print('element is found')
		for i in list2:
			print(i)
			
	else:
		print('key is not found')

list1 = [ 34, 23,5,6,7,1,23,8]
print(list1 )
key = int (input("enter the key element: "))
search (list1,key)
