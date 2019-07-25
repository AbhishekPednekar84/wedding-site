import os
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KET")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)

from forms.testimonials import TestimonialForm
from models.db_models import Testimonial


@app.route("/", methods=["GET", "POST"])
def wedding_page():
    pw_images = os.listdir(os.path.join(os.getcwd(), "static\\images\\pre-wedding\\"))

    # Submit the testimonial to the database
    form = TestimonialForm()
    if form.validate_on_submit():
        testimonial = Testimonial(name=form.name.data, message=form.message.data)
        db.session.add(testimonial)
        db.session.commit()

        return redirect(url_for("display_testimonials"))
    return render_template("wedding_page.html", pw_images=pw_images, form=form)


@app.route("/testimonials")
def display_testimonials():
    testimonials = Testimonial.query.all()
    return render_template("testimonials.html", testimonials=testimonials)
