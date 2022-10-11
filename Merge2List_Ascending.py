def merge2ListAsc(A,B)   :
    la = len(A); lb = len(B)
    C = list()
    i = 0; j = 0

    # Merge2List
    while i < la and j < lb :
        if A[i] < B[j] :
            C.append(A[i])
            i += 1
        else :
            C.append(B[j])
            j += 1

    while i < la :
        C.append(A[i])
        i += 1
    while j < lb :
        C.append(B[j])
        j += 1
    return C

A = [2,3,8,15,23,37]
B = [4,6,12,15,20]
C = merge2ListAsc(A, B)
print(C)
