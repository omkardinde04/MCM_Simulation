from flask import Flask, render_template, request, jsonify
import sys

app = Flask(__name__)

def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0 for _ in range(n)] for _ in range(n)]
    steps = []

    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                expression = f"{m[i][k]} + {m[k + 1][j]} + {p[i]}*{p[k + 1]}*{p[j + 1]} = {cost}"
                if cost < m[i][j]:
                    m[i][j] = cost
                    steps.append({
                        "i": i,
                        "j": j,
                        "k": k,
                        "cost": cost,
                        "expression": expression
                    })

    return m, steps

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/compute', methods=['POST'])
def compute():
    data = request.get_json()
    dims = data['dimensions']
    m, steps = matrix_chain_order(dims)
    final_answer = m[0][len(dims) - 2]  # The minimum cost is stored in m[0][n-1]
    return jsonify({"steps": steps, "final_answer": final_answer})

@app.route('/simulation')
def simulation():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
