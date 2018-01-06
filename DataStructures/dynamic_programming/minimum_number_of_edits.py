# minimum number of edits to go from s1 to s2

def minimum_number_of_edits(s1, s2, n, m):

    # 
    if min(n, m) == 0:
        return max(n, m)

    if s1[n-1] == s2[m-1]:
        return minimum_number_of_edits(s1, s2, n - 1, m - 1)
    return 1 + min(minimum_number_of_edits(s1, s2, n, m - 1),
                   minimum_number_of_edits(s1, s2, n - 1, m),
                   minimum_number_of_edits(s1, s2, n - 1, m - 1))

s1 = "geek"
s2 = "gessek"

print minimum_number_of_edits(s1, s2, len(s1), len(s2))
