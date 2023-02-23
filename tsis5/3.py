import re

s = 'dkjneuA_a_dadkeoaa_a_AaD_d_a__aPEKafaaajfjn;oefi'

result = re.findall(r'([a-z]+_[a-z]+)+' , s)

print(result)