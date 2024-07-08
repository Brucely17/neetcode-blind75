s = "()[]{}"
s="([{])"
# s="(){}}{"
s="{[]}"
s="){"
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<=1:
            return False
        par={
            ')':'(',
            ']':'[',
            '}':'{'
        }

        present=[]
        for i in range(len(s)):
            if s[i]=='(' or s[i]=="[" or s[i]=='{':
                present.append(s[i])
            else:
                if len(present)==0:
                    
                    return False
                    break

                temp=present.pop()
                if par[s[i]]!=temp:
                    
                    return False
                    
        if len(present)!=0:
            return False
        return True

# dict={"(":1,")":1,}
# par={
#             ')':'(',
#             ']':'[',
#             '}':'{'
#         }
# dicts={
#     '(':0,
#     '[':0,
#     '{':0

# }
temp=[]
for i in s:
    temp.append(i)
print(temp)
count=0
present=[]
for i in range(len(s)):
    if s[i]=='(' or s[i]=="[" or s[i]=='{':
        dicts[s[i]]+=1
        # present=s[i]
        present.append(s[i])
        print(present,i)
    elif s[i]==')' or s[i]=="]" or s[i]=='}':
        print(present,s[i],par[s[i]])
        temp=present.pop()
        if temp!=par[s[i]]:

            # return False
            print(False)
        dicts[par[s[i]]]-=1
        
        # present=False


for i in dicts.values():
    if i!=0:
        print("False1")
        # return False
print('True')
# return True
    