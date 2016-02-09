def fibIter(n):
    # iterative version
    numbers = [0, 1]
    start = 2
    if n == 0 or n == 1:
        return n
    while start <= n:
        prev1 = numbers[start - 1]
        prev2 = numbers[start - 2]
        numbers.append(prev1 + prev2)
        start += 1
    return numbers[n]
    
# for i in range(10):
#     print(str(i+1) + " " + str(fibIter(i)))

# -------------------------------

def fibIter2(n):
    if n == 0 or n == 1:
        return n
    prev2 = 0
    prev1 = 1
    fi = None
    i = 0
    while i < n:
        fi = prev2 + prev1
        prev2 = prev1
        prev1 = fi
        i += 1
    return fi
    
# for i in range(10):
#     print(str(i + 1) + " " + str(fibIter2(i)))
    
# -------------------------------

def fibRec(n):
    if n is 0 or n is 1: return n
    else: return fibRec(n - 2) + fibRec(n - 1)
        
# for i in range(10):
#     print(str(i + 1) + " " + str(fibRec(i)))

# -------------------------------
    
fibLambda = lambda n:reduce(lambda x,n:[x[1],x[0]+x[1]], range(n),[0,1])[0]

print (fibLambda(4))
