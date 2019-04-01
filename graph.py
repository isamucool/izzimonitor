from flask import Flask, render_template, request, redirect, url_for

import pygal

app = Flask(__name__, template_folder="templates", static_folder="static")
@app.route ('/', methods = ['GET', 'POST'])
def graph():
    graph = pygal.SolidGauge(
    half_pie=True, inner_radius=0.70,
    style=pygal.style.styles['default'](value_font_size=10))

    percent_formatter = lambda x: '{:.10g}%'.format(x)
    graph.value_formatter = percent_formatter
    graph.add('Series 1', [{'value': 33, 'max_value': 100}])
    graph_data = graph.render_data_uri()

    return render_template("graph.html", graph_data=graph_data)


if __name__ == '__main__':
    app.run(debug = True, port=7777)
