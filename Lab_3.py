import math
import random as rand
import statistics as stats

list = [1,5,77,22,3,99,35,10]
print(list)
print("Sum is: ", math.fsum(list))
print("Average is: ", stats.mean(list))
print("Median value: ", stats.median(list))
print("Standard deviation: ", stats.stdev(list));

print("Random integer between 1 and 100: ", rand.randint(1,100));
