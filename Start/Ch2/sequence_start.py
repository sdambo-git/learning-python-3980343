# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
mylist = [0, 1, "two", 3.2, False]
# print(len(mylist))

# to access a member of a sequence type, use []
# print(mylist[2])  
# print(mylist[-1])
# mylist[0] = 10
# print(mylist)

# add a list to another list
# another_list = [6, 7, 8]
# mylist += another_list
# print(mylist)

# mystr = "This is a string"
# print(mystr[5])
# mystr[2]="X"

# use slices to get parts of a sequence
# print(mylist[1:4]) # prints elements from index 1 to 3
# print(mylist[1:4:2]) # prints every second element from index 1 to 3
# print(mylist[:4]) # prints elements from index 0 to 3
# print(mylist[::2]) # prints every second element from the whole list

# you can use slices to reverse a sequence
#print(mylist[::-1]) # prints the whole list in reverse order

# Tuples are like lists, but they are immutable
mytuple = (0, 1, "two", 3.2, False)
# print(mytuple)
# print(mytuple[2])
# mytuple[0] = 2 # this will cause an error, tuples cannot be modified

# Sets are also sequences, but they contain unique values
myset = {0, 1, "two", 3.2, 3.2 ,False}
print(myset)  # prints the set, note that duplicates are removed

# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error
# print(myset[0])  # this will cause an error

# Test for membership
print(1 in myset)  # prints True, since 1 is in the set
print(3 in mytuple) # prints False, since 3 is not in the tuple
print(5 not in mylist)  # prints True, since 5 is not in the list