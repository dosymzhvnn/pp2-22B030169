import math
import time
number = int(input())
time = int(input())


time.sleep(time/1000)
sr = math.sqrt(number)


print(f"Square root of {number} after {time} miliseconds is {sr}")