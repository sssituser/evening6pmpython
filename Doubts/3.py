s1 ="ab"
s2="cdab"

print(s1+s2)
s3=s1.__add__(s2)
print(f's3 : {s3}')
print(s3.count('a'))
print(s3.index('d'))
print(s3.isalpha())
print(s3.isalnum())
print(s3.isdigit())
dob ="19-dec-2020"
# print(dob.split('-'))

li = dob.split('-')
print(li[0])
print(li[1])
print(li[2])