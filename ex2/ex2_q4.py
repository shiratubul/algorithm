def lcs_dynamic_programming(X, Y):
    m = len(X)
    n = len(Y)
    
    L = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                # אם האותיות זהות
                L[i][j] = L[i-1][j-1] + 1
            else:
                # אם שונות
                L[i][j] = max(L[i-1][j], L[i][j-1])
    
    lcs_str = ""
    i, j = m, n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs_str = X[i-1] + lcs_str
            i -= 1
            j -= 1
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
            
    return lcs_str, L[m][n]

# הרצה לדוגמה
X_input = "ABCBDAB"
Y_input = "BDCABA"

result_str, length = lcs_dynamic_programming(X_input, Y_input)

print(f"X: {X_input}")
print(f"Y: {Y_input}")
print(f"LCS: '{result_str}'")
