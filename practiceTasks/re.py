import re

email = input('Write your email : ')

username , domain = email.split('@', 1)
username_pattern= r'^\w+([\.-]?\w+)*s'
domain_pattern = r'^\w+([-]?\w+)*\.\w{2,3}'

if re.search(username_pattern,username) and re.search(domain_pattern, domain):
    print("Email is valid.")
else:
    print("Email is valid.")