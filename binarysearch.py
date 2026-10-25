#binary search

numbers = [20,35,40,45,60,65,70,85,90]
tosearch = int(input("Which number are you looking for? "))

def binary_search(start,end):
    if start>end:
        return -1

    middle = (start+end)//2

    if numbers[middle] == tosearch:
        return middle

    elif numbers[middle] > tosearch:
        return binary_search(start, middle -1)
    else:
        return binary_search(middle+1, end)

result = binary_search(0,len(numbers)-1)

if result! = -1:
    print("Numeber found in Index!", result)
else:
    print("Number not found in list.")






