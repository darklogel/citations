from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    title = "ma page"
    content = "contenu"
    return render_template('base.html', title=title, content=content)



if __name__=="__main__":
    app.run(host='0.0.0.0',port=80,debug=True)