from flask import Flask, render_template, request
from inltk.inltk import get_sentence_encoding
from preprocess import preprocess_text
from similarity import get_similarity

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    similarity_scores = None
    if request.method == 'POST':
        text1 = request.form['text1']
        text2 = request.form['text2']
        print(text1)
        print(text2)


        txt1 ,txt2 = preprocess_text(text1, text2)
        txt1 =  get_sentence_encoding(text1,'gu')
        txt2  = get_sentence_encoding(text2,'gu')   
        similarity_scores = get_similarity(txt1 ,txt2)

    return render_template('index.html', similarity_scores=similarity_scores)

if __name__ == '__main__':
    app.run(debug=True)
