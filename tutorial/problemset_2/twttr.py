str=input("Input: ")
length=len(str)
ans=""
for i in range(length):
    if str[i]=='a' or str[i]=='e'or str[i]=='i' or str[i]=='o'or str[i]=='u'or str[i]=='A' or str[i]=='E'or str[i]=='I' or str[i]=='O'or str[i]=='U':
        ans=ans
    else:
        ans+=str[i]
print(ans)