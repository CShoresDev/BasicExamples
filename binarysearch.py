some_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# iterative approach. Binary Search algorithm ("Binary Chop")
def binary_search(data: [int], value: int) -> int:

    tries = 0

    high = len(data) - 1
    low = 0
    mid = low + (high - low) // 2

    while high >= low:

        if data[mid] == value:

            print("{} was found".format(data[mid]))
            tries += 1
            print("found {0} in {1} try(ies)".format(data[mid], tries))
            return data[mid]

        elif data[mid] > value:

            high = mid - 1
            mid = low + (high - low) // 2
            tries += 1
            continue

        else:

            low = mid + 1
            mid = low + (high - low) // 2
            tries += 1
            continue

    print("{0} was NOT found! and was searched in {1} try(ies)".format(value, tries))
    return -1


print("******************************************")
print("{} was returned".format(binary_search(some_data, 0)))
print("******************************************")
print("{} was returned".format(binary_search(some_data, 1)))
print("******************************************")
print("{} was returned".format(binary_search(some_data, 2)))
print("******************************************")
print("{} was returned".format(binary_search(some_data, 3)))
print("******************************************")
print("{} was returned".format(binary_search(some_data, 4)))
print("******************************************")
print("{} was returned".format(binary_search(some_data, 5)))
print("******************************************")
print("{} was returned".format(binary_search(some_data, 6)))
print("******************************************")
print("{} was returned".format(binary_search(some_data, 7)))
print("******************************************")
print("{} was returned".format(binary_search(some_data, 8)))
print("******************************************")
print("{} was returned".format(binary_search(some_data, 9)))
print("******************************************")
print("{} was returned".format(binary_search(some_data, 10)))
print("******************************************")
print("{} was returned".format(binary_search(some_data, 100)))
print("******************************************")
print(str(binary_search(some_data, -100)) + " was returned...")
print("******************************************")
