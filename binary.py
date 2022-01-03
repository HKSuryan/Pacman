
'''number = int(input("Enter the number to find:"))

listu = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
         51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]


def insertionsort(array):

    # Traverse through 1 to len(arr)
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array


listu = insertionsort(listu)
print("Sorted array", listu)
global found, store, j
j = 1
found = False
store = 0


def binarysearch(number, listu):

    global found, store, j
    print(f"the {j} time")
    j += 1

    if len(listu) == 1:
        if number in listu:
            print(f"Found the number at {store}")
            found = True
        return 0

    if len(listu) % 2 == 0:

        middle_element_index = int((len(listu)/2)-1)

        store += middle_element_index+1

        print("stored middle value", store)

        middle_element = listu[middle_element_index]
        print("The middle element is ", middle_element)
        if middle_element == number:
            print(
                f"Found the number at source1 {store}")
            found = True

        else:
            if number > middle_element:
                newlist = listu[middle_element_index+1:]
                print("The new lsit is ", newlist)
                binarysearch(number, newlist)

            elif number < middle_element:
                newlist = listu[:middle_element_index]
                print("The new lsit is ", newlist)
                subtract = middle_element-number+1
                store -= subtract
                if j == 2:
                    store = 0
                binarysearch(number, newlist)

    elif len(listu) % 2 != 0:
        length = int(len(listu)//2)
        middle_element_index = length
        if length == 0 and number == 7:
            store += middle_element_index
        else:
            store += middle_element_index+1

        middle_element = listu[middle_element_index]
        print("The middle element is ", middle_element)
        if middle_element == number:
            print(
                f"Found the number at source2  {store}")
            found = True

        else:
            if number > middle_element:
                newlist = listu[middle_element_index+1:]
                print("The new lsit is ", newlist)
                binarysearch(number, newlist)

            elif number < middle_element:
                newlist = listu[:middle_element_index]
                print("The new lsit is ", newlist)
                subtract = middle_element-number+1
                store -= subtract
                if j == 2:
                    store = 0
                binarysearch(number, newlist)

    elif found == False:
        print("The number is not in the array")


binarysearch(number, listu)
'''


'''def binary_search(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1

'''


def binarysearch(array, low, high, number):
    if high >= low:
        mid_element_index = (high+low)//2
        mid_element = array[mid_element_index]

        if number == mid_element:
            return mid_element_index
        elif number > mid_element:
            return binarysearch(array, mid_element_index+1, high, number)
        else:
            return binarysearch(array, low, mid_element_index-1, number)

    else:
        return -1


# Test array
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
       51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
x = int(input("Enter the number to be found"))

# Function call
result = binarysearch(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index", str(result+1))
else:
    print("Element is not present in array")
