#Given three integers, X Y Z, representing dimensions of a cuboid with an integer n.
#Print all possible coordinates on a 3d grid where the sum of i+j+k does not equal n.
#Use list comprehension to solve the problem


#Python 2 Solution
if __name__ == '__main__':
    x = int (raw_input()) 
    y = int (raw_input())
    z = int (raw_input()) 
    n = int (raw_input()) 
    print [ [ i, j, k] for i in range( x + 1) for j in range( y + 1) for k in range( z + 1) 
                                                                 if ( ( i + j + k ) != n )]
   
#Python 3 Solution
if __name__ == '__main__':
    x = int(input()) 
    y = int(input())
    z = int(input()) 
    n = int(input())
    print([[ i, j, k] for i in range( x + 1) for j in range( y + 1) for k in range( z + 1) 
                                                               if ( ( i + j + k ) != n )])   
