from flask import Flask, make_response
from flask import request

app = Flask(__name__)


@app.route('/')
def index(): #view function
    return'<h3> Hello World!</h3>'

@app.route('/tom')
def tom():
    return "<h2>Hi Tommy!</h2>"

@app.route('/user/<name>')
def user(name):
    return '<h1>Helloz, %s</h1>' % name

@app.route('/user/<int:id>')#not working for some reason
def user_id(id):
    return '<h1>Hello, %d</h1>' % id

#matplotlib ex
@app.route("/simple")
def simple():
    import datetime
    import StringIO
    import random

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    png_output = StringIO.StringIO()
    canvas.print_png(png_output)
    response=make_response(png_output.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response
#end ex

#not working
@app.route('/userA')
def userA():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s </p>'%user_agent

if __name__ == '__main__':
    app.run()
