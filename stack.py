stack = []
#push
stack.append('A')
stack.append('B')
stack.append('C')
#peek
top_element = stack[-1]
print('peek: ',top_element)
#pop
popped_element = stack.pop()
print('Popped_element: ',popped_element)
#stack after pop
print('stack after pop: ',stack)
#isEmpty
isEmpty = not bool(stack)
print('isEmpty: ',isEmpty)
#size
print('size: ',len(stack))