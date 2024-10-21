U2L1: A = [2, 8, 6, 3, 9, 1, 7]
B = [0] * len(A)

shift = 2

for i in range(len(A)):
    B[i] = A[(i + shift) % len(A)]

print(B)



U2L2: 
inches = 10 ** 12  # one trillion
(foot, inches) = divmod(inches, 12)
(yards, foot_) = divmod(foot, 3)
(miles, yards_) = divmod(yards, 1760)
(MoonDistance, miles_) = divmod(miles, 238855) 

print("One trillion inches is the same as")
print(MoonDistance, "Distances between earth and the moon;", miles_, "miles;", yards_,
      "yards;", foot_, "feet; and", inches, "inches")


U2L3:

A) a and b are going to occupy the same ID until a is slightly altered
B)A = ["zebra", "kangaroo", "cat", "human", "aardvark"]

def exchange_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]

exchange_sort(A)

print(", ".join(A))




U2L5: 
A) output will be {2, 3, 5, 37, 7, 11, 13, 17, 19, 23, 29, 31}
B) s1 = {2, 3, 5, 7}
s2 = {11, 13, 17, 19, 23}
s3 = {29, 31, 37}

S = s1.isdisjoint(s2) and s2.isdisjoint(s3) and s3.isdisjoint(s1)
print(S)

This code returned true so that means there is no overlap

C) The ouput will beEscape
Camry
Pacifica
Challenger

D) little =   {"hairy":"rat", "clever":"bat", "slow":"cod", "bare":"ant", "quick":"cat"}
midsized = {"hairy":"ewe", "clever":"fox", "slow":"pig", "bare":"eel", "quick":"doe"}
large =    {"hairy":"gnu", "clever":"ape", "slow":"cow", "bare":"elephant", "quick":"nag"}

animals = {"little": little, "midsized": midsized, "large": large} 
for key in animals:
    hash1 = animals[key]
    for key2 in hash1:
        print(hash1[key2])

U2L6: def linsearch(arr):
    values = []
    for n in range(len(arr)):
        if (arr[n] == 20):
            values.append(n)
        if (arr[n] == 25):
            values.append(n)
        if (arr[n] == 60):
            values.append(n)
        if (arr[n] == 74):
            values.append(n)
        if (arr[n] == 97):
            values.append(n)
    return(values)
           
# your main code here
myArr = [20, 20, 24, 27, 39, 40, 43, 46, 50,
         60, 60, 62, 71, 74, 76, 86, 86, 87, 97, 97]


print("The index values of the given array that contain the values 20, 25, 60, 74, and 97 are: ", linsearch(myArr))

U2L7: a = [7, 1, 3, 5, 2, 4, 6]
b = []

for n in range(len(a)):
    x = ((n-2) % 7)
    b.append(a[x])
   
print("before:", a)
print("after:", b)

U2L9:

A) a1 = [2, 7, 6]
a2 = [9, 5, 1]
a3 = [4, 3, 8]
Magic3 = [a1, a2, a3]

def horizantals(arr):
    x0 = arr[0][0] + arr[0][1] + arr[0][2]
    x1 = arr[1][0] + arr[1][1] + arr[1][2]
    x2 = arr[2][0] + arr[2][1] + arr[2][2]
    if x0 == x1 == x2:
        return True
    else:
        return False
   
def verticals(arr):    
    y0 = arr[0][0] + arr[1][0] + arr[2][0]
    y1 = arr[0][1] + arr[1][1] + arr[2][1]
    y2 = arr[0][2] + arr[1][2] + arr[2][2]
    if y0 == y1 == y2:
        return True
    else:
        return False
       
def diagonals(arr):    
    z0 = arr[0][0] + arr[1][1] + arr[2][2]
    z1 = arr[0][2] + arr[1][1] + arr[2][0]
    if z0 == z1:
        x = z1
        return True
    else:
        return False

MagicNum = Magic3[0][0] + Magic3[1][0] + Magic3[2][0]
if (horizantals(Magic3) and verticals(Magic3) and diagonals(Magic3)):
    print("The array is a Magic Square")
    print("The magic number is:", MagicNum)
else:
    print("This array is not a Magic Square")

B) a1 = [2, 7, 6]
a2 = [9, 5, 1]
a3 = [4, 3, 8]
Magic3 = [a1, a2, a3]

add = input("How much would you like to add to the array?: ")
add = int(add)

def horizantals(arr):
    x0 = (arr[0][0] + add) + (arr[0][1] + add) + (arr[0][2] + add)
    x1 = (arr[1][0] + add) + (arr[1][1] + add) + (arr[1][2] + add)
    x2 = (arr[2][0] + add) + (arr[2][1] + add) + (arr[2][2] + add)
    if x0 == x1 == x2:
        return True
    else:
        return False
   
def verticals(arr):    
    y0 = (arr[0][0] + add) + (arr[1][0] + add) + (arr[2][0] + add)
    y1 = (arr[0][1] + add) + (arr[1][1] + add) + (arr[2][1] + add)
    y2 = (arr[0][2] + add) + (arr[1][2] + add) + (arr[2][2] + add)
    if y0 == y1 == y2:
        return True
    else:
        return False
       
def diagonals(arr):    
    z0 = (arr[0][0] + add) + (arr[1][1] + add) + (arr[2][2] + add)
    z1 = (arr[0][2] + add) + (arr[1][1] + add) + (arr[2][0] + add)
    if z0 == z1:
        x = z1
        return True
    else:
        return False

MagicNum = (Magic3[0][0] + add) + (Magic3[1][0] + add) + (Magic3[2][0] + add)
if (horizantals(Magic3) and verticals(Magic3) and diagonals(Magic3)):
    print("The array is a Magic Square")
    print("The magic number is:", MagicNum)
else:
    print("This array is not a Magic Square")

C) a1 = [2, 7, 6]
a2 = [9, 5, 1]
a3 = [4, 3, 8]
Magic3 = [a1, a2, a3]

minus = input("How much would you like to minus to the array?: ")
minus = int(minus)

def horizantals(arr):
    x0 = (arr[0][0] - minus) + (arr[0][1] - minus) + (arr[0][2] - minus)
    x1 = (arr[1][0] - minus) + (arr[1][1] - minus) + (arr[1][2] - minus)
    x2 = (arr[2][0] - minus) + (arr[2][1] - minus) + (arr[2][2] - minus)
    if x0 == x1 == x2:
        return True
    else:
        return False
   
def verticals(arr):    
    y0 = (arr[0][0] - minus) + (arr[1][0] - minus) + (arr[2][0] - minus)
    y1 = (arr[0][1] - minus) + (arr[1][1] - minus) + (arr[2][1] - minus)
    y2 = (arr[0][2] - minus) + (arr[1][2] - minus) + (arr[2][2] - minus)
    if y0 == y1 == y2:
        return True
    else:
        return False
       
def diagonals(arr):    
    z0 = (arr[0][0] - minus) + (arr[1][1] - minus) + (arr[2][2] - minus)
    z1 = (arr[0][2] - minus) + (arr[1][1] - minus) + (arr[2][0] - minus)
    if z0 == z1:
        x = z1
        return True
    else:
        return False

MagicNum = (Magic3[0][0] - minus) + (Magic3[1][0] - minus) + (Magic3[2][0] - minus)
if (horizantals(Magic3) and verticals(Magic3) and diagonals(Magic3)):
    print("The array is a Magic Square")
    print("The magic number is:", MagicNum)
else:
    print("This array is not a Magic Square")

D) a1 = [2, 7, 6]
a2 = [9, 5, 1]
a3 = [4, 3, 8]
Magic3 = [a1, a2, a3]

times = input("How much would you like to times to the array?: ")
times = int(times)

def horizantals(arr):
    x0 = (arr[0][0] * times) + (arr[0][1] * times) + (arr[0][2] * times)
    x1 = (arr[1][0] * times) + (arr[1][1] * times) + (arr[1][2] * times)
    x2 = (arr[2][0] * times) + (arr[2][1] * times) + (arr[2][2] * times)
    if x0 == x1 == x2:
        return True
    else:
        return False
   
def verticals(arr):    
    y0 = (arr[0][0] * times) + (arr[1][0] * times) + (arr[2][0] * times)
    y1 = (arr[0][1] * times) + (arr[1][1] * times) + (arr[2][1] * times)
    y2 = (arr[0][2] * times) + (arr[1][2] * times) + (arr[2][2] * times)
    if y0 == y1 == y2:
        return True
    else:
        return False
       
def diagonals(arr):    
    z0 = (arr[0][0] * times) + (arr[1][1] * times) + (arr[2][2] * times)
    z1 = (arr[0][2] * times) + (arr[1][1] * times) + (arr[2][0] * times)
    if z0 == z1:
        x = z1
        return True
    else:
        return False

MagicNum = (Magic3[0][0] * times) + (Magic3[1][0] * times) + (Magic3[2][0] * times)
if (horizantals(Magic3) and verticals(Magic3) and diagonals(Magic3)):
    print("The array is a Magic Square")
    print("The magic number is:", MagicNum)
else:
    print("This array is not a Magic Square")
