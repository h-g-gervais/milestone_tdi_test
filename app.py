from flask import Flask, render_template, request, redirect
from bokeh.embed import components
from bokeh.plotting import figure

app = Flask(__name__)

def create_figure():
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 2, 4, 5]
    
    p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')
    p.line(x, y, legend="Temp.", line_width=2)
    
    return p

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('price_choices.html')
    else :
        #my_app_lulu.prices = request.form.getlist('prices')
        #stock = request.form['ticker']
        #create_plot(stock, my_app_lulu.prices)
        
        plot = create_figure()
        script, div = components(plot)
        return render_template('plot_stocks.html', script = script, div = div)


if __name__ == '__main__':
  app.run(port=33507)
