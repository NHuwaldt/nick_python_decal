#Problem 1

#1: You can use pwd to see what the working directory is

#2 ls lists the elements in a directory

#3 to update the homework file, you would use commands "cd python_decal" followed by "git clone 'link' "
#which should override files with the same name (or provide an option to)

#4 to move the homework file, you would need to use "mv" followed by the file and then the 
#pathway to the new desired location

#5 to view the file, we could use "nano" which also allows us to edit the file

#6 to edit the file, "nano" will open the text editor

#7 to upload the homework to the online repository, we use:
# git add .
# git commit -m "message"
#git push origin (master/main)

#8 

#9 to shorthand the absolute path, we can use "~ cd/Recent"


#Problem 2

#1
def type_writer(object): 
    return print(type(object))

#2
def even_or_odd(value):
    if value % 2 == 0:
        print("even")
    else:
        print("odd")
    return print(f"Remainder:", {value%2})


#Problem 3

def list_sum(list):
    value = 0
    i = 0
    while i < len(list):
        value += list[i]
        i+=1
    return value


#Problem 4

#1
def list_doubler(input_list):
    return [i for i in input_list for j in range(2)]

#2
def square(num): #missing colon
    return num * num
