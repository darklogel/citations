from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    title = "Mon site web"
    
    # Définissez le nom du fichier CSS à inclure
    css_filename = "style.css"  # Entrez le nom du fichier CSS ici
    return render_template('article.html', title=title, css_filename=css_filename)




if __name__=="__main__":
    app.run(host='0.0.0.0',port=80,debug=True)