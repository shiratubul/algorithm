lcs_calls = 0

def lcs_recursive(X, Y):
    global lcs_calls
    lcs_calls += 1
    
    if not X or not Y:
        return ""
    
    # אם האותיות האחרונות זהות
    if X[-1] == Y[-1]:
        return lcs_recursive(X[:-1], Y[:-1]) + X[-1]
    
    # אם הן שונות, בודקים את שני הפיצולים
    res1 = lcs_recursive(X, Y[:-1])
    res2 = lcs_recursive(X[:-1], Y)
    
    # לוקחים את המחרוזת הארוכה  
    return res1 if len(res1) > len(res2) else res2


X_str = "ABCBDAB"
Y_str = "BDCABA"

lcs_calls = 0
result = lcs_recursive(X_str, Y_str)

print(f"String X: {X_str}")
print(f"String Y: {Y_str}")
print(f"LCS Result: '{result}'")
print(f"Total Calls: {lcs_calls}")