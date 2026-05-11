class matrix_multiplication_table:
    def __init__(self,dimensions):
        self.dimensions = dimensions
        self.titles = {}
        for i in range(len(dimensions)-1):
            self.titles[i+1] = F"A{i+1}: {dimensions[i]}x{dimensions[i+1]}"
            

        self.table = {}
        for i in range(1, len(dimensions)):
            self.table[i] = {}
            for j in range(1, len(dimensions)):
                self.table[i][j] = None

    def add_ops_range(self):
        # calculate the range of operands for each cell in the table
        for i in range(1, len(self.dimensions)):
            for j in range(i, len(self.dimensions)):
                if j > i:
                    self.table[i][j] = {"range": (i, j)}

    def cell_to_html(self, cell):
        if cell is None:
            return ""
        if type(cell) is not dict:
            return ""
        # else, cell is a dict
        ret = ""
        i,j = cell["range"]
        if j == i+1:
            ret += F"ops: A{i} x A{j}"
        else:
            ret += F"ops: A{i} .. A{j}"

        if "cost" in cell:
            ret += F"<br>cost: {cell['cost']}"
        if "optimized_parenthesization" in cell:
            ret += F"<br>optimized: {cell['optimized_parenthesization']}"
        return ret

    def calculate_one_multiplication_cost(self):  # calculate the cost of multiplying exactly two matrices
        for i in range(1, len(self.dimensions)-1):
            self.table[i][i+1] = {"range": (i, i+1),
                                  "cost": self.dimensions[i-1]*self.dimensions[i]*self.dimensions[i+1], 
                                  "optimized_parenthesization": F"A{i}xA{i+1}"}

    def get_cost(self, i, j):
        if i == j:
            return 0
        return self.table[i][j]["cost"]

    def get_optimized_parenthesization(self, i, j):
        cell = self.table[i][j]
        if i == j:
            return F"A{i}"
        if j == i+1:
            return F"(A{i}xA{j})"
        if "optimized_parenthesization" in cell:
            return cell["optimized_parenthesization"]
        else:
            return ""

    def calculate_multiplication_cost(self, num_multiplications):
        # num_multiplications must be at least 2, because the cost of multiplying two matrices
        # is already calculated in calculate_one_multiplication_cost
        if num_multiplications < 2:
            raise ValueError("num_multiplications must be at least 2")
        for i in range(1, len(self.dimensions)-num_multiplications):
            j = i + num_multiplications
            min_cost = None
            best_k = None
            for k in range(i, j):
                cost = (self.get_cost(i, k) + self.get_cost(k+1, j) +
                        self.dimensions[i-1]*self.dimensions[k]*self.dimensions[j])
                if min_cost is None or cost < min_cost:
                    min_cost = cost
                    best_k = k
            optimized_parenthesization_left = self.get_optimized_parenthesization(i, best_k)
            optimized_parenthesization_right = self.get_optimized_parenthesization(best_k+1, j)
            optimized_parenthesization = F"({optimized_parenthesization_left}x{optimized_parenthesization_right})"
            self.table[i][j] = {"range": (i, j), "cost": min_cost, "optimized_parenthesization": optimized_parenthesization}


    def print_to_html(self):
        html = "<table border='1' style='border-collapse: collapse'>\n"
        html += "<tr><th></th>"
        for j in range(1, len(self.dimensions)):
            html += F"<th>{self.titles[j]}</th>"
        html += "</tr>\n"
        for i in range(1, len(self.dimensions)):
            html += F"<tr><th>{self.titles[i]}</th>"
            for j in range(1, len(self.dimensions)):
                cell = self.table[i][j]
                html += F"<td>{self.cell_to_html(cell)}</td>"
            html += "</tr>\n"
        html += "</table>"
        return html

def main():
    dimensions=[30, 20, 5, 15, 20, 25]
    t = matrix_multiplication_table(dimensions)
    t.add_ops_range()
    t.calculate_one_multiplication_cost()

    output_file = "matrix_multiplication_table_01.html"
    with open(output_file, "w") as f:
        f.write(t.print_to_html())

    for num_multiplications in range(2, len(dimensions)-1):
        t.calculate_multiplication_cost(num_multiplications)
        output_file = F"matrix_multiplication_table_{num_multiplications:02}.html"
        with open(output_file, "w") as f:
            f.write(t.print_to_html())


if __name__ == "__main__":
    main()