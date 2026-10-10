guess = input("Total points: 1 + 2 + 3 + 4 =")

input("Formula: one calculation. Press Enter to run")
n = int(input("Enter the number of terms: "))
total = n * (n + 1) // 2
print(" total=", total, " step = 1")

input("Loop: add one student at a time. Press Enter to run")
total = 0
for student in range(1, n + 1):
    total += student
print(" total=", total, "step =", n)

input("Double loop: counts every single point. Press Enter to run")
total = 0
steps = 0
for student in range(1, n + 1):
    for point in range(1, student +1):
        total += 1
        steps += 1
print( "total=", total, "step =", steps, "your guess was:", guess)