# class Difference:
#     def __init__(self, a):
#         self.__elements = a
#         self.maximumDifference = 0
#
#     # Add your code here
#     # maximumdifference = 0
#     def computeDifference(self):
#         # maxdiff = 0
#         alllis = []
#         lis = self.__elements
#         print(lis)
#         for i in lis:
#             k = 1
#             for j in lis[k:]:
#                 dif = abs(j-i)
#                 alllis.append(dif)
#                 k += 1
#         self.maximumDifference = max(alllis)
#
#
# # End of Difference class
#
# _ = input()
# a = [int(e) for e in input().split(' ')]
#
# d = Difference(a)
# d.computeDifference()
#
# print(d.maximumDifference)
#
# num = 600851475143
#
# while True:
#     for i in range(2,600851475143):
#         if num%i == 0:
#             div = num//i
# initial_value = 600851475143
# lis = []
# def primeFactor(number):
#     num = number
#     # initialvalue = number
#
#     for i in range(2,num+1):
#         # print(num, i)
#         if num%i == 0:
#             div = num//i
#             if div == 1 and initial_value != i:
#                 # print("This is " + str(i))
#                 lis.append(i)
#                 break
#             else:
#                 primeFactor(div)
#                 # lis.append(div)
#         else:
#             continue
# primeFactor(initial_value)
# # print(max(lis))
# print(lis)
# print(lis[0])

# import math
#
# factors = []
# n = 600851475143
#
# for i in range(2, math.ceil(math.sqrt(n))):
#     while n % i == 0:
#         factors.append(i)
#         n = n / i
#
# print(factors[-1])


# new_s = ""

def swap(st):
    new_s = []
    string = ""
    s1 = list(st)
    for i in s1:
        # print(i)
        if i == i.upper():
            new_s.append(i.lower())
            string += str(i.lower)
        else:
            string += str(i.upper)
            new_s.append(i.upper())

    for i in new_s:
        print(i, end="")

    # print(new_s)
    return string

s = "hacker Rank"
print(swap(s))

