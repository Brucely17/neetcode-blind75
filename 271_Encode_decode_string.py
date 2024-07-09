# Premium 
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        res=''
        for i in strs:
            res+=str(len(i))+'|'+i
        print(res)
        return res


    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        lst=[]
        i=0
        while i<=len(str)-1:
            if str[i].isnumeric() :
                ind=i
                # temp=str
                print(ind)
                while str[ind]!='|':
                    ind+=1
                val=int(str[i:ind])
                print("last:",ind,val,str[ind:ind+val+1])
                
                # break
                    

                print(val,str[i+1:i+val+1],str[val+1])
                lst.append(str[ind+1:ind+val+1])
                i=ind+val+1
                print(str[i:])
        print(lst)

        return lst