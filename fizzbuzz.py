L1=[1,2,3,4,5,6]
L2=[1,2,3,4,5,6,7,8,9]
def fizzbuzz():
    L1 = input('enter a list for L1:')
    L2 = input('enter a list for L2:')
    l = L1 + L2
    number =len(l)
    if number%3==0 and number%5==0:
        print("fizzbuzz")
    elif number%3 == 0:
        print("fizz")
    elif number%5 == 0:
        print ("buzz")
    else:
        print (number)    
fizzbuzz()