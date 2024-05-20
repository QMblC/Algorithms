


def solve(s, l, r):
    if dp[l][r]:
        return dp[l][r]
    substr = s[l:r]
    m = r - l
    if m < 5:
        return substr
    substr = zip_str(s, l, r, 1, substr)
    for i in range(2, m):
        if m % i != 0:
            continue
        substr = zip_str(s, l, r, i, substr)
        substr = zip_str(s, l, r, m // i, substr)

    for i in range(l + 1, r):
        sub = solve(s, l, i) + solve(s, i, r)
        if len(sub) < len(substr):
            substr = sub
    dp[l][r] = substr
    return dp[l][r]

def zip_str(s, l, r, times, prev):
    s_len = r - l
    curr = prev
    if is_periodic(s, l, r, times):
        sub = solve(s, l, l + times)
        curr = f"{s_len // times}({sub})"

    return min(prev, curr, key=lambda x: len(x))

def is_periodic(s, l, r, times):
    period = (r - l) // times
    for i in range(times):
        for j in range(1, period):
            if s[l + times * j + i] != s[l + (times - 1) * j + i]:
                return False
    return True


s = input()
n = len(s)
dp = [[None] * (n + 1) for i in range(n + 1)]

print(solve(s, 0, n))