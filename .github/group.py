def groups_of_3(list1:list[int])->list[list[int]]:
    return [list1[i:i+3] for i in range(0,len(list1),3)] #start, stop, step

#the function's purpose is to group the elements of an input lists into groups of three values
#each group forms a sublist within a list
#the input is a list of integers
#the output is a nested list with groups of 3 values
#the parameter is type list[int]
#list[list[int]] is returned (i.e. a list of lists)
