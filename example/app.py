from pyytdata.pyytdata import PyYtData


from flask import Flask, request, render_template
from forms import SearchForm

app = Flask(__name__)


@app.route("/recm", methods=["GET", "POST"])
def recm_skill():
    form = SearchForm()
    key_word = ""
    val = request.form.get("val")
    print(val)
    if request.method == "POST" and val == "val1":
        key_word = request.form.get("key_word")
        data = PyYtData(key_word, 5)
        titles = data.get_titles()
        descriptions = data.get_descriptions()
        get_urls = data.get_image_urls()
        get_links = data.get_links()
        data1 = zip(titles, descriptions, get_urls, get_links)
        return render_template("recm_skill.html", data1=data1, form=form, j=0)

    return render_template("recm_skill.html", form=form)


if __name__ == "__main__":
    app.secret_key = "123456daily"
    app.run(debug=True)
