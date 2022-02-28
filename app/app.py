from flask import render_template, request, redirect
from db import db_tools
from db import create_app
from db.models import Cats

app = create_app()


@app.route('/', methods=["GET", "POST"])
def hello_world():  # put application's code here
    if request.method == "POST":
        name = request.form.get("name")
        price = request.form.get("price")
        breed = request.form.get("breed")

        db_tools.add_instance(Cats, name=name, price=price, breed=breed)
        redirect("/")

    return render_template("form.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)