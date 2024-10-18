#2 Practicing Slicing and Striding

#2.1, Making a List Variable
list_variable = list(range(21))
print (list_variable)
"""
I didn't encounter an error, but the first time I tried I did the following:
list_variable = (range(21)) 
which did not get me what I wanted. I did some Google searching to figure out the right syntax
"""

#2.2 Working with List Elements
def squareList(list):
    return [i**2 for i in list]


list_variable_squared = squareList(list_variable)
print(list_variable_squared)

"""
I first tried

def squareList():
    for i in list:
        i = i**2
    i = i+1
    return i

which gave me the following error:
line 16, in <module>
    list_variable_squared = squareList(list_variable)
                            ^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: squareList() takes 0 positional arguments but 1 was given

So I tried adjusting to 
def squareList(list)
This didn't give me an error, but it gave me a single answer when what I wanted was a list.
Then I thought I was overcomplicating it, so I took most of the code out to get this:
def squareList(list):
    for i in list:
        return i**2

But that returned a value of 0. So then I went online again to figure out how to better format it.
"""

#2.3 Slicing
def first_fifteen_elements(list):
    return [list[:15]]

print(first_fifteen_elements(list_variable_squared))

#2.4 Striding
def every_fifth_element(list):
    return [list[::5]]

"""
Why doesn't the result in the example include 0?
"""

print(every_fifth_element(list_variable_squared))

#2.5 Slicing and Striding
def fancy_fucntion(list):
    return [list[::-3]]

print(fancy_fucntion(list_variable_squared))

"""
Not sure exactly what to do for that last one because there aren't even 30 elements in the list? 
but the result is the same as in the example
"""

#3 3D Lists

#3.1

def create_2d_list(list_of_lists):
    matrix = []
    element = 1
    for i in range(5):
        insidelist = []
        for j in range(5):
            insidelist.append(element)
            element = element+1
        matrix.append(insidelist)
    return matrix

matrix = create_2d_list(list_variable)
print(matrix)

"""
I'm not gonna lie this one was pretty rough. I didn't end up getting errors in the process I just never got what I actually wanted.
Did a lot of Googling and looking back through older demos to figure stuff out.
"""

#3.2
def modified_2d_list(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 3 == 0:
                matrix[i][j] = '?'
    return matrix
new_matrix = modified_2d_list(matrix)
print (new_matrix)

"""I first tried:

def modified_2d_list(matrix):
    for i in matrix:
        for j in i:
            if (i%3) == 0:
                j = '?'
            else:
                j = j
    return matrix

new_matrix = modified_2d_list(matrix)
print (new_matrix)

And I got the Error:
in modified_2d_list
    if (i%3) == 0:
        ~^~
TypeError: unsupported operand type(s) for %: 'list' and 'int'
I did some more research about this error and figured out I needed more brackets and had to use range and len.
I also didn't need the j = j part.
"""

#3.3
"""I already assigned it to a variable in 3.2 whoops"""

def sum_non_question_elements(some_matrix):
    temp_sum = 0
    for i in range(len(some_matrix)):
        for j in range(len(some_matrix[i])):
            if matrix[i][j] != type(str):
                temp_sum += matrix[i][j]
    return temp_sum

print (sum_non_question_elements(new_matrix))

"""
I first tried:
def sum_non_question_elements(some_matrix):
    temp_sum = 0
    for i in range(len(some_matrix)):
        for j in range(len(some_matrix[i])):
            if j == type(int):
                temp_sum = temp_sum + j
    return temp_sum

Which didn't give me an error, but only returned a value of 0 so I knew I was doing something wrong.
I decided to try a negative conditional instead of a positive one as well as implementing the same brackets as last time
I had to look up the != part

What I have now still gives me a new error:
 in sum_non_question_elements
    temp_sum += matrix[i][j]
TypeError: unsupported operand type(s) for +=: 'int' and 'str'

But I do not know how to fix this because I specified it to only add if matrix[i][j] was not a string. I tried my best :(
"""