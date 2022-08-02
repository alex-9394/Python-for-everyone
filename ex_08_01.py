def chop(list):  # function removing the 1st and the last element
    del list[0]
    del list[-1]


def middle(list):  # func. returns a new list w/ the 1st and the last element
    new_list = list[1:-1]
    return(new_list)


a = [1, 2, 3, 4]
print(middle(a))  # if you put chop(a) 1st, middle(a) returns []-empty brackets
print(chop(a))  # So the order of execution of functions matters
