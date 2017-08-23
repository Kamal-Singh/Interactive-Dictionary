import json

def edit_diff(str1,str2,m,n):
    dp = [[0 for x in range(n+1)] for y in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif str1[i-1]==str2[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
    return dp[m][n]

def best_match(str1,keys):
    m=0
    global bmatch
    bmatch=[]
    for str2 in keys:
        diff=edit_diff(str1,str2,len(str1),len(str2))
        if(diff>=m and len(str2)<=len(str1)):
            m=diff
            bmatch.insert(0,str2)
    return bmatch

def search(str1,data):
    str1=str1.lower()
    if str1 in data:
        return data[str1]
    elif len(best_match(str1,list(data.keys())))>0:
        return bmatch
    else:
        return 'The entered word doesn\'t exist, Double check it.'

data=json.load(open('data.json'))
