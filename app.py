from flask import Flask, request, render_template
from levenshtein_distance import lev_dis, word_error_rate

app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def text_post ():
    text1 = request.form['s1']
    text2 = request.form['s2']
    distance = lev_dis(text1, text2)
    wer = word_error_rate(text1, distance) * 100
    values = {"val1": distance, "val2" :wer}

    return render_template('result.html', values=values)
 
if __name__ == '__main__':
    app.run()