#Project2
brk = [[1, 2], [3, 4], [5, 6, 7]]
  
def reversed(l):
    l.reverse() # reversed the list
    
    for i in l:
        if type(i)==list:  
            reversed(i)

reversed(brk)
print(brk)
