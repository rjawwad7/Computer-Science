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
