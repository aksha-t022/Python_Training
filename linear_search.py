arr = [1,10,20,25,87,97,11,12]
key = int(input("Enter element to search: "))

found = False
for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at index", i)
        found = True
        break

if not found:
    print("Element not found")