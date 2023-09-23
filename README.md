# patika.dev_python1
b = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
b1 = []

def flatten(n):
    for i in n :
        if isinstance(i,list): # check if it's a list
            flatten(i) # If it is a list, send it to the flatten function again
        else:
            l1.append(i)

flatten(l)
print(b1)
