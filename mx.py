print("Hello Git\n")
n1, n2 = 0, 1
count = 0
answer = 0

# check if the number of terms is valid
print("Fibonacci sequence:")
while True:
       # print(n1)
       nth = n1 + n2
       while nth < 4000000:
            if nth%2 == 0:
                answer = answer + nth
                n1 = n2
                n2 = nth
                nth = n1 + n2

            else:
                n1 = n2
                n2 = nth
                nth = n1 + n2
                # count += 1
       break
print(answer)
