import re

snake_case = "snake_case_str"

camel_case = re.sub(r'_([a-z])' , lambda m : m.group(1).upper(), snake_case)

print(camel_case)
