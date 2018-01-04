# maximum substring

def max_substring(s1, s2, m, n):

    if m == 0 or n == 0:
        return 0
    elif s1[m-1] == s2[n-1]:
        return 1 + max_substring(s1, s2, m - 1, n - 1)
    else:
        return max(max_substring(s1, s2, m, n - 1),
                   max_substring(s1, s2, m - 1, n))


s1 = "robertchin"
s2 = "herinderchin"


print max_substring(s1, s2, len(s1), len(s2))
