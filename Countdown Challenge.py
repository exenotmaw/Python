import time

secondAmount = int(input("Enter the time in seconds: "))

for i in reversed(range(1, secondAmount)):
    secondAmount = i % 60
    minutesAmount = int(i / 60) % 60
    hoursAmount = int(i / 3600)
    print(f"{hoursAmount:02}:{minutesAmount:02}:{secondAmount:02}")
    time.sleep(1)
print("Time to sleep!!!")