#Problem 1
#Debugging, make notes about errors as you go

#Problem 2
numbers = range(21)
test_list = list(numbers)
print(test_list)
#I had an error message here, however I don't know if I'm at fault
#Upon first running this code, I received a message saying:
#'range' object is not callable
#but after restarting the kernel it works just fine lol

#Problem2.2
def list_squarer(list_s):
    squared_list = []
    for value in list_s:
        squared_list.append(value**2)
    return squared_list
#Got an error for forgetting the colon after the for loop, followed inevitably by an indent error
list_squared = list_squarer(test_list)
print(list_squared)

#Problem 2.3

slicing_list = list_squared[0:15]

#Problem 2.4
stride_list = list_squared[0:21:5]

#Problem 2.5
slice_stride = list_squared[-4:0:-3]

#Problem 3
def matrix_generator(a, b):
    matrix = [list(range(i * a + 1, (i + 1) * b + 1)) for i in range(a)]
    return matrix

test_mat = matrix_generator(5, 5)

#Problem 3.2
def matrix_editor(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 3 == 0:
                matrix[i][j] = "?"
    return matrix
#I honestly lost track of the errors here, and I also had to google using double brackets to select specific elements
new_mat = matrix_editor(test_mat)

#Problem 3.3
def matrix_sum(matrix):
    total_sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != "?":
                total_sum += matrix[i][j]
    return total_sum

#Got an error for forgetting to assign an initial value to total sum