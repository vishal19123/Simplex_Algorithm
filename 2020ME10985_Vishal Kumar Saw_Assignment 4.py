"""
<<< Coded by @VKS >>>

# MCL261 Assignment4 --> simplex method using tableau method

# Problem statements---> linear programming problem in standard form 
            
            min cTx 
            s.t. Ax = b 
            x >= 0, b > 0 where (c)nx1, (A)mxn ,and (b)mx1 matrix

implement python code for tableau method and find the optimal value, solution and nature of slution i.e
whether problem has unique solution or problem has multiple solutions.

NOTE:---> FIRST RUN THE CODE & THEN PLEASE ENTER THE INPUT VALUES ON COMMAND PROMPT

According to my code you will have to be enter -
first enter c 
and then enter A
and at last enter b in appropiate formated as stated in problem

FOR EXAMPLE:
please enter in the formate:
c:[-1,-2,0,0,0] <--- ist
A:[[-2,1,1,0,0],[-1,2,0,1,0],[1,0,0,0,1]] <--- 2nd
b:[2,7,3] <--- 3rd

"""

import math
import numpy as np

""" 
Defining a simplex function will take c, A, and b lists that will be entered by user and will convert it
into required format for calculation i.e (c)nx1 , (A)mxn, and (b)mx1 matrix. and constructed tableau formate
"""
def simplex(c,A,b):
    
    m = len(A) # m is number of row in matrix A
    n = len(A[0]) # n is number of column in matrix A
    
    x=[] # x is basis variable
    for i in range(m,n+1):
        x.append(i)
    
    for i in range(m):
        A[i].append(b[i])
    
    c.append(0)
    while pivot(c,m)!=-1:#loop for updating basis variable matrix
        j = pivot(c,m)
        i = rtio(A,j,m,n)
        x[i]=j+1
        row_opr(A,c,i,j,m,n+1,A[i][j])
    
    multiple = 0
    for i in range(n):#loop for checking whether solution is unique or multiple solution
        if c[i]==0:
            if i+1 not in x:
                multiple=1
                break
    ans = []
    for i in range(n):
        ans.append(0)
    for i in range(m):
        ans[x[i]-1]=A[i][-1] 

    if multiple==1:
        print("The optimal objective function value is",-c[n])
        print("The optimal solution is" ,ans)
        print("This LP has multiple optimal solutions")
    else:    
        print("The optimal objective function value is",-c[n])
        print("The optimal solution is" ,ans)
        print("This LP has a unique optimal solution")

"""
Defining a function for finding column of pivot element. 
column of pivot element corresponding to column of minimum value of ci among all ci's(reduced costs)
and return the coulumn of pivot element.
"""
def pivot(c,m):
    
    min = c[0]
    j = 0
    
    for i in range(m): # loop for finding minimum ci among all ci's
        if c[i]<min:
            j = i
            min = c[i]
    
    if min>=0:
        return -1
    else:
         return j

"""
Defining a function for row operation that will convert entring column into the formate 
where pivot element will be 1 and other remaining element will be 0 expect pivot one in entering column.
"""
def row_opr(A,C,i,j,m,n,v):
    
    for h in range(n):
        A[i][h] = A[i][h]/v

    for k in range(m):
        if k==i:
            c = 0
        else:    
            c = A[k][j]

        for y in range(n):
                A[k][y] = A[k][y] - c*A[i][y]  

    c = C[j]  
    for y in range(n):
        C[y] = C[y] - c*A[i][y]

"""Defining rtio function that will perform ratio test and return the row no. of exiting variable from basis variables"""
def rtio(A,j,m,n):
    
    ratio = 999999999 # initially large value of ratio taken because we need small non-nagative value of ratio for finding pivot element
    ans = -1
    
    for i in range(m):
        if A[i][j]>0:
            if A[i][n-1]/A[i][j] < ratio:
                ratio = A[i][n-1]/A[i][j]
                ans = i
    
    return ans

"""
input entered by user as a whole list like [[c1,c2,.....,cn],[[a11,a12...a1n],[a21,a22,...a2n],......,[am1,am2,....amn]],[b1,b2,...bm]]
splitted the list and extracted c = [c1,c2,.....,cn], A=[[a11,a12...a1n],[a21,a22,...a2n],.....,[am1,am2,....amn]] and b = [b1,b2,...bm]
Here input taken as string and converting it into floating point value 
"""
c_str = str(input("c:"))
A_str = str(input("A:"))
b_str = str(input("b:"))

C=[int(f) for f in c_str[1:len(c_str)-1].split(",")]
i=1
A_str = A_str[2:len(A_str)-2]
af = A_str.split("],[")

A=[]
for x in af:
    A.append([int(f) for f in x.split(",")])
    
b = [int(f) for f in b_str[1:len(b_str)-1].split(",")]    

"""Passes C, A, b to the simplex function"""
simplex(C,A,b)

"""
#input format
#simplex( [-1,0,0,0,0],[[-2,1,1,0,0],[-1,1,0,1,0],[1,0,0,0,1]],[2,3,3] )
#simplex( [-1,-2,0,0,0],[[-2,1,1,0,0],[-1,2,0,1,0],[1,0,0,0,1]] , [2,7,3] 
"""