def reverseOnlyLetters(s):
    idx = []
    letters = ''
    for i in range(len(s)):
        if s[i] in 'qwertyuiopasdfghjklmnbvcxz':
            letters +=s[i]
        else:
            idx.append(i)
    letters = letters[::-1]
    ans = ''
    j,k=0,0
    for i in range(len(s)):
        if i==idx[k]:
            ans +=s[i]
            k +=1
        else:
            ans +=letters[j]
            j +=1
    return ans