# log n

# test case
the_list = [1, 1, 2, 4, 9, 11, 15, 16, 16, 19, 21, 22]
the_value = 2
start_index = 0
end_index = len(theList)
test_index = (start_index + end_index) / 2
print start_index, end_index, test_index

def searchList(theList, theValue):
    print theValue != theList[test_index]
    print theValue, theList[test_index]

    # while theValue != theList[test_index]:
    #     print("inside")
            
    #     if theList[test_index] < theValue:
    #         end_index = test_index
    #     else:
    #         start_index = test_index
            
    # if theList[test_index] == theValue:
    #     print "The value {} is found at index {}.".format(theValue, theList[test_index])
        
searchList(theList, theValue)

