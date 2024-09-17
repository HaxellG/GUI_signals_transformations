import numpy as np
import plotly.graph_objs as go

# Estilos generales
COLORS = {
    'background': '#fcf8f3',
    'text': '#4b2e24',
    'button': '#b88b68'
}

def create_continuous_plotly_graph(x, y, title):
    trace = go.Scatter(x=x, y=y, mode='lines', line={'color': '#8c6239'})
    layout= go.Layout(
        title=title,
        xaxis={'title': 'Tiempo (s)'},
        yaxis={'title': 'Amplitud'},
        plot_bgcolor=COLORS['background'],
        paper_bgcolor=COLORS['background'],
        margin={'l': 40, 'r': 40, 't': 40, 'b': 40},
        font={'color': COLORS['text']}
    )
    
    return {'data': [trace], 'layout': layout}

def create_double_continuous_plotly_graph(x1, x2, y, title):
    trace_1 = go.Scatter(x=x1, y=y, mode='lines', line={'color': '#4d2c14'})
    trace_2 = go.Scatter(x=x2, y=y, mode='lines', line={'color': '#bc8f00'})
    layout= go.Layout(
        title=title,
        xaxis={'title': 'Tiempo (s)'},
        yaxis={'title': 'Amplitud'},
        plot_bgcolor=COLORS['background'],
        paper_bgcolor=COLORS['background'],
        margin={'l': 40, 'r': 40, 't': 40, 'b': 40},
        font={'color': COLORS['text']}
    )
    
    return {'data': [trace_1, trace_2], 'layout': layout}

def generate_first_continuous_signal():
    Delta = 0.1
    
    # Crear los intervalos de tiempo para cada tramo de la señal
    tc_1 = np.arange(-2,-1+Delta,Delta)
    tc_2 = np.arange(-1,1+Delta,Delta)
    tc_3 = np.arange(1,2+Delta,Delta)
    
    # Definir la señal en cada tramo
    xc_1 = (tc_1)*2 + 4
    xc_2 = 2*np.ones(len(tc_2))
    xc_3 = -2*tc_3 + 4
    
    xc1 = np.concatenate((xc_1,xc_2,xc_3))
    
    # Concatenar los valores de la señal y el tiempo
    xc1 = np.concatenate((xc_1,xc_2,xc_3))
    tc1 = np.concatenate((tc_1,tc_2,tc_3))
    
    return tc1, xc1

def generate_second_continuous_signal():
    Delta = 0.1
    
    # Crear los intervalos de tiempo para cada tramo de la señal
    tc2_1 = np.arange(-3,-2+Delta,Delta)
    tc2_2 = np.arange(-2,-1+Delta,Delta)
    tc2_3 = np.arange(-1,0+Delta,Delta)
    tc2_4 = np.arange(0,2+Delta,Delta)
    tc2_5 = np.arange(2,3+Delta,Delta)
    tc2_6 = np.arange(3,3+0.00001,Delta)
    
    # Definir la señal en cada tramo
    xc2_1 = (tc2_1) + 3
    xc2_2 = 2*np.ones(len(tc2_2))
    xc2_3 = (tc2_3) + 3
    xc2_4 = -1*(tc2_4) + 3
    xc2_5 = 1*np.ones(len(tc2_5))
    xc2_6 = np.zeros(len(tc2_6))
    
    # Concatenar los valores de la señal y el tiempo
    xc2 = np.concatenate((xc2_1,xc2_2,xc2_3,xc2_4,xc2_5,xc2_6))
    tc2 = np.concatenate((tc2_1,tc2_2,tc2_3,tc2_4,tc2_5,tc2_6))
    
    return tc2, xc2

def generate_method_1_continuous_signal_transformation(time_shift, scale_factor, signal_number):
    tc1, xc1 = generate_first_continuous_signal() if signal_number == '1' else generate_second_continuous_signal()
    tdes = tc1 - time_shift
    tesc = (1/scale_factor) * tdes
    
    data = {
        'shifted': {
            'x': tdes,
            'y': xc1,
        },
        'scaled': {
            'x': tesc,
            'y': xc1,
        }
    }
    return data

def generate_method_2_continuous_signal_transformation(time_shift, scale_factor, signal_number):
    tc1, xc1 = generate_first_continuous_signal() if signal_number == '1' else generate_second_continuous_signal()
    tesc = scale_factor*tc1
    tdes = (1/scale_factor)*(time_shift)
    tn = tesc - tdes
    
    data = {
        'shifted': {
            'x': tesc,
            'y': xc1,
        },
        'scaled': {
            'x': tn,
            'y': xc1,
        }
    }
    return data