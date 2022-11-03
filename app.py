from flask import Flask, request, render_template
import levenshtein_distance as ld

app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def text_post ():
    ref = request.form['s1']
    hyp = request.form['s2']
    distance = ld.lev_dis(ref, hyp)
    ref_arr = ref.split()
    hyp_arr = hyp.split()
    ref_len = len(ref_arr)
    hyp_len = len(hyp_arr)
    ld.count_error(ref_len, hyp_len)
    wer = ld.word_error_rate(ref, distance) * 100

    values = {"ref": ref, 
            "hyp": hyp,
            "sub": ld.sub_count, 
            "del": ld.del_count, 
            "ins": ld.ins_count, 
            "total": distance, 
            "wer" :round(wer, 2)
        }

    return render_template('result.html', values=values)
 
if __name__ == '__main__':
    app.run()