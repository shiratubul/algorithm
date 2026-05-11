def matrix_multiplication_cost_2(dimensions):
    if len(dimensions) != 3:
        raise ValueError(" dimensions חייב להכיל בדיוק 3 מספרים")
    
    cost = dimensions[0] * dimensions[1] * dimensions[2]
    return cost


print(f"העלות היא: {matrix_multiplication_cost_2([10, 20, 8])}")