#my_list = [None,None,None,None,None,None,None,None,None,None]
my_list = [[],[],[],[],[],[],[],[],[],[]]

#creating a hash function
def hash_function(value):
    sum_of_chars = 0
    for char in value:
        sum_of_chars += ord(char)
    return sum_of_chars % 10
print("'Bob' has hash code:",hash_function('Bob'))

#inserting an element
def add(name):
    index = hash_function(name)
    my_list[index].append(name) #handling collisions
add('bazu')
add('sally')
add('marvin')
add('lisa')
add('nora')
print(my_list)

#looking up for a name
def contains(name):
    index = hash_function(name)
    #return my_list[index] == name
    return name in my_list[index]
print("'sally' is in the hash table:",contains('sally'))

