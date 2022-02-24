# Program to multiply two matrices using nested loops
import random
import numpy as np

N = 250

# NxN matrix
@profile                  #####
def  main(): 
    X=np.random.randint(0,100,(250,250))

# Nx(N+1) matrix
    Y=np.random.randint(0,100,(250,251))
#dot proudct
    Result= np.dot(X,Y)

    print(Result)

main()