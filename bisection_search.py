# generate sorted array of random ints
n = rand()

# function to generate array of random ints
def rand(n = 20):
    a = []
    for i in range(20):
    a.append(random.randint(0,100))
    a.sort()
    return a
    
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) <= 0:
        return False
    if len(aStr) == 1:
        return char == aStr
        
    midpoint = len(aStr) // 2
    if char == aStr[midpoint]:
        return True
    else: 
        if char < aStr[midpoint]:
            # print("lower")
            return isIn(char, aStr[:midpoint])
        else:
            # print("higher")
            return isIn(char, aStr[midpoint:])
    
print(isIn("o", ""))
print(isIn("o", "a"))
print(isIn('o', 'degmorrrstxxxyy'))
print(isIn('o', 'bfjo'))