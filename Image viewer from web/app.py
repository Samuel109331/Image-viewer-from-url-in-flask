from flask import Flask,render_template,request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.errorhandler(404)
def notfound(error):
    return render_template("404.html"),404

@app.route("/")
def first():
    return render_template("home.html")

@app.route("/view",methods=["POST"])
def images():
    try:
        url = request.form.get("website")
        soup = BeautifulSoup(requests.get(url).content,'html.parser')
        imgs = soup.find_all("img")
        img_links = []
        for i in imgs:
            try:
                img_links.append(i['src'])
            except:
                img_links.append(i['data-src'])
        return render_template("viewer.html",img_links=img_links)
    except Exception as e:
        error = e
        return render_template("error_page.html",error=e)

if __name__ == "__main__":
    app.run(debug=True)