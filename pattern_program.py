
no_of_rows = int(input())

for i in range(1,no_of_rows,2):
    print("*"*i)

for j in range(no_of_rows,0,-2):
    print("*"*j)

''' Input : 5

    Output :

 *
 ***
 *****
 ***
 *

  Input : 7

  Output :

 *
 ***
 *****
 *******
 *****
 ***
 *

'''
