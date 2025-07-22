from flask import Flask, render_template, redirect, flash, url_for
from forms import RSVPForm

app = Flask(__name__)
app.secret_key = "rsvp_secret"

@app.route("/", methods=["GET", "POST"])
def rsvp():
    form = RSVPForm()
    if form.validate_on_submit():
        if not form.will_attend.data:
            flash("Sorry to miss you", "warning")
        else:
            flash("Thanks for confirming your attendance!", "success")
        return redirect(url_for("rsvp"))
    return render_template("rsvp.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)
