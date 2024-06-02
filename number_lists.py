# create a list of even and odd numbers.
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# use builtin functions to get min and max values of both lists respectively.
print(min(even), max(even), "\n" + "{}".format(min(odd)), max(odd))

# len(iterable) returns the number of characters in a string or the number of elements in a sequence.
print("length of even numbers is %d" % len(even), "\nlength of odd numbers is %2d" % len(odd))

# iterable.count(x) returns the number of occurrences of x in the array.
print(even.count(4), odd.count(7), "\n{}".format("mississippi".count("p")), even.count(8))

# appending to a list. MULTIPLE WAYS!
even.append(10)
even += [12, 14, 16, 18, 20]
odd[len(odd):len(odd)] = [11, 13, 15, 17, 19]

# printing new lists with appended elements.
print(even, "\n{}".format(odd))

# adding a small anonymous list as an element to the list called "even"
even.append([22, 24])
print(even)
