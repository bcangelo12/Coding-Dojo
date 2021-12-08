#countdown
def countdown(start):
    return list(range(start, -1, -1))
print(countdown(7))

#print and return
def print_and_return(num_list):
    print(num_list[0])
    return num_list[1]
print(print_and_return([1,2]))

#first plus length
def first_plus_length(list):
    return list[0] + len(list)
print(first_plus_length([17, 4, 6, 0, 10, 21]))

#values greater than second
def values_greater_than_second(list):
    a = []
    if len(list) >= 2:
        for x in list:
            if x > list[1]:
                a.append(x)
        print(len(a))
        return a
    else:
        return False
print(values_greater_than_second([1,3,7,2,8,9]))
print(values_greater_than_second([4]))

#this length, that value
def length_and_value(size,value):
    a = [value] * size
    return a
print(length_and_value(5,10))
print(length_and_value(15,2))