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
    else:
        res1 = lcs_recursive(X, Y[:-1])
        res2 = lcs_recursive(X[:-1], Y)
        
        # לוקחים את המחרוזת הארוכה  
        if len(res1) > len(res2):
            return res1
        else:
            return res2


X=['A', 'B', 'C', 'B', 'D', 'A', 'B']
Y=['B', 'D', 'C', 'A', 'B', 'A']

lcs_calls = 0
final_string = lcs_recursive(X, Y)

print(f"LCS : {final_string}")
print(f"COUNTER : {lcs_calls}")
print("=============================")


X=['A', 'B', 'C']
Y=['D', 'E', 'F', 'G']

lcs_calls = 0
final_string = lcs_recursive(X, Y)

print(f"LCS : {final_string}")
print(f"COUNTER : {lcs_calls}")
