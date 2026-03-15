lcs_calls = 0
nodes = []
edges = []

def lcs_to_dot(X, Y, parent_id=None):
    global lcs_calls
    lcs_calls += 1
    current_id = lcs_calls
    
    if not X or not Y:
        result = ""
    elif X[-1] == Y[-1]:
        result = lcs_to_dot(X[:-1], Y[:-1], current_id) + X[-1]
    else:
        res1 = lcs_to_dot(X, Y[:-1], current_id)
        res2 = lcs_to_dot(X[:-1], Y, current_id)
        result = res1 if len(res1) > len(res2) else res2
    
    label = f"#{current_id}\\nX: {X if X else '∅'}\\nY: {Y if Y else '∅'}\\nLCS: '{result}'"
    nodes.append(f'  {current_id} [label="{label}"];')
    
    if parent_id is not None:
        edges.append(f"  {parent_id} -> {current_id};")
        
    return result

def generate_graphviz_file(X, Y):
    global lcs_calls, nodes, edges
    lcs_calls = 0
    nodes = []
    edges = []
    
    lcs_to_dot(X, Y)
    
    dot_content = "digraph LCS_Tree {\n"
    dot_content += "  node [shape=box, fontname=\"Arial\", style=filled, fillcolor=\"#f9f9f9\"];\n"
    dot_content += "\n".join(nodes) + "\n"
    dot_content += "\n".join(edges) + "\n"
    dot_content += "}"
    return dot_content

X_test = "ABC"
Y_test = "BD"

dot_output = generate_graphviz_file(X_test, Y_test)
print(dot_output)