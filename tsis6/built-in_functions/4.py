import math
import time
number = int(input())
times = int(input())


time.sleep(times/1000)
sr = math.sqrt(number)


print(f"Square root of {number} after {times} miliseconds is {sr}")