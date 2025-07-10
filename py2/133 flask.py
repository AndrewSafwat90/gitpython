from flask import Flask, render_template

skills_app = Flask(__name__)

my_skills = [("HTML", 80), ("CSS", 70), ("JavaScript", 60), ("Python", 90)]


@skills_app.route("/")
def homePage():
    return render_template("homepage.html", pagetitle="HomePage", custom_css="home")


@skills_app.route("/contactus")
def contactUs():
    return render_template("contactus.html", pagetitle="contactus")


@skills_app.route("/add")
def add():
    return render_template("add.html", pagetitle="add", custom_css="add")


@skills_app.route("/skills")
def skills():
    return render_template("skills.html", pagetitle="skills",
                           custom_css="skills", page_head="My skills",
                           description="Here are my skills",
                           skills=my_skills, custom_css="skills")


if __name__ == "__main__":
    skills_app.run(debug=True, port=9000)
