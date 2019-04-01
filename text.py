from flask import Flask, render_template, request, redirect, url_for
from nltk.tokenize import WhitespaceTokenizer
import linecache
import pygal

app = Flask(__name__, template_folder="templates", static_folder="static")
@app.route ('/', methods = ['GET', 'POST'])
def text():
    server1 = WhitespaceTokenizer().tokenize(linecache.getline('LogConsultasSrvr.txt',27))
    #server1='texto de prueba 1'
    

    return render_template("text.html", server1=server1[0])


if __name__ == '__main__':
    app.run(debug = True, port=7777)
