def max_sum_subarray(A):
    """
    Given an array of positive and negative integers,find the maximum sum contiguous subarray.
    Takes list as input.
    """
    max_sum = 0
    current_sum = 0
    start=0
    end=0
    for i in range(0,len(A)):
        if(A[i] > (current_sum + A[i])):
            current_sum = A[i]
            start = i
            end = i
        else:
            current_sum += A[i]
        if (current_sum > max_sum):
            max_sum = current_sum
            end = i
    return start,end,max_sum

A = input("Please enter the input array\n")
s,e,su = max_sum_subarray(A)
print("Maximum Sum Subarray = %s\nSum = %d\n"%(str(A[s:e+1]),su))
