def max_sum_subarray(A):
    """
    Given an array of positive and negative integers,find the maximum sum contiguous subarray.
    Takes list as input.
    """
    max_sum = A[0]
    current_sum = max_sum
    start=end=sp=ep=0
    length=templen=1
    for i in range(1,len(A)):
        if(A[i] > (current_sum + A[i])):
            if(A[i] > current_sum):
                current_sum = A[i]
                sp=i
                ep=i
                if (current_sum >= max_sum):
                    max_sum = current_sum
                    if ((ep-sp+1) >= length):
                        start = sp
                        end = ep
                        length = ep-sp+1
            else:
                sp=i
                ep=i
            current_sum = A[i]              
        else:
            if(A[i]>=0):
                current_sum += A[i]
                ep = i
                if (current_sum >= max_sum):
                    max_sum = current_sum
                    if ((ep-sp+1) > length):
                        start = sp
                        end = ep
                        length = ep-sp+1
            else:
                if (current_sum >= max_sum):
                    max_sum = current_sum
                    if ((ep-sp+1) > length):
                        start = sp
                        end = ep
                        length = ep-sp+1
                        sp=i
                        ep=i
                current_sum = A[i]
    return start,end,max_sum

A = input("Please enter the input array\n")
s,e,su = max_sum_subarray(A)
print("Maximum Sum Subarray = %s\nSum = %d\n"%(str(A[s:e+1]),su))
