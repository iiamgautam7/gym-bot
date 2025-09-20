from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret123"  # for sessions

# Fake database
USERS = {"test": "1234"}
RESERVATIONS = []

HTML_LOGIN = """
<h2>Login</h2>
<form method="POST">
  Username: <input name="username"><br><br>
  Password: <input name="password" type="password"><br><br>
  <button type="submit">Login</button>
</form>
"""

HTML_DASHBOARD = """
<h2>Welcome {{user}}</h2>
<a href="{{url_for('reservations')}}">Book a Time Slot</a><br><br>
<a href="{{url_for('logout')}}">Logout</a>
"""

HTML_RESERVATIONS = """
<h2>Available Time Slots</h2>
<ul>
{% for t in times %}
  <li>
    {{t}}
    {% if t not in booked %}
      <form method="POST" style="display:inline;">
        <input type="hidden" name="slot" value="{{t}}">
        <button type="submit">Reserve</button>
      </form>
    {% else %}
      (Already Reserved)
    {% endif %}
  </li>
{% endfor %}
</ul>
<a href="{{url_for('dashboard')}}">Back</a>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u, p = request.form["username"], request.form["password"]
        if USERS.get(u) == p:
            session["user"] = u
            return redirect(url_for("dashboard"))
    return render_template_string(HTML_LOGIN)

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template_string(HTML_DASHBOARD, user=session["user"])

@app.route("/reservations", methods=["GET", "POST"])
def reservations():
    if "user" not in session:
        return redirect(url_for("login"))

    times = ["6:00 PM", "7:00 PM", "8:00 PM"]
    if request.method == "POST":
        slot = request.form["slot"]
        if slot not in RESERVATIONS:
            RESERVATIONS.append(slot)
    return render_template_string(HTML_RESERVATIONS, times=times, booked=RESERVATIONS)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
