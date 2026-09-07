# li =[12,34,56,78,90,33,57,87,85,31]
# print(li)
# # evens =[]
# # for i in li:
# #     if i%2==0:
# #         evens.append(i)

# evens =[x for x in li if x%2==0]
# print(evens)

# odds = [x for x in li if x%2!=0]
# print(odds)

names = ["kiran","raj","mani","nitya","arun","jenita"]

jnnames =[x for x in names if x.__contains__('j') or x.__contains__('m')]
print(jnnames)