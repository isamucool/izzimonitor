from flask import Flask, render_template, request, redirect, url_for
from nltk.tokenize import WhitespaceTokenizer
import linecache
import pygal

app = Flask(__name__, template_folder="templates", static_folder="static")
@app.route ('/monitor', methods = ['GET', 'POST'])


def monitor():
    
    #lectura del archivo por lineas
    #lectura de status de servidores
    serverData1 = WhitespaceTokenizer().tokenize(linecache.getline('LogConsultasSrvr.txt',27))
    serverData2 = WhitespaceTokenizer().tokenize(linecache.getline('LogConsultasSrvr.txt',28))
    serverData3 = WhitespaceTokenizer().tokenize(linecache.getline('LogConsultasSrvr.txt',29))

    #lectura de status de Componentes
    componentData1 = WhitespaceTokenizer().tokenize(linecache.getline('LogConsultasSrvr.txt',47))
    componentData2 = WhitespaceTokenizer().tokenize(linecache.getline('LogConsultasSrvr.txt',48))
    componentData3 = WhitespaceTokenizer().tokenize(linecache.getline('LogConsultasSrvr.txt',49))
    
    
    #lectura de status de Tareas Activas
    taskData1 = WhitespaceTokenizer().tokenize(linecache.getline('LogConsultasSrvr.txt',101))
    taskData2 = WhitespaceTokenizer().tokenize(linecache.getline('LogConsultasSrvr.txt',109))
    taskData3 = WhitespaceTokenizer().tokenize(linecache.getline('LogConsultasSrvr.txt',117))
    taskData4 = WhitespaceTokenizer().tokenize(linecache.getline('LogConsultasSrvr.txt',125))
   

    #creacion de grafico para medidor para componente 1
    
    graph = pygal.SolidGauge(
    half_pie=True, inner_radius=0.50,
    style=pygal.style.styles['default'](value_font_size=10))

    #percent_formatter = lambda x: '{:.10g}%'.format(x)
    user_formatter = lambda x: '{:1g}'.format(x)
    #graph.show_legend = False
    graph.human_readable=True
    graph.value_formatter = user_formatter
    graph.add(componentData1[0], [{'value': int(componentData1[8]), 'max_value': int(componentData1[9])}])
    graph.add(componentData2[0], [{'value': int(componentData2[8]), 'max_value': int(componentData2[9])}])
    graph.add(componentData3[0], [{'value': int(componentData3[8]), 'max_value': int(componentData3[9])}])
    graph_data = graph.render_data_uri()

    #creacion de grafico para medidor para componente 2
    # graph2 = pygal.SolidGauge(
    # half_pie=True, inner_radius=0.70,
    # style=pygal.style.styles['default'](value_font_size=10))
    # graph2.add('Series 2', [{'value': int(componentData2[8]), 'max_value': int(componentData2[9])}])
    # graph2_data = graph2.render_data_uri()

    #creacion de grafico para medidor para componente 3
    # graph3 = pygal.SolidGauge(
    # half_pie=True, inner_radius=0.70,
    # style=pygal.style.styles['default'](value_font_size=10))
    # graph3.add('Series 3', [{'value': int(componentData3[8]), 'max_value': int(componentData3[9])}])
    # graph3_data = graph3.render_data_uri()


    return render_template("monitor.html", 
                            serverData1=serverData1, 
                            serverData2=serverData2, 
                            serverData3=serverData3,
                            componentData1=componentData1,
                            componentData2=componentData2,
                            componentData3=componentData3,
                            graph_data=graph_data,
                            # graph2_data=graph2_data,
                            # graph3_data=graph3_data,
                            taskData1=taskData1,
                            taskData2=taskData2,
                            taskData3=taskData3,
                            taskData4=taskData4)



if __name__ == '__main__':
    app.run(debug = True, port=7777)
