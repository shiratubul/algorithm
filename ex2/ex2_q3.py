import os

class LCSMemoizedTracker:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.memo = {} 
        self.order_counter = 0

    def solve(self, i, j):
        # בדיקה אם התוצאה כבר קיימת בזיכרון
        if (i, j) in self.memo:
            return self.memo[(i, j)][1]

        # א. אחת המחרוזות ריקה
        if i == 0 or j == 0:
            result = ""
            method = "Base Case"
        
        # ב. אם האותיות האחרונות זהות 
        elif self.X[i-1] == self.Y[j-1]:
            res_prev = self.solve(i-1, j-1)
            result = res_prev + self.X[i-1]
            method = f"Match ('{self.X[i-1]}')"
        
        # ג. אם האותיות שונות 
        else:
            res_left = self.solve(i, j-1)
            res_top = self.solve(i-1, j)
            
            if len(res_left) > len(res_top):
                result = res_left
                method = "From Left"
            else:
                result = res_top
                method = "From Top"

        self.order_counter += 1
        self.memo[(i, j)] = (self.order_counter, result, method)
        return result

    def generate_html(self, filename="lcs_memo_table.html"):
        html = """
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; direction: rtl; padding: 20px; }
                table { border-collapse: collapse; margin-top: 20px; background-color: white; }
                th, td { border: 1px solid #444; padding: 12px; text-align: center; min-width: 100px; }
                th { background-color: #f8f9fa; }
                .header-cell { background-color: #e9ecef; font-weight: bold; }
                .order { color: #007bff; font-size: 0.85em; font-weight: bold; display: block; margin-bottom: 4px; }
                .lcs { color: #28a745; font-family: monospace; font-size: 1.1em; }
                .method { color: #6c757d; font-size: 0.75em; display: block; margin-top: 4px; }
                .match { background-color: #d4edda; }
            </style>
        </head>
        <body>
            <h2>טבלת מעקב LCS (Memoization)</h2>
            <p>מחרוזת X: <b>""" + self.X + """</b> (שורות)</p>
            <p>מחרוזת Y: <b>""" + self.Y + """</b> (עמודות)</p>
            <table>
                <tr>
                    <th></th><th>""</th>
        """
        # כותרות עמודות (Y)
        for char in self.Y:
            html += f"<th>{char}</th>"
        html += "</tr>"

        # בניית גוף הטבלה
        for i in range(len(self.X) + 1):
            char_x = self.X[i-1] if i > 0 else '""'
            html += f"<tr><td class='header-cell'>{char_x}</td>"
            for j in range(len(self.Y) + 1):
                data = self.memo.get((i, j), (None, "", "-"))
                order_num, lcs_val, method_val = data
                
                cell_class = "match" if "Match" in method_val else ""
                order_str = f"<span class='order'>#{order_num}</span>" if order_num else ""
                
                html += f"<td class='{cell_class}'>{order_str}<span class='lcs'>'{lcs_val}'</span><br><span class='method'>{method_val}</span></td>"
            html += "</tr>"

        html += "</table></body></html>"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"הקובץ נוצר בהצלחה! פתח את: {os.path.abspath(filename)}")


X_input = "ABC"
Y_input = "BDC"

tracker = LCSMemoizedTracker(X_input, Y_input)
final_result = tracker.solve(len(X_input), len(Y_input))

print(f"LCS סופי: {final_result}")
tracker.generate_html()