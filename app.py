from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('price_choices.html')
    else :
        #my_app_lulu.prices = request.form.getlist('prices')
        #stock = request.form['ticker']
        #create_plot(stock, my_app_lulu.prices)
        return render_template('plot_stocks.html')


if __name__ == '__main__':
  app.run(port=33507)
