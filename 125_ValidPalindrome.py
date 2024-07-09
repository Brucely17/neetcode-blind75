s = "A man, a plan, a canal: Panama"


l,r=0,len(s)-1
while l<r:
    while not s[l].isalnum() and l<r:
        l+=1
    while not s[r].isalnum() and l<r:
        r-=1
    
    if s[l].lower() != s[r].lower():
        print(False)
    l+=1
    r-=1
print(True)
# def filtering(i):
#     if str.isalpha(i):
#         return True
#     elif str.isdigit(i):
#         return True
#     else:
#         return False

# filtered=list(filter(filtering,s))

# def convert (i):
#     if str.isupper(i):
#         return str.lower(i)
#     else:
#         return i
# # print(list(filtered))
# # filtered=list(filtered)
# final=list(map(convert,filtered))
# print(final)