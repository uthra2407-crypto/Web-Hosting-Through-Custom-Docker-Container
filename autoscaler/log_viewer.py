from flask import Flask, render_template_string

app = Flask(__name__)
log_path = "scaling_log.txt"  # ✅ FIXED PATH

@app.route("/")
def index():
    try:
        with open(log_path,encoding="utf-8", errors="replace") as f:
            logs = f.readlines()
    except FileNotFoundError:
        logs = ["[ERROR] scaling_log.txt not found."]
    
    logs.reverse()
    return render_template_string("""
        <h2>📈 Auto-Scaling Log Viewer</h2>
        <pre style="background:#111;color:#0f0;padding:10px;border-radius:10px;">
        {% for line in logs %}
        {{ line.strip() }}
        {% endfor %}
        </pre>
    """, logs=logs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
