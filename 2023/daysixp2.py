import math

file = open("day_six_input.txt")

"""
Thoughts:
Boat will go x(T - x) millimeters where x = num seconds held down and T = total time allotted
We want x(T - x) > R where R = record

Tx - x^2 > R
Tx > x^2 + R
x > (x^2 + R) / T

range from (T +- sqrt(T^2 - 4R) / 2) 

"""

product = 1
times = []
distances = []

for line in file:
    nums = ["".join([x for x in line.split(":")[1].split(" ") if len(x) > 0])]
    print(nums)
    if "Time" in line:
        times = nums[:]
    elif "Distance" in line:
        distances = nums[:]

print(len(times))
print(times)
for x in range(len(times)):
    # print(times[x])
    time = float(times[x])
    # print(time)
    record = float(distances[x])
    # print(time)
    # print(record)

    root = math.sqrt(time ** 2 - 4 * record)
    minTime = math.ceil((time - root) / 2)
    if (minTime * (time - minTime)) == record:
        minTime += 1
    print("Min: " + str(minTime))
    maxTime = math.floor((time + root) / 2)
    if (maxTime * (time - maxTime)) == record:
        maxTime -= 1
    print("Max: " + str(maxTime))

    product *= maxTime - minTime + 1

print(product)
