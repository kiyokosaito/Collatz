# The number we will perform the Collatz opperation on.
n = int(input ("Enter a positive integer : "))

# Keep looping until we reach 1.
# Note : this assumes the Collatz congecture is true.

while n != 1:
    # Print the current value of n.
    print (n)
    #chech if n is even.
    if n % 2 == 0:
        #If n is even, divede it by two.
        n = n / 2
    else : 
        #If n is odd, multiply by three and add 1.
        n = (3 * n ) + 1

#Finally, print the 1.
print (n)