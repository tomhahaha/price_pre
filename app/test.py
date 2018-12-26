import re,os

def lcs(a, b):
    lena = len(a)
    lenb = len(b)
    c = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]
    flag = [[0 for i in range(lenb + 1)] for j in range(lena + 1)]
    for i in range(lena):
        for j in range(lenb):
            if a[i] == b[j]:
                c[i + 1][j + 1] = c[i][j] + 1
                flag[i + 1][j + 1] = 'ok'
            elif c[i + 1][j] > c[i][j + 1]:
                c[i + 1][j + 1] = c[i + 1][j]
                flag[i + 1][j + 1] = 'left'
            else:
                c[i + 1][j + 1] = c[i][j + 1]
                flag[i + 1][j + 1] = 'up'
    return c, flag

def printLcs(flag, a, i, j):
    if i == 0 or j == 0:
        return ''
    if flag[i][j] == 'ok':
        # printLcs(flag, a, i - 1, j - 1)
        return printLcs(flag, a, i - 1, j - 1)+a[i - 1]
    elif flag[i][j] == 'left':
        return ''+ printLcs(flag, a, i, j - 1)
    else:
        return ''+printLcs(flag, a, i - 1, j)

def matchit(a,b):

    p='( INC$| IN$| CORP$)'
    b=re.sub(p,'',b)
    for w in a.split(' '):
        if len(w)>3:
            for x in b.split(' '):
                if len(x)>3:
                    c, flag = lcs(w,x)
                    # 如果最长公共子序列长度大于两个词长的最小值的一半，匹配
                    if len(printLcs(flag,w, len(w), len(x)))>min(len(w),len(x))/2:
                        return True
    return False

# print(matchit('BAMANN E','ALI BAVMANN'))
print(os.listdir('/Users/fxm/Downloads/训练集/xuelang_round1_train_part1_20180628/吊纬'))