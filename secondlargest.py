  
arr = list(map(int, input("Enter array elements: ").split()))

unique_elements = list(set(arr))

if len(unique_elements) < 2:
    print("Second largest element does not exist")
else:
    unique_elements.sort(reverse=True)
    print("Second largest element:", unique_elements[1])
