from flask import Flask, render_template_string, request
import math

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Advanced Calculator</title>
    <style>
        body { font-family: Arial, background: #181c2f; color: #fff; }
        .container { max-width: 400px; margin: 60px auto; background: #23274d; padding: 30px; border-radius: 12px; box-shadow: 0 0 20px #00fff7; }
        input[type=text] { width: 100%; padding: 12px; font-size: 1.2em; border-radius: 6px; border: none; margin-bottom: 10px; }
        input[type=submit] { width: 100%; padding: 12px; font-size: 1.1em; background: #00fff7; color: #181c2f; border: none; border-radius: 6px; cursor: pointer; }
        .result { margin-top: 18px; font-size: 1.3em; color: #fffd82; }
        .error { color: #ff4b5c; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Advanced Calculator</h2>
        <form method="post">
            <input type="text" name="expression" placeholder="Enter expression, e.g. sin(45) + log(10)" value="{{ expr|default('') }}">
            <input type="submit" value="Calculate">
        </form>
        {% if result is not none %}
            <div class="result">Result: {{ result }}</div>
        {% endif %}
        {% if error %}
            <div class="error">{{ error }}</div>
        {% endif %}
        <div style="margin-top:18px; font-size:0.95em;">
            <b>Supported:</b> +, -, *, /, **, sin, cos, tan, log, sqrt, exp, pi, e, parentheses<br>
            <b>Examples:</b> <code>2+2</code>, <code>sin(90)</code>, <code>log(100, 10)</code>, <code>sqrt(16)</code>, <code>2**8</code>
        </div>
    </div>
</body>
</html>
"""

# Safe evaluation context
allowed_names = {
    k: v for k, v in math.__dict__.items() if not k.startswith("__")
}
allowed_names.update({
    "abs": abs,
    "round": round,
    "pow": pow
})

def safe_eval(expr):
    # Replace degrees for trig functions
    expr = expr.replace('^', '**')
    for func in ['sin', 'cos', 'tan']:
        expr = expr.replace(f"{func}(", f"{func}(math.radians(")
    code = compile(expr, "<string>", "eval")
    return eval(code, {"__builtins__": {},"math": math}, allowed_names)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    error = ""
    expr = ""
    if request.method == "POST":
        expr = request.form.get("expression", "")
        try:
            # Remove whitespace for safety
            expr = expr.strip()
            result = safe_eval(expr)
        except Exception as e:
            error = f"Error: {str(e)}"
    return render_template_string(HTML, result=result, error=error, expr=expr)

if __name__ == "__main__":
    app.run(debug=True)