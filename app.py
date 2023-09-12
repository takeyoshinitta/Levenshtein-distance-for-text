from flask import Flask, request, render_template
import levenshtein_distance as ld

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def text_post():
    ref = request.form['s1']
    hyp = request.form['s2']
    distance, sub_count, del_count, ins_count = ld.lev_dis(ref, hyp)
    wer = ld.word_error_rate(ref, distance) * 100

    values = {
        "ref": ref,
        "hyp": hyp,
        "sub": sub_count,
        "del": del_count,
        "ins": ins_count,
        "total": distance,
        "wer": round(wer, 2)
    }

    return render_template('result.html', values=values)

if __name__ == '__main__':
    app.run()