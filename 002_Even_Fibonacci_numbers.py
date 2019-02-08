'''Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''
myarg = input("enter max limit: ")

def even_fibonnaci_sum(maxlimit):
    sum=0
    prev_term=1
    curr_term=2
    for i in range(1, int(maxlimit)+1, 1):
        next_term=prev_term + curr_term
   #     print(str(prev_term)+"  "+str(curr_term)+"___"+str(next_term))
        if prev_term%2==0:
            sum+=prev_term
            
        prev_term=curr_term
        curr_term=next_term
    return(sum)

print(even_fibonnaci_sum(myarg))