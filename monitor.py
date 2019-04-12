from flask import Flask, render_template, request, redirect, url_for
from nltk.tokenize import WhitespaceTokenizer
import linecache
import pygal

app = Flask(__name__, template_folder="templates", static_folder="static")
@app.route ('/monitor', methods = ['GET', 'POST'])


def monitor():
    fileToRead = 'LogConsultasSrvr2.txt'
    #lectura del archivo por lineas
    #lectura de status de servidores
    serverData1 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,27))
    serverData2 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,28))
    serverData3 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,29))

    #lectura de status de Componentes
    componentData1 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,39))
    componentData2 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,40))
    componentData3 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,41))
    componentData4 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,49))
    componentData5 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,50))
    componentData6 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,51))
    componentData7 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,59))
    componentData8 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,60))
    componentData9 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,61))
    componentData7 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,69))
    componentData8 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,70))
    componentData9 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,71))
    
    
    #lectura de status de Tareas Activas
    taskData1 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,81))
    taskData2 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,82))
    taskData3 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,83))
    taskData4 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,84))
    taskData5 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,85))
    taskData6 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,86))
    taskData7 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,87))
    taskData8 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,88))
    taskData9 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,89))
    taskData10 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,90))
    taskData11 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,91))
    taskData12 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,92))
    taskData13 = WhitespaceTokenizer().tokenize(linecache.getline(fileToRead,93))
    

    #creacion de grafico para medidor para componente 1
    
    graph = pygal.SolidGauge(
    half_pie=True, inner_radius=0.50,
    style=pygal.style.styles['default'](value_font_size=10))

    #percent_formatter = lambda x: '{:.10g}%'.format(x)
    user_formatter = lambda x: '{:1g}'.format(x)
    #graph.show_legend = False
    graph.human_readable=True
    graph.value_formatter = user_formatter
    graph.add(componentData1[0] + '_' + componentData1[1], [{'value': int(componentData1[3]), 'max_value': int(componentData1[4])}])
    graph.add(componentData2[0] + '_' + componentData2[1], [{'value': int(componentData2[3]), 'max_value': int(componentData2[4])}])
    graph.add(componentData3[0] + '_' + componentData3[1], [{'value': int(componentData3[3]), 'max_value': int(componentData3[4])}])
    graph.add(componentData4[0] + '_' + componentData4[1], [{'value': int(componentData3[3]), 'max_value': int(componentData3[4])}])
    graph.add(componentData5[0] + '_' + componentData5[1], [{'value': int(componentData3[3]), 'max_value': int(componentData3[4])}])
    graph.add(componentData6[0] + '_' + componentData6[1], [{'value': int(componentData3[3]), 'max_value': int(componentData3[4])}])
    graph.add(componentData7[0] + '_' + componentData7[1], [{'value': int(componentData3[3]), 'max_value': int(componentData3[4])}])
    graph.add(componentData8[0] + '_' + componentData8[1], [{'value': int(componentData3[3]), 'max_value': int(componentData3[4])}])
    graph.add(componentData9[0] + '_' + componentData9[1], [{'value': int(componentData3[3]), 'max_value': int(componentData3[4])}])
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
                            componentData4=componentData4,
                            componentData5=componentData5,
                            componentData6=componentData6,
                            componentData7=componentData7,
                            componentData8=componentData8,
                            componentData9=componentData9,
                            graph_data=graph_data,
                            taskData1=taskData1,
                            taskData2=taskData2,
                            taskData3=taskData3,
                            taskData4=taskData4,
                            taskData5=taskData5,
                            taskData6=taskData6,
                            taskData7=taskData7,
                            taskData8=taskData8,
                            taskData9=taskData9,
                            taskData10=taskData10,
                            taskData11=taskData11,
                            taskData12=taskData12,
                            taskData13=taskData13)

if __name__ == '__main__':
    app.run(debug = True, port=7777)
