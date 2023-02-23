import re

def camel_to_snake(camel_str):
    camel_case = re.sub(r'(?<!^)(?=[A-Z])' , '_' , camel_str).lower()
    return camel_case


camel_case = "camelCaseStr"
snake_case = camel_to_snake(camel_case)
print(snake_case)