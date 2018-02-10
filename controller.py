from model import InputForm
from flask import Flask, render_template, request
from compute import compute

app = Flask(__name__)

@app.route('/home')
def home():
    # form = InputForm(request.form)
    # if request.method == 'POST' and form.validate():
    #     result = compute(form.a.data, form.b.data,form.c.data, form.d.data,form.e.data,form.z.data,form.g.data,form.h.data,form.i.data)
    # else:
    #     result = None
    return render_template('home.html')

@app.route('/usingdata/', methods=['GET', 'POST'])
def usingdata():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = compute(form.a.data, form.b.data,form.c.data, form.d.data,form.e.data,form.z.data,form.g.data,form.h.data,form.i.data)
    else:
        result = None
    return render_template('usingdata.html', form=form, result=result)

@app.route('/usingimages/')
def usingimages():
    # form = InputForm(request.form)
    # if request.method == 'POST' and form.validate():
    #     result = compute(form.a.data, form.b.data,form.c.data, form.d.data,form.e.data,form.z.data,form.g.data,form.h.data,form.i.data)
    # else:
    #     result = None
    return render_template('usingimages.html')

@app.route('/preventivemeasures/')
def preventivemeasures():
    # form = InputForm(request.form)
    # if request.method == 'POST' and form.validate():
    #     result = compute(form.a.data, form.b.data,form.c.data, form.d.data,form.e.data,form.z.data,form.g.data,form.h.data,form.i.data)
    # else:
    #     result = None
    return render_template('preventivemeasures.html')

if __name__ == '__main__':
    app.run(debug = True)
