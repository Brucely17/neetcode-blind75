candidates=[2,3,6,7]
target=7
# a=set([[2,3],[3,2]])
# print(a)
candidates=[2,3,5]
target=8
dp=[]
for i in range(target+1):
    dp.append([])
print(dp)
# dp[0]=[[]]


for i in range(1,target+1):
   
    for j in candidates:

        if i>j:
            print('\ncoindition1:',i)
            val=i-j
            print(dp[val],val)
            lst=[]
            if dp[val]!=[]:
                for k in range(len(dp[val])):
                    lst=dp[val][k][:]
                    
                    if lst[-1]>j:
                        continue
                    else:
                
                        print(i,j,lst)
                        lst.append(j)
                        dp[i].append(lst)
                print(i,j,lst)
                print('\n')
               
            # if dp[val]!=0:
            

        
        elif i==j:

            print('\ncondition2')
            dp[i].append([j])
            print(i,dp[i],j)
            print('\n')
            
        for e in dp:
            print(e,'\n')

        
       
        print('\n')

        


        # elif i<j:
        #     print(i,dp[i],'condition3')
        #     break
# print(dp)
