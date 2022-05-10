from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from PIL import Image
from werkzeug.utils import secure_filename
from collections import defaultdict
from colorthief import ColorThief


app = Flask(__name__)
Bootstrap(app)
my_list = []


def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        filepath = secure_filename(request.files["file"].filename)
        request.files["file"].save(filepath)
        print(filepath)
        img = Image.open(filepath)
        color_thief = ColorThief(filepath)
        # build a color palette
        palette = color_thief.get_palette(color_count=10)
        for color in palette:
            clr = rgb_to_hex(color)
            my_list.append(clr)

        return redirect(url_for("home"))

    return render_template("index.html", colors=my_list)


if __name__ == '__main__':
    app.run(debug=True)
