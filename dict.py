import json

def edit_diff(str1,str2,m,n):
    dp = [[0 for x in range(n+1)] for y in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0:
                dp[i][j]=j
            elif j==0:
                dp[i][j]=i
            elif str1[i-1]==str2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j])
    return dp[m][n]

def best_match(str1,keys):
    min=1001
    for str2 in keys:
        diff=edit_diff(str1,str2,len(str1),len(str2))
        if(diff<min):
            min=diff
            best_match=str2
    return best_match

def search(str1,data):
    str1=str1.lower()
    if str1 in data:
        return data[str1]
    elif best_match(str1,list(data.keys())):
        match=best_match(str1,data.keys())
        print('Do you mean %s ? If yes enter "Y" else "N" ' %match)
        yn=input()
        if yn=='Y' or yn=='y':
            return data[match]
        elif yn=='N' or yn=='n':
            return 'The entered word doesn\'t exist, Double check it.'
        else:
            return 'The entered Query Doesn\'t exist'
    else:
        return 'The entered word doesn\'t exist, Double check it.'

data=json.load(open('data.json'))
str1=input('Enter Word: ')
ans=search(str1,data)
if type(ans)==list:
    for i in ans:
        print(i)
else:
    print(ans)



