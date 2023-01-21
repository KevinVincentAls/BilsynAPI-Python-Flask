from flask import Flask, request, render_template
from motor import nummerplade
import os
app = Flask(__name__)

#buildtag = os.environ['BUILDTAG']


@app.route('/', methods=['GET', 'POST'])
def index():
    answer = None
    if request.method == 'POST':
        input_text = request.form.get('input_text')
        numberplate = nummerplade(input_text)
        
        answer = numberplate
        
    return render_template('index.html', answer=answer, type=type) #, buildtag=buildtag


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)