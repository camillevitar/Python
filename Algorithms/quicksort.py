#Quicksort sin el pivote aleatorio

L = 1
def qsort():
    if L == []: return []
    return qsort([x for x in L[1:] 
if x< L [0]]) + L[0:1] + \
        qsort([x for x in L[L:1] 
if x>=L[0]])

