from flask import Flask,render_template

app = Flask(__name__ )

@app.route("/123")
def index():
   # return"nml<h1>g</h1><span style='color:red;'>b</span>"
    return render_template("fankui.html")



@app.route("/sex/news")
def xxx():
    return render_template("xxx.html")



if __name__ == '__main__':
    app.run(host='0.0.0.0')




