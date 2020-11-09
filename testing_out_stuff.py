
def ternary_partition(l):
    pivot = l[0]
    result = []
    for i in range(1, len(l)-1):
        if l[i] < pivot:
            l.insert((i-1), l.pop(i))

        elif l[i] == pivot:
            l.insert((i+1), l.pop(i))

        else:
            l.insert(len(l), l.pop(i))


    print(l)



print(ternary_partition([3, 2, 2, 5, 6, 3, 1, 3]))