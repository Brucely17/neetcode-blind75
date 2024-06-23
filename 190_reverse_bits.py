n=4
# 32 bit - 0100
res=0

for i in range(32):
    bit=(n>>i)&1 #last bit
    res=res|(bit <<(31-i))
    print(res)