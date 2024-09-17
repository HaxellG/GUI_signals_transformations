from flask import Flask, render_template, request
import plotly
import json
from signals.continuous_signals import (
    create_continuous_plotly_graph, 
    create_double_continuous_plotly_graph, 
    generate_first_continuous_signal, 
    generate_second_continuous_signal, 
    generate_method_1_continuous_signal_transformation, 
    generate_method_2_continuous_signal_transformation
)
from signals.discrete_signals import (
    create_discrete_plotly_graph,
    create_double_discrete_plotly_graph,
    generate_first_discrete_signal, 
    generate_second_discrete_signal,
    generate_method_1_discrete_signal_transformation,
    generate_method_2_discrete_signal_transformation,
)
from signals.add_c_signals import (
    generate_first_c1_signal_transformaded,
    generate_first_c2_signal_transformaded,
    generate_preview_first_sum_c_signal, 
    generate_preview_second_sum_c_signal, 
    generate_result_first_sum_c_signal,
    generate_second_c1_signal_transformaded,
    generate_second_c2_signal_transformaded,
    generate_result_second_sum_c_signal,
)
from signals.add_d_signals import (
    generate_first_d1_signal_transformaded,
    generate_first_d2_signal_transformaded,
    generate_preview_first_sum_d_signal, 
    generate_preview_second_sum_d_signal, 
    generate_result_first_sum_d_signal,
    generate_second_d1_signal_transformaded,
    generate_second_d2_signal_transformaded,
    generate_result_second_sum_d_signal,
)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/introduction')
def introduction():
    return render_template('introduction.html')

@app.route('/continuous-signals')
def continuous_signals():
    # Obtener los valores de las señales
    x_1, y_1 = generate_first_continuous_signal()
    x_2, y_2 = generate_second_continuous_signal()

    # Crear el gráfico
    graph_1 = create_continuous_plotly_graph(x_1, y_1, 'Gráfica Genarada de la Señal Continua 1')
    graph_2 = create_continuous_plotly_graph(x_2, y_2, 'Gráfica Genarada de la Señal Continua 2')

    graphiques = {
        'data_1': graph_1['data'],
        'layout_1': graph_1['layout'],
        'data_2': graph_2['data'],
        'layout_2': graph_2['layout'],
    }

    # Convertir gráfico a JSON para enviarlo al front
    graph_json = json.dumps(graphiques, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('continuous_signals/signals.html', graphJSON=graph_json)

@app.route('/continuous-signals/first-signal')
def first_continuous_signal():
    # Obtener los valores de las señales
    x, y = generate_first_continuous_signal()

    # Crear el gráfico
    graph = create_continuous_plotly_graph(x, y, 'Gráfica Original de la Señal Continua 1')

    # Convertir gráfico a JSON para enviarlo al front
    graph_json = json.dumps(graph, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('continuous_signals/signal_1.html', graphJSON=graph_json)

@app.route('/continuous-signals/first-signal/first-method')
def first_continuous_method():
    # Obtener parametros del request
    scale_factor = request.args.get('scale_factor', type=float)
    time_shift = request.args.get('time_shift', type=float)

    # Generar señal original
    x, y = generate_first_continuous_signal()
    graph_1 = create_continuous_plotly_graph(x, y, 'Gráfica Original de la Señal Continua 1')

    # Generar señal transformada si existen parametros de transformacion
    if scale_factor is not None and time_shift is not None:
        transformation_data = generate_method_1_continuous_signal_transformation(time_shift, scale_factor, '1')
        x_2, y_2 = transformation_data['shifted']['x'], transformation_data['shifted']['y']
        x_3, y_3 = transformation_data['scaled']['x'], transformation_data['scaled']['y']
        graph_2 = create_continuous_plotly_graph(x_2, y_2, 'Gráfica Desplazada de la Señal Continua 1')
        graph_3 = create_continuous_plotly_graph(x_3, y_3, 'Gráfica Escalada de la Señal Continua 1')
    else:
        graph_2 = graph_1
        graph_3 = graph_1

    graphiques = {
        'data_1': graph_1['data'],
        'layout_1': graph_1['layout'],
        'data_2': graph_2['data'],
        'layout_2': graph_2['layout'],
        'data_3': graph_3['data'],
        'layout_3': graph_3['layout'],
    }

    # Convertir gráficos a JSON para enviarlo al front
    graph_json = json.dumps(graphiques, cls=plotly.utils.PlotlyJSONEncoder)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return graph_json
    else:
        return render_template('continuous_signals/signal_1_method_1.html', graphJSON=graph_json)

@app.route('/continuous-signals/first-signal/second-method')
def second_continuous_method():
    # Obtener parametros del request
    scale_factor = request.args.get('scale_factor', type=float)
    time_shift = request.args.get('time_shift', type=float)

    # Generar señal original
    x, y = generate_first_continuous_signal()
    graph_1 = create_continuous_plotly_graph(x, y, 'Gráfica Original de la Señal Continua 1')

    # Generar señal transformada si existen parametros de transformacion
    if scale_factor is not None and time_shift is not None:
        transformation_data = generate_method_2_continuous_signal_transformation(time_shift, scale_factor, '1')
        x_2, y_2 = transformation_data['shifted']['x'], transformation_data['shifted']['y']
        x_3, y_3 = transformation_data['scaled']['x'], transformation_data['scaled']['y']
        graph_2 = create_continuous_plotly_graph(x_2, y_2, 'Gráfica Desplazada de la Señal Continua 1')
        graph_3 = create_continuous_plotly_graph(x_3, y_3, 'Gráfica Escalada de la Señal Continua 1')
    else:
        graph_2 = graph_1
        graph_3 = graph_1

    graphiques = {
        'data_1': graph_1['data'],
        'layout_1': graph_1['layout'],
        'data_2': graph_2['data'],
        'layout_2': graph_2['layout'],
        'data_3': graph_3['data'],
        'layout_3': graph_3['layout'],
    }

    # Convertir gráficos a JSON para enviarlo al front
    graph_json = json.dumps(graphiques, cls=plotly.utils.PlotlyJSONEncoder)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return graph_json
    else:
        return render_template('continuous_signals/signal_1_method_2.html', graphJSON=graph_json)



@app.route('/continuous-signals/second-signal')
def second_continuous_signal():
    # Obtener los valores de las señales
    x, y = generate_second_continuous_signal()

    # Crear el gráfico
    graph = create_continuous_plotly_graph(x, y, 'Gráfica Original de la Señal Continua 2')

    # Convertir gráfico a JSON para enviarlo al front
    graph_json = json.dumps(graph, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('continuous_signals/signal_2.html', graphJSON=graph_json)

@app.route('/continuous-signals/second-signal/first-method')
def second_continuous_signal_first_method():
    # Obtener parametros del request
    scale_factor = request.args.get('scale_factor', type=float)
    time_shift = request.args.get('time_shift', type=float)

    # Generar señal original
    x, y = generate_second_continuous_signal()
    graph_1 = create_continuous_plotly_graph(x, y, 'Gráfica Original de la Señal Continua 2')

    # Generar señal transformada si existen parametros de transformacion
    if scale_factor is not None and time_shift is not None:
        transformation_data = generate_method_1_continuous_signal_transformation(time_shift, scale_factor, '2')
        x_2, y_2 = transformation_data['shifted']['x'], transformation_data['shifted']['y']
        x_3, y_3 = transformation_data['scaled']['x'], transformation_data['scaled']['y']
        graph_2 = create_continuous_plotly_graph(x_2, y_2, 'Gráfica Desplazada de la Señal Continua 2')
        graph_3 = create_continuous_plotly_graph(x_3, y_3, 'Gráfica Escalada de la Señal Continua 2')
    else:
        graph_2 = graph_1
        graph_3 = graph_1

    graphiques = {
        'data_1': graph_1['data'],
        'layout_1': graph_1['layout'],
        'data_2': graph_2['data'],
        'layout_2': graph_2['layout'],
        'data_3': graph_3['data'],
        'layout_3': graph_3['layout'],
    }

    # Convertir gráficos a JSON para enviarlo al front
    graph_json = json.dumps(graphiques, cls=plotly.utils.PlotlyJSONEncoder)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return graph_json
    else:
        return render_template('continuous_signals/signal_2_method_1.html', graphJSON=graph_json)

@app.route('/continuous-signals/second-signal/second-method')
def second_continuous_signal_second_method():
    # Obtener parametros del request
    scale_factor = request.args.get('scale_factor', type=float)
    time_shift = request.args.get('time_shift', type=float)

    # Generar señal original
    x, y = generate_second_continuous_signal()
    graph_1 = create_continuous_plotly_graph(x, y, 'Gráfica Original de la Señal Continua 2')

    # Generar señal transformada si existen parametros de transformacion
    if scale_factor is not None and time_shift is not None:
        transformation_data = generate_method_2_continuous_signal_transformation(time_shift, scale_factor, '2')
        x_2, y_2 = transformation_data['shifted']['x'], transformation_data['shifted']['y']
        x_3, y_3 = transformation_data['scaled']['x'], transformation_data['scaled']['y']
        graph_2 = create_continuous_plotly_graph(x_2, y_2, 'Gráfica Desplazada de la Señal Continua 2')
        graph_3 = create_continuous_plotly_graph(x_3, y_3, 'Gráfica Escalada de la Señal Continua 2')
    else:
        graph_2 = graph_1
        graph_3 = graph_1

    graphiques = {
        'data_1': graph_1['data'],
        'layout_1': graph_1['layout'],
        'data_2': graph_2['data'],
        'layout_2': graph_2['layout'],
        'data_3': graph_3['data'],
        'layout_3': graph_3['layout'],
    }

    # Convertir gráficos a JSON para enviarlo al front
    graph_json = json.dumps(graphiques, cls=plotly.utils.PlotlyJSONEncoder)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return graph_json
    else:
        return render_template('continuous_signals/signal_2_method_2.html', graphJSON=graph_json)







@app.route('/discrete-signals')
def discrete_signals():
    # Obtener los valores de las señales
    x_1, y_1 = generate_first_discrete_signal()
    x_2, y_2 = generate_second_discrete_signal()

    # Crear el gráfico
    graph_1 = create_discrete_plotly_graph(x_1, y_1, 'Gráfica Genarada de la Señal Discreta 1')
    graph_2 = create_discrete_plotly_graph(x_2, y_2, 'Gráfica Genarada de la Señal Discreta 2')

    graphiques = {
        'data_1': graph_1.get('data'),
        'layout_1': graph_1.get('layout'),
        'data_2': graph_2.get('data'),
        'layout_2': graph_2.get('layout'),
    }

    # Convertir gráfico a JSON para enviarlo al front
    graph_json = json.dumps(graphiques, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('discrete_signals/signals.html', graphJSON=graph_json)

@app.route('/discrete-signals/first-signal')
def first_discrete_signal():
    # Obtener los valores de las señales
    x, y = generate_first_discrete_signal()

    # Crear el gráfico
    graph = create_discrete_plotly_graph(x, y, 'Gráfica Seleccionada: Señal Discreta 1')

    # Convertir gráfico a JSON para enviarlo al front
    graph_json = json.dumps(graph, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('discrete_signals/signal_1.html', graphJSON=graph_json)

@app.route('/discrete-signals/second-signal')
def second_discrete_signal():
    # Obtener los valores de las señales
    x, y = generate_second_discrete_signal()

    # Crear el gráfico
    graph = create_discrete_plotly_graph(x, y, 'Gráfica Seleccionada: Señal Discreta 2')

    # Convertir gráfico a JSON para enviarlo al front
    graph_json = json.dumps(graph, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('discrete_signals/signal_2.html', graphJSON=graph_json)

@app.route('/discrete-signals/first-signal/first-method')
def first_discrete_method():
    # Obtener parametros del request
    scale_factor = request.args.get('scale_factor', type=float)
    time_shift = request.args.get('time_shift', type=float)

    # Generar señal original
    x, y = generate_first_discrete_signal()
    graph_1 = create_discrete_plotly_graph(x, y, 'Gráfica Original de la Señal Discreta 1')

    # Generar señal transformada si existen parametros de transformacion
    if scale_factor is not None and time_shift is not None:
        transformation_data, graphs_number = generate_method_1_discrete_signal_transformation(time_shift, scale_factor, '1')
        if (graphs_number == '1'):
            x_2, y_2 = transformation_data['shifted']['x'], transformation_data['shifted']['y']
            x_6, y_6 = transformation_data['scaled']['x'], transformation_data['scaled']['y']
            graph_2 = create_discrete_plotly_graph(x_2, y_2, 'Gráfica Desplazada de la Señal Discreta 1')
            graph_6 = create_discrete_plotly_graph(x_6, y_6, 'Gráfica Escalada de la Señal Discreta 1')
            
            graphiques = {
                'graphs_number': graphs_number,
                'data_1': graph_1['data'],
                'layout_1': graph_1['layout'],
                'data_2': None,
                'layout_2': None,
                'data_3': None,
                'layout_3': None,
                'data_4': None,
                'layout_4': None,
                'data_5': None,
                'layout_5': None,
                'data_6': graph_6['data'],
                'layout_6': graph_6['layout'],
            }
        else:
            x_2, y_2 = transformation_data['shifted']['x'], transformation_data['shifted']['y']
            x_3, y_3 = transformation_data['zeros']['x'], transformation_data['zeros']['y']
            x_4, y_4 = transformation_data['escalon']['x'], transformation_data['escalon']['y']
            x_5, y_5 = transformation_data['linear']['x'], transformation_data['linear']['y']
            
            graph_2 = create_discrete_plotly_graph(x_2, y_2, 'Gráfica Desplazada de la Señal Discreta 1')
            graph_3 = create_discrete_plotly_graph(x_3, y_3, 'Gráfica Interpolada por cero')
            graph_4 = create_discrete_plotly_graph(x_4, y_4, 'Gráfica Interpolada por escalon')
            graph_5 = create_discrete_plotly_graph(x_5, y_5, 'Gráfica Interpolada Lineal')
            
            graphiques = {
                'graphs_number': graphs_number,
                'data_1': graph_1['data'],
                'layout_1': graph_1['layout'],
                'data_2': graph_2['data'],
                'layout_2': graph_2['layout'],
                'data_3': graph_3['data'],
                'layout_3': graph_3['layout'],
                'data_4': graph_4['data'],
                'layout_4': graph_4['layout'],
                'data_5': graph_5['data'],
                'layout_5': graph_5['layout'],
                'data_6': None,
                'layout_6': None,
            }
    else:
        graphiques = {
            'graphs_number': '1',
            'data_1': graph_1['data'],
            'layout_1': graph_1['layout'],
            'data_2': None,
            'layout_2': None,
            'data_3': None,
            'layout_3': None,
            'data_4': None,
            'layout_4': None,
            'data_5': None,
            'layout_5': None,
            'data_6': graph_1['data'],
            'layout_6': graph_1['layout'],
        }

    # Convertir gráficos a JSON para enviarlo al front
    graph_json = json.dumps(graphiques, cls=plotly.utils.PlotlyJSONEncoder)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return graph_json
    else:
        return render_template('discrete_signals/signal_1_method_1.html', graphJSON=graph_json)

@app.route('/discrete-signals/first-signal/second-method')
def second_discrete_method():
    # Obtener parametros del request
    scale_factor = request.args.get('scale_factor', type=float)
    time_shift = request.args.get('time_shift', type=float)

    # Generar señal original
    x, y = generate_first_discrete_signal()
    graph_1 = create_discrete_plotly_graph(x, y, 'Gráfica Original de la Señal Discreta 1')

    # Generar señal transformada si existen parametros de transformacion
    if scale_factor is not None and time_shift is not None:
        transformation_data, graphs_number = generate_method_2_discrete_signal_transformation(time_shift, scale_factor, '1')
        if (graphs_number == '1'):
            x_2, y_2 = transformation_data['scaled']['x'], transformation_data['scaled']['y']
            x_9, y_9 = transformation_data['shifted']['x'], transformation_data['shifted']['y']
            graph_2 = create_discrete_plotly_graph(x_2, y_2, 'Gráfica Escalada - Diezmada de la Señal Discreta 1')
            graph_9 = create_discrete_plotly_graph(x_9, y_9, 'Gráfica Desplazada - Diezmada de la Señal Discreta 1')
            
            graphiques = {
                'graphs_number': graphs_number,
                'data_1': graph_1['data'],
                'layout_1': graph_1['layout'],
                'data_2': graph_2['data'],
                'layout_2': graph_2['layout'],
                'data_3': None,
                'layout_3': None,
                'data_4': None,
                'layout_4': None,
                'data_5': None,
                'layout_5': None,
                'data_6': None,
                'layout_6': None,
                'data_7': None,
                'layout_7': None,
                'data_8': None,
                'layout_8': None,
                'data_9': graph_9['data'],
                'layout_9': graph_9['layout'],
            }
        else:
            x_2, y_2 = transformation_data['scaled']['x'], transformation_data['scaled']['y']

            x_3, y_3 = transformation_data['zeros']['x'], transformation_data['zeros']['y']
            x_4, y_4 = transformation_data['zeros_d']['x'], transformation_data['zeros_d']['y']

            x_5, y_5 = transformation_data['escalon']['x'], transformation_data['escalon']['y']
            x_6, y_6 = transformation_data['escalon_d']['x'], transformation_data['escalon_d']['y']

            x_7, y_7 = transformation_data['linear']['x'], transformation_data['linear']['y']
            x_8, y_8 = transformation_data['linear_d']['x'], transformation_data['linear_d']['y']
            x_9, y_9 = transformation_data['shifted']['x'], transformation_data['shifted']['y']
            
            graph_2 = create_discrete_plotly_graph(x_2, y_2, 'Gráfica Escalada de la Señal Discreta 1')
            graph_3 = create_discrete_plotly_graph(x_3, y_3, 'Gráfica Interpolada por cero')
            graph_4 = create_discrete_plotly_graph(x_4, y_4, 'Gráfica Interpolada por cero Desplazada')
            graph_5 = create_discrete_plotly_graph(x_5, y_5, 'Gráfica Interpolada por escalon')
            graph_6 = create_discrete_plotly_graph(x_6, y_6, 'Gráfica Interpolada por escalon Desplazada')
            graph_7 = create_discrete_plotly_graph(x_7, y_7, 'Gráfica Interpolada lineal')
            graph_8 = create_discrete_plotly_graph(x_8, y_8, 'Gráfica Interpolada lineal Desplazada')
            graph_9 = create_discrete_plotly_graph(x_9, y_9, 'Gráfica Desplazada - Diezmada de la Señal Discreta 1')
            
            graphiques = {
                'graphs_number': graphs_number,
                'data_1': graph_1['data'],
                'layout_1': graph_1['layout'],
                'data_2': graph_2['data'],
                'layout_2': graph_2['layout'],
                'data_3': graph_3['data'],
                'layout_3': graph_3['layout'],
                'data_4': graph_4['data'],
                'layout_4': graph_4['layout'],
                'data_5': graph_5['data'],
                'layout_5': graph_5['layout'],
                'data_6': graph_6['data'],
                'layout_6': graph_6['layout'],
                'data_7': graph_7['data'],
                'layout_7': graph_7['layout'],
                'data_8': graph_8['data'],
                'layout_8': graph_8['layout'],
                'data_9': None,
                'layout_9': None,
            }
    else:
        graphiques = {
            'graphs_number': '1',
            'data_1': graph_1['data'],
            'layout_1': graph_1['layout'],
            'data_2': None,
            'layout_2': None,
            'data_3': None,
            'layout_3': None,
            'data_4': None,
            'layout_4': None,
            'data_5': None,
            'layout_5': None,
            'layout_6': None,
            'data_7': None,
            'layout_7': None,
            'data_8': None,
            'layout_8': None,
            'data_9': graph_1['data'],
            'layout_9': graph_1['layout'],
        }

    # Convertir gráficos a JSON para enviarlo al front
    graph_json = json.dumps(graphiques, cls=plotly.utils.PlotlyJSONEncoder)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return graph_json
    else:
        return render_template('discrete_signals/signal_1_method_2.html', graphJSON=graph_json)

@app.route('/discrete-signals/second-signal/first-method')
def second_discrete_method_1():
    # Obtener parametros del request
    scale_factor = request.args.get('scale_factor', type=float)
    time_shift = request.args.get('time_shift', type=float)

    # Generar señal original
    x, y = generate_second_discrete_signal()
    graph_1 = create_discrete_plotly_graph(x, y, 'Gráfica Original de la Señal Discreta 2')

    # Generar señal transformada si existen parametros de transformacion
    if scale_factor is not None and time_shift is not None:
        transformation_data, graphs_number = generate_method_1_discrete_signal_transformation(time_shift, scale_factor, '2')
        if (graphs_number == '1'):
            x_2, y_2 = transformation_data['shifted']['x'], transformation_data['shifted']['y']
            x_6, y_6 = transformation_data['scaled']['x'], transformation_data['scaled']['y']
            graph_2 = create_discrete_plotly_graph(x_2, y_2, 'Gráfica Desplazada de la Señal Discreta 2')
            graph_6 = create_discrete_plotly_graph(x_6, y_6, 'Gráfica Escalada de la Señal Discreta 2')
            
            graphiques = {
                'graphs_number': graphs_number,
                'data_1': graph_1['data'],
                'layout_1': graph_1['layout'],
                'data_2': None,
                'layout_2': None,
                'data_3': None,
                'layout_3': None,
                'data_4': None,
                'layout_4': None,
                'data_5': None,
                'layout_5': None,
                'data_6': graph_6['data'],
                'layout_6': graph_6['layout'],
            }
        else:
            x_2, y_2 = transformation_data['shifted']['x'], transformation_data['shifted']['y']
            x_3, y_3 = transformation_data['zeros']['x'], transformation_data['zeros']['y']
            x_4, y_4 = transformation_data['escalon']['x'], transformation_data['escalon']['y']
            x_5, y_5 = transformation_data['linear']['x'], transformation_data['linear']['y']
            
            graph_2 = create_discrete_plotly_graph(x_2, y_2, 'Gráfica Desplazada de la Señal Discreta 2')
            graph_3 = create_discrete_plotly_graph(x_3, y_3, 'Gráfica Interpolada por cero')
            graph_4 = create_discrete_plotly_graph(x_4, y_4, 'Gráfica Interpolada por escalon')
            graph_5 = create_discrete_plotly_graph(x_5, y_5, 'Gráfica Interpolada Lineal')
            
            graphiques = {
                'graphs_number': graphs_number,
                'data_1': graph_1['data'],
                'layout_1': graph_1['layout'],
                'data_2': graph_2['data'],
                'layout_2': graph_2['layout'],
                'data_3': graph_3['data'],
                'layout_3': graph_3['layout'],
                'data_4': graph_4['data'],
                'layout_4': graph_4['layout'],
                'data_5': graph_5['data'],
                'layout_5': graph_5['layout'],
                'data_6': None,
                'layout_6': None,
            }
    else:
        graphiques = {
            'graphs_number': '1',
            'data_1': graph_1['data'],
            'layout_1': graph_1['layout'],
            'data_2': None,
            'layout_2': None,
            'data_3': None,
            'layout_3': None,
            'data_4': None,
            'layout_4': None,
            'data_5': None,
            'layout_5': None,
            'data_6': graph_1['data'],
            'layout_6': graph_1['layout'],
        }

    # Convertir gráficos a JSON para enviarlo al front
    graph_json = json.dumps(graphiques, cls=plotly.utils.PlotlyJSONEncoder)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return graph_json
    else:
        return render_template('discrete_signals/signal_2_method_1.html', graphJSON=graph_json)

@app.route('/discrete-signals/second-signal/second-method')
def second_discrete_method_2():
    # Obtener parametros del request
    scale_factor = request.args.get('scale_factor', type=float)
    time_shift = request.args.get('time_shift', type=float)

    # Generar señal original
    x, y = generate_second_discrete_signal()
    graph_1 = create_discrete_plotly_graph(x, y, 'Gráfica Original de la Señal Discreta 2')

    # Generar señal transformada si existen parametros de transformacion
    if scale_factor is not None and time_shift is not None:
        transformation_data, graphs_number = generate_method_2_discrete_signal_transformation(time_shift, scale_factor, '2')
        if (graphs_number == '1'):
            x_2, y_2 = transformation_data['scaled']['x'], transformation_data['scaled']['y']
            x_9, y_9 = transformation_data['shifted']['x'], transformation_data['shifted']['y']
            graph_2 = create_discrete_plotly_graph(x_2, y_2, 'Gráfica Escalada - Diezmada de la Señal Discreta 2')
            graph_9 = create_discrete_plotly_graph(x_9, y_9, 'Gráfica Desplazada - Diezmada de la Señal Discreta 2')
            
            graphiques = {
                'graphs_number': graphs_number,
                'data_1': graph_1['data'],
                'layout_1': graph_1['layout'],
                'data_2': graph_2['data'],
                'layout_2': graph_2['layout'],
                'data_3': None,
                'layout_3': None,
                'data_4': None,
                'layout_4': None,
                'data_5': None,
                'layout_5': None,
                'data_6': None,
                'layout_6': None,
                'data_7': None,
                'layout_7': None,
                'data_8': None,
                'layout_8': None,
                'data_9': graph_9['data'],
                'layout_9': graph_9['layout'],
            }
        else:
            x_2, y_2 = transformation_data['scaled']['x'], transformation_data['scaled']['y']

            x_3, y_3 = transformation_data['zeros']['x'], transformation_data['zeros']['y']
            x_4, y_4 = transformation_data['zeros_d']['x'], transformation_data['zeros_d']['y']

            x_5, y_5 = transformation_data['escalon']['x'], transformation_data['escalon']['y']
            x_6, y_6 = transformation_data['escalon_d']['x'], transformation_data['escalon_d']['y']

            x_7, y_7 = transformation_data['linear']['x'], transformation_data['linear']['y']
            x_8, y_8 = transformation_data['linear_d']['x'], transformation_data['linear_d']['y']
            x_9, y_9 = transformation_data['shifted']['x'], transformation_data['shifted']['y']
            
            graph_2 = create_discrete_plotly_graph(x_2, y_2, 'Gráfica Escalada de la Señal Discreta 2')
            graph_3 = create_discrete_plotly_graph(x_3, y_3, 'Gráfica Interpolada por cero')
            graph_4 = create_discrete_plotly_graph(x_4, y_4, 'Gráfica Interpolada por cero Desplazada')
            graph_5 = create_discrete_plotly_graph(x_5, y_5, 'Gráfica Interpolada por escalon')
            graph_6 = create_discrete_plotly_graph(x_6, y_6, 'Gráfica Interpolada por escalon Desplazada')
            graph_7 = create_discrete_plotly_graph(x_7, y_7, 'Gráfica Interpolada lineal')
            graph_8 = create_discrete_plotly_graph(x_8, y_8, 'Gráfica Interpolada lineal Desplazada')
            graph_9 = create_discrete_plotly_graph(x_9, y_9, 'Gráfica Desplazada - Diezmada de la Señal Discreta 2')
            
            graphiques = {
                'graphs_number': graphs_number,
                'data_1': graph_1['data'],
                'layout_1': graph_1['layout'],
                'data_2': graph_2['data'],
                'layout_2': graph_2['layout'],
                'data_3': graph_3['data'],
                'layout_3': graph_3['layout'],
                'data_4': graph_4['data'],
                'layout_4': graph_4['layout'],
                'data_5': graph_5['data'],
                'layout_5': graph_5['layout'],
                'data_6': graph_6['data'],
                'layout_6': graph_6['layout'],
                'data_7': graph_7['data'],
                'layout_7': graph_7['layout'],
                'data_8': graph_8['data'],
                'layout_8': graph_8['layout'],
                'data_9': None,
                'layout_9': None,
            }
    else:
        graphiques = {
            'graphs_number': '1',
            'data_1': graph_1['data'],
            'layout_1': graph_1['layout'],
            'data_2': None,
            'layout_2': None,
            'data_3': None,
            'layout_3': None,
            'data_4': None,
            'layout_4': None,
            'data_5': None,
            'layout_5': None,
            'layout_6': None,
            'data_7': None,
            'layout_7': None,
            'data_8': None,
            'layout_8': None,
            'data_9': graph_1['data'],
            'layout_9': graph_1['layout'],
        }

    # Convertir gráficos a JSON para enviarlo al front
    graph_json = json.dumps(graphiques, cls=plotly.utils.PlotlyJSONEncoder)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return graph_json
    else:
        return render_template('discrete_signals/signal_2_method_2.html', graphJSON=graph_json)

@app.route('/add-signals')
def signal_sums():
    # Obtener los valores de las señales
    x_11, x_12, y_1 = generate_preview_first_sum_c_signal()
    x_21, x_22, y_2 = generate_preview_second_sum_c_signal()
    x_31, x_32, y_31, y_32 = generate_preview_first_sum_d_signal()
    x_41, x_42, y_41, y_42 = generate_preview_second_sum_d_signal()

    # Crear el gráfico
    graph_1 = create_double_continuous_plotly_graph(x_11, x_12, y_1, 'Visualización de las Señales Continuas a Sumar 1')
    graph_2 = create_double_continuous_plotly_graph(x_21, x_22, y_2, 'Visualización de las Señales Continuas a Sumar 2')
    graph_3 = create_double_discrete_plotly_graph(x_31, x_32, y_31, y_32, 'Visualización de las Señales Discretas a Sumar 1')
    graph_4 = create_double_discrete_plotly_graph(x_41, x_42, y_41, y_42, 'Visualización de las Señales Discretas a Sumar 2')

    graphiques = {
        'data_1': graph_1.get('data'),
        'layout_1': graph_1.get('layout'),
        'data_2': graph_2.get('data'),
        'layout_2': graph_2.get('layout'),
        'data_3': graph_3.get('data'),
        'layout_3': graph_3.get('layout'),
        'data_4': graph_4.get('data'),
        'layout_4': graph_4.get('layout'),
    }

    # Convertir gráfico a JSON para enviarlo al front
    graph_json = json.dumps(graphiques, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('add_signals/signals.html', graphJSON=graph_json)

@app.route('/add-signals/continuous-signals/first-signal')
def signal_sums_continuous_first():
    # Obtener los valores de las señales
    x_11, x_12 = generate_first_continuous_signal()
    x_21, x_22 = generate_first_c1_signal_transformaded()
    x_31, x_32 = generate_first_c2_signal_transformaded()
    x_41, x_42, y_4 = generate_preview_first_sum_c_signal()
    x_51, x_52 = generate_result_first_sum_c_signal()

    # Crear el gráfico
    graph_1 = create_continuous_plotly_graph(x_11, x_12, 'Visualización de las Señales Continuas a Sumar 1')
    graph_2 = create_continuous_plotly_graph(x_21, x_22, 'Visualización de las Señales Continuas a Sumar 2')
    graph_3 = create_continuous_plotly_graph(x_31, x_32, 'Visualización de las Señales Discretas a Sumar 1')
    graph_4 = create_double_continuous_plotly_graph(x_41, x_42, y_4, 'Visualización de las Señales Discretas a Sumar 2')
    graph_5 = create_continuous_plotly_graph(x_51, x_52, 'Visualización de las Señales Discretas a Sumar 2')

    graphiques = {
        'data_1': graph_1.get('data'),
        'layout_1': graph_1.get('layout'),
        'data_2': graph_2.get('data'),
        'layout_2': graph_2.get('layout'),
        'data_3': graph_3.get('data'),
        'layout_3': graph_3.get('layout'),
        'data_4': graph_4.get('data'),
        'layout_4': graph_4.get('layout'),
        'data_5': graph_5.get('data'),
        'layout_5': graph_5.get('layout'),
    }

    # Convertir gráfico a JSON para enviarlo al front
    graph_json = json.dumps(graphiques, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('add_signals/csignals_1.html', graphJSON=graph_json)

@app.route('/add-signals/continuous-signals/second-signal')
def signal_sums_continuous_second():
    # Obtener los valores de las señales
    x_11, x_12 = generate_second_continuous_signal()
    x_21, x_22 = generate_second_c1_signal_transformaded()
    x_31, x_32 = generate_second_c2_signal_transformaded()
    x_41, x_42, y_41, y_42 = generate_preview_second_sum_d_signal()
    x_51, x_52 = generate_result_second_sum_c_signal()

    # Crear el gráfico
    graph_1 = create_continuous_plotly_graph(x_11, x_12, 'Visualización de las Señales Continuas a Sumar 1')
    graph_2 = create_continuous_plotly_graph(x_21, x_22, 'Visualización de las Señales Continuas a Sumar 2')
    graph_3 = create_continuous_plotly_graph(x_31, x_32, 'Visualización de las Señales Discretas a Sumar 1')
    graph_4 = create_double_continuous_plotly_graph(x_41, x_42, y_41, y_42, 'Visualización de las Señales Discretas a Sumar 2')
    graph_5 = create_continuous_plotly_graph(x_51, x_52, 'Visualización de las Señales Discretas a Sumar 2')

    graphiques = {
        'data_1': graph_1.get('data'),
        'layout_1': graph_1.get('layout'),
        'data_2': graph_2.get('data'),
        'layout_2': graph_2.get('layout'),
        'data_3': graph_3.get('data'),
        'layout_3': graph_3.get('layout'),
        'data_4': graph_4.get('data'),
        'layout_4': graph_4.get('layout'),
        'data_5': graph_5.get('data'),
        'layout_5': graph_5.get('layout'),
    }

    # Convertir gráfico a JSON para enviarlo al front
    graph_json = json.dumps(graphiques, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('add_signals/csignals_2.html', graphJSON=graph_json)

@app.route('/add-signals/discrete-signals/first-signal')
def signal_sums_discrete_first():
    # Obtener los valores de las señales
    x_11, x_12 = generate_first_discrete_signal()
    x_21, x_22 = generate_first_d1_signal_transformaded()
    x_31, x_32 = generate_first_d2_signal_transformaded()
    x_41, x_42, y_41, y42 = generate_preview_first_sum_d_signal()
    x_51, x_52 = generate_result_first_sum_d_signal()

    # Crear el gráfico
    graph_1 = create_discrete_plotly_graph(x_11, x_12, 'Visualización de las Señal Discreta a Sumar 1')
    graph_2 = create_discrete_plotly_graph(x_21, x_22, 'Señal Discreta 1 transformada 1')
    graph_3 = create_discrete_plotly_graph(x_31, x_32, 'Señal Discreta 1 transformada 2')
    graph_4 = create_double_discrete_plotly_graph(x_41, x_42, y_41, y42, 'Visualización de las Señales Discretas a Sumar 1')
    graph_5 = create_discrete_plotly_graph(x_51, x_52, 'Visualización de las Señales Discretas a Sumar 1')

    graphiques = {
        'data_1': graph_1.get('data'),
        'layout_1': graph_1.get('layout'),
        'data_2': graph_2.get('data'),
        'layout_2': graph_2.get('layout'),
        'data_3': graph_3.get('data'),
        'layout_3': graph_3.get('layout'),
        'data_4': graph_4.get('data'),
        'layout_4': graph_4.get('layout'),
        'data_5': graph_5.get('data'),
        'layout_5': graph_5.get('layout'),
    }

    # Convertir gráfico a JSON para enviarlo al front
    graph_json = json.dumps(graphiques, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('add_signals/dsignals_1.html', graphJSON=graph_json)

@app.route('/add-signals/discrete-signals/second-signal')
def signal_sums_discrete_second():
    # Obtener los valores de las señales
    x_11, x_12 = generate_second_discrete_signal()
    x_21, x_22 = generate_second_d1_signal_transformaded()
    x_31, x_32 = generate_second_d2_signal_transformaded()
    x_41, x_42, y_41, y_42 = generate_preview_second_sum_d_signal()
    x_51, x_52 = generate_result_second_sum_d_signal()

    # Crear el gráfico
    graph_1 = create_discrete_plotly_graph(x_11, x_12, 'Visualización de las Señal Discreta a Sumar 2')
    graph_2 = create_discrete_plotly_graph(x_21, x_22, 'Señal Discreta 2 transformada 1')
    graph_3 = create_discrete_plotly_graph(x_31, x_32, 'Señal Discreta 2 transformada 2')
    graph_4 = create_double_discrete_plotly_graph(x_41, x_42, y_41, y_42, 'Visualización de las Señales Discretas a Sumar 2')
    graph_5 = create_discrete_plotly_graph(x_51, x_52, 'Visualización de las Señales Discretas a Sumar 2')

    graphiques = {
        'data_1': graph_1.get('data'),
        'layout_1': graph_1.get('layout'),
        'data_2': graph_2.get('data'),
        'layout_2': graph_2.get('layout'),
        'data_3': graph_3.get('data'),
        'layout_3': graph_3.get('layout'),
        'data_4': graph_4.get('data'),
        'layout_4': graph_4.get('layout'),
        'data_5': graph_5.get('data'),
        'layout_5': graph_5.get('layout'),
    }

    # Convertir gráfico a JSON para enviarlo al front
    graph_json = json.dumps(graphiques, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('add_signals/dsignals_2.html', graphJSON=graph_json)

@app.route('/credits')
def credits():
    return render_template('credits.html')

if __name__ == '__main__':
    app.run(debug=True)