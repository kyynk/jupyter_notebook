'''
S_iterative:
S_ 10 : 520
'''
# the iterative approach
def S_iterative(n):
    ans = 0
    for i in range(2,n+1):
        ans += (2**(i-2) + 1)
    return ans

n=10
print ("S_iterative:")
print ("S_", n , ":", S_iterative(n))
'''S_recursive:
S_ 10 : 520 ; recursive calls:  109'''
'''# the recursive version
def S_recursive(n):
    global total
    total += 1
    if(n == 1):
        return 0
    elif(n == 2):
        return 2
    return 2*S_recursive(n-1) - S_recursive(n-2) + 2**(n-3)'''
# the recursive version
def S_recursive(n):
    global total
    total += 1
    if(n == 1):
        return 0
    return S_recursive(n-1)+2**(n-2)+1

n=10
total=0
print ("S_recursive:")
print ("S_", n , ":", S_recursive(n) , "; recursive calls: " , total ,) 

'''
Running time comparison (Timer Method 1):
Iterative on 10 = 520 ; Recursive on 10 = 520
iterative approach: 0.03165690000000154
Recursive approach: 0.2878708000000003
Running time comparison (Timer Method 2):
Iterative on 10 = 520 ; Recursive on 10 = 520
iterative approach: 0.032541999999999405
Recursive approach: 0.3432421000000012
'''
#---------------------------------------------------------timeit
import timeit as ti
n=10
#---------------------------------------------------------Method 1
print("Running time comparison (Timer Method 1):")

tstart = ti.default_timer() #timer start 計時器開啟
for i in range(10000):
    S_iterative(n)
tend = ti.default_timer() #timer end計時器關閉
t_ite=tend - tstart#開始與結束的差值

tstart = ti.default_timer() #timer start 計時器開啟
for i in range(10000):
    S_recursive(n)
tend = ti.default_timer() #timer end計時器關閉
t_rec=tend - tstart#開始與結束的差值

print("Iterative on", n, "=", S_iterative(n), "; Recursive on", n, "=", S_recursive(n))
print("iterative approach:", t_ite)
print("Recursive approach:", t_rec)

#---------------------------------------------------------Method 2
print("Running time comparison (Timer Method 2):")

def iterative_test():
    S_iterative(n)
    
def recursive_test():
    S_recursive(n)
    
t_ite = ti.timeit("iterative_test()", setup="from __main__ import iterative_test", number = 10000)#timeit(函數名稱,執行次數)
t_rec = ti.timeit("recursive_test()", setup="from __main__ import recursive_test", number = 10000)

print("Iterative on", n, "=", S_iterative(n), "; Recursive on", n, "=", S_recursive(n))
print("iterative approach:", t_ite)
print("Recursive approach:", t_rec)
'''
The inversion number of  [35, 11, 26, 13, 64, 21, 44, 6, 100, 57, 77, 82] is 19
'''
# the iterative approach
def inversion_number_iterative(P):
    sum = 0
    for i in range(len(P)-1):
        for j in range(i+1,len(P)):
            if P[i]>P[j]:
                sum += 1
    return sum

#perm=[4, 6, 2, 5, 1, 3]
#perm = [12, 11, 13, 5, 6, 7]
perm=[35, 11, 26, 13, 64, 21, 44, 6, 100, 57, 77, 82]
print('The inversion number of ', perm, 'is', inversion_number_iterative(perm))

'''
The inversion number of  [35, 11, 26, 13, 64, 21, 44, 6, 100, 57, 77, 82] is 19
'''
# the linear recursive version
def inversion_number_recursive(P,i=0,j=1):
    if i == len(P)-1:
        return 0
    sum = 0
    #print(P[i],P[j])
    if P[i]>P[j]:
        sum += 1
    if j == len(P)-1:
        return sum + inversion_number_recursive(P,i+1,i+2)
    return sum + inversion_number_recursive(P,i,j+1)

#perm=[4, 6, 2, 5, 1, 3]
#perm = [12, 11, 13, 5, 6, 7]
perm=[35, 11, 26, 13, 64, 21, 44, 6, 100, 57, 77, 82]
print('The inversion number of ', perm, 'is', inversion_number_recursive(perm))

'''
The inversion number of  [35, 11, 26, 13, 64, 21, 44, 6, 100, 57, 77, 82] is 19
'''
def inversion_number_tworecurs(P,L=0,R=0,index=-1,compare=0):
    if(index==-1):
        sum=0
        for i in range(len(P)):
            #print(i,sum)
            sum+=inversion_number_tworecurs(P,0,len(P),i,P[i])
        return sum
    if (len(P)==1):
        if index < L and compare > P[0] :
            #print(1,L,R)
            return 1 
        else:
            #print(0,L,R)
            return 0
    mid=len(P)//2
    LP=P[:mid]
    RP=P[mid:]
    #print(LP,RP)
    return inversion_number_tworecurs(LP,L,L+mid,index,compare)+inversion_number_tworecurs(RP,L+mid,R,index,compare)

#perm=[4, 6, 2, 5, 1, 3]
#perm = [12, 11, 13, 5, 6, 7]
perm=[35, 11, 26, 13, 64, 21, 44, 6, 100, 57, 77, 82]
print('The inversion number of ', perm, 'is', inversion_number_tworecurs(perm))

'''
Running time comparison (Timer Method 1):
Permutation: [35, 11, 26, 13, 64, 21, 44, 6, 100, 57, 77, 82]
The inversion number of is 19 (iterat)
The inversion number of is 19 (linear)
The inversion number of is 19 (binary)
Iterative approach: 0.0713134000000002
Recursive approach: 0.09004210000000001
Binrecurs approach: 0.174385
Running time comparison (Timer Method 2):
Iterative approach: 0.07094770000000006
Recursive approach: 0.08859680000000014
Binrecurs approach: 0.17697819999999997
'''
#---------------------------------------------------------timeit
#import timeit as ti

#perm = [12, 11, 13, 5, 6, 7]
perm=[35, 11, 26, 13, 64, 21, 44, 6, 100, 57, 77, 82]

#---------------------------------------------------------Method 1
print("Running time comparison (Timer Method 1):")

tstart = ti.default_timer() #timer start 計時器開啟

for i in range(10000):
    inversion_number_iterative(perm)
tend = ti.default_timer() #timer end計時器關閉
t_ite=tend - tstart#開始與結束的差值

tstart = ti.default_timer() #timer start 計時器開啟
for i in range(10000):
    inversion_number_recursive(perm)
tend = ti.default_timer() #timer end計時器關閉
t_rec=tend - tstart#開始與結束的差值

tstart = ti.default_timer() #timer start 計時器開啟
for i in range(10000):
    inversion_number_tworecurs(perm)
tend = ti.default_timer() #timer end計時器關閉
t_twr=tend - tstart#開始與結束的差值

print("Permutation:", perm)
print('The inversion number of is', inversion_number_iterative(perm),'(iterat)')
print('The inversion number of is', inversion_number_recursive(perm),'(linear)')
print('The inversion number of is', inversion_number_tworecurs(perm),'(binary)')

print("Iterative approach:", t_ite)
print("Recursive approach:", t_rec)
print("Binrecurs approach:", t_twr)

#---------------------------------------------------------Method 2
print("Running time comparison (Timer Method 2):")

def iterative_test():
    inversion_number_iterative(perm)

def recursive_test():
    inversion_number_recursive(perm)

def binrecurs_test():
    inversion_number_tworecurs(perm)
    
t_ite = ti.timeit("iterative_test()", setup="from __main__ import iterative_test", number = 10000)#timeit(函數名稱,執行次數)
t_rec = ti.timeit("recursive_test()", setup="from __main__ import recursive_test", number = 10000)
t_twr = ti.timeit("binrecurs_test()", setup="from __main__ import binrecurs_test", number = 10000)

print("Iterative approach:", t_ite)
print("Recursive approach:", t_rec)
print("Binrecurs approach:", t_twr)