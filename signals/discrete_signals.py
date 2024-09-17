import numpy as np
import plotly.graph_objs as go

# Estilos generales
COLORS = {
    'background': '#fcf8f3',
    'text': '#4b2e24',
    'button': '#b88b68'
}

def create_discrete_plotly_graph(x, y, title):
    stems = go.Scatter(
        x=np.repeat(x, 3),
        y=np.ravel(np.column_stack((np.zeros_like(y), y, np.zeros_like(y)))),
        mode='lines',
        line=dict(color='#b88b68', width=2),
        showlegend=False
    )
    markers = go.Scatter(
        x=x,
        y=y,
        mode='markers',
        marker=dict(color='#b88b68', size=10),
        showlegend=False
    )
    trace = [stems, markers]

    layout = go.Layout(
        title=title,
        xaxis={'title': 'Índice (n)'},
        yaxis={'title': 'Amplitud'},
        plot_bgcolor=COLORS['background'],
        paper_bgcolor=COLORS['background'],
        margin={'l': 40, 'r': 40, 't': 40, 'b': 40},
        font={'color': COLORS['text']}
    )
    
    return {'data': trace, 'layout': layout}

def create_double_discrete_plotly_graph(x1, x2, y1, y2, title):
    # First graph (stems and markers)
    stems1 = go.Scatter(
        x=np.repeat(x1, 3),
        y=np.ravel(np.column_stack((np.zeros_like(y1), y1, np.zeros_like(y1)))),
        mode='lines',
        line=dict(color='#d6b197', width=2),
        showlegend=False
    )
    markers1 = go.Scatter(
        x=x1,
        y=y1,
        mode='markers',
        marker=dict(color='#d6b197', size=10),
        showlegend=False
    )

    # Second graph (stems and markers)
    stems2 = go.Scatter(
        x=np.repeat(x2, 3),
        y=np.ravel(np.column_stack((np.zeros_like(y2), y2, np.zeros_like(y2)))),
        mode='lines',
        line=dict(color='#8a6600', width=2),
        showlegend=False
    )
    markers2 = go.Scatter(
        x=x2,
        y=y2,
        mode='markers',
        marker=dict(color='#8a6600', size=10),
        showlegend=False
    )

    # Combine all traces
    trace = [stems1, markers1, stems2, markers2]

    # Define layout
    layout = go.Layout(
        title=title,
        xaxis={'title': 'Índice (n)'},
        yaxis={'title': 'Amplitud'},
        plot_bgcolor=COLORS['background'],
        paper_bgcolor=COLORS['background'],
        margin={'l': 40, 'r': 40, 't': 40, 'b': 40},
        font={'color': COLORS['text']}
    )

    # Return the data and layout as dictionary (for Dash)
    return {'data': trace, 'layout': layout}

def generate_first_discrete_signal():
    x_n = [0,0,0,0,0,-3,0,5,4,-2,-4,-1,2,5,7,4,-2,0,0,0,0,0]
    t_n = np.arange(-5,17)

    return t_n, x_n

def generate_second_discrete_signal():
    n2_1 = np.arange(-10,-6+1)
    n2_2 = np.arange(-5,0+1)
    n2_3 = np.arange(1,5+1)
    n2_4 = np.arange(6,10+1)
    tn2 = np.concatenate((n2_1,n2_2,n2_3,n2_4))

    x2d_n = np.zeros(len(n2_1))
    x2d_2 = (2/3)**n2_2
    x2d_3 = (8/5)**n2_3
    x2d_4 = np.zeros(len(n2_4))
    xn2 = np.concatenate((x2d_n,x2d_2,x2d_3,x2d_4))

    return tn2, xn2

def generate_method_1_discrete_signal_transformation(time_shift, a, signal_number):
    tn, xn = generate_first_discrete_signal() if signal_number == '1' else generate_second_discrete_signal()
    tnt = tn - time_shift
    H=len(tnt)
    M=int(abs(1/a))

    if(abs(a) < 1):  # Cuando se cumple esta condición, se interpola
        graph_number = '3'
        A = abs(a)
        tne = np.arange(tnt[0] * M, tnt[H-1] * M + 1)
        dnzero = np.zeros(len(tne))
        dnesc = np.zeros(len(tne))
        Ln = len(tne)

        for i in range(Ln):
            if i % M == 0:
                r = int(i * A)
                dnzero[i] = xn[r]  # INTERPOLACION CON CEROS
                dnesc[i] = xn[r]   # INTERPOLACION ESCALON
            else:
                dnzero[i] = 0
                dnesc[i] = dnesc[i-1]

        k = 0
        lnm = len(tne)
        xnm = np.arange(1, lnm + 1, dtype=float)

        ln = len(xn)
        for s in range(ln-1):  # INTERPOLACION LINEAL
            xnm[k] = xn[s]
            for j in range(1, M):
                dif = xn[s+1] - xn[s]
                C = dif * j * abs(a) + xn[s]
                xnm[k + 1] = C
                k = k + 1
            k = k + 1
        xnm[lnm-1] = xn[ln-1]

        if(a < 0):
            tne22 = -tne  # SE MULTIPLICA EL TIEMPO POR -1
            
    elif(abs(a) > 1):
        graph_number = '1'
        M=(abs(1/a))
        i = 0
        c = 0

        while (i < len(xn)):  # AQUÍ SE ENCUENTRA EL VALOR MINIMO Y MAXIMO QUE DEBE TENER EL VECTOR DE TIEMPO DIEZMADO
            if(tnt[i] % abs(a) == 0):
                if(c == 0):
                    tnd0 = tnt[i] / abs(a)
                    c = 1
                else:
                    tndf = tnt[i] / abs(a)
            i = i + 1

        tnd = np.arange(tnd0, tndf + 1)  # UNA VEZ SE ENCUENTRAN, SE CREA EL VECTOR
        xndiez = np.empty(len(tnd))
        g = 0
        i = 0
        while (i < len(xn)):
            if(tnt[i] % abs(a) == 0):
                xndiez[g] = xn[i]
                g = g + 1
            i = i + 1

        if(a < 0):
            print("Al ser 'a' MENOR que 0, SÍ se refleja")
            tnd = -tnd

    data = {
        'graph_number': graph_number,
        'shifted': {
            'x': tnt,
            'y': xn,
        },
        'scaled': {
            'x': tnd if graph_number == '1' else None,
            'y': xndiez if abs(a) > 1 else None,
        },
        'zeros': {
            'x': tne22+3 if a < 0 and graph_number == '3' and M==3 else tne-3 if a > 0 and graph_number == '3' and M==3 else tne22 if a < 0 and graph_number == '3' else tne if a > 0 and graph_number == '3' else None,
            'y': dnzero if graph_number == '3' else None,
        },
        'escalon': {
            'x': tne22+3 if a < 0 and graph_number == '3' and M==3 else tne-3 if a > 0 and graph_number == '3' and M==3 else tne22 if a < 0 and graph_number == '3' else tne if a > 0 and graph_number == '3' else None,
            'y': dnesc if graph_number == '3' else None,
        },
        'linear': {
            'x': tne22 if a < 0 and graph_number == '3' else tne if a > 0 and graph_number == '3' else None,
            'y': xnm if graph_number == '3' else None,
        }
    }
    return data, graph_number

def generate_method_2_discrete_signal_transformation(time_shift, a, signal_number):
    tn, xn = generate_first_discrete_signal() if signal_number == '1' else generate_second_discrete_signal()
    tnt = tn-time_shift
    H = 22 if signal_number == '1' else 21
    M = int(abs(1/a))
    n02=M*time_shift #CALCULO DEL TIEMPO NUEVO

    if(abs(a) < 1):  # Cuando se cumple esta condición, se interpola
        graph_number = '3'
        A = abs(a)
        print("LEN tn: ", len(tn))
        tne2=np.arange(tn[0]*M, tn[H-1]*M+1)
        dnzero=np.zeros(len(tne2))
        dnesc=np.zeros(len(tne2))
        Ln=len(tne2)

        print("LN: ", Ln)
        print("M: ", M)
        print("A: ", A)
        for i in range (Ln):
            if i % M==0:
                r=int(i*A)
                dnzero[i]=xn[r]  #INTERPOLACION CON CEROS
                dnesc[i]=xn[r]   #INTERPOLACION ESCALON
            else:
                dnzero[i]=0
                dnesc[i]=dnesc[i-1]

        print("DN ZERO: ", len(dnzero))
        print("DN ESC: ", len(dnesc))

        k = 0
        lnm = len(tne2)
        xnm = np.arange(1, lnm + 1, dtype=float)

        ln = len(xn)
        for s in range(ln-1):  # INTERPOLACION LINEAL
            xnm[k] = xn[s]
            for j in range(1, M):
                dif = xn[s+1] - xn[s]
                C = dif * j * abs(a) + xn[s]
                xnm[k + 1] = C
                k = k + 1
            k = k + 1
        xnm[lnm-1] = xn[ln-1]

        if(a < 0):
            tne222=-tne2  # SE MULTIPLICA EL TIEMPO POR -1
            
    elif(abs(a) > 1):
        graph_number = '1'
        i = 0
        c = 0
        tnt = tn - time_shift
        while (i < len(xn)):  # AQUÍ SE ENCUENTRA EL VALOR MINIMO Y MAXIMO QUE DEBE TENER EL VECTOR DE TIEMPO DIEZMADO
            if(tnt[i] % abs(a) == 0):
                if(c == 0):
                    tnd0 = tnt[i] / abs(a)
                    c = 1
                else:
                    tndf = tnt[i] / abs(a)
            i = i + 1
        
        tndcheat = np.arange(tnd0, tndf + 1)  # UNA VEZ SE ENCUENTRAN, SE CREA EL VECTOR TRUCADO
        xndiez=np.empty(len(tndcheat))
        g=0
        i=0
        while (i<len(xn)):  #
            if(tnt[i] % abs(a)==0):
                xndiez[g]=xn[i]
                g=g+1
            i=i+1
        XNDIEZ_M2=xndiez

        if(a < 0):
            print("Al ser 'a' MENOR que 0, SÍ se refleja")
            tndcheat = -tndcheat

        i = 0
        c = 0
        while (i < len(xn)):  # AQUÍ SE ENCUENTRA EL VALOR MINIMO Y MAXIMO QUE DEBE TENER EL VECTOR DE TIEMPO DIEZMADO
            if(tn[i] % abs(a) == 0):
                if(c == 0):
                    tnd0 = tn[i] / abs(a)
                    c = 1
                else:
                    tndf = tn[i] / abs(a)
            i = i + 1

        print("tnd0: ", tnd0)
        print("tndf: ", tndf)
        tnd = np.arange(tnd0, tndf + 1)  # UNA VEZ SE ENCUENTRAN, SE CREA EL VECTOR
        xndiez = np.empty(len(tnd))
        g = 0
        i = 0
        while (i < len(xn)):
            if(tn[i] % abs(a) == 0):
                xndiez[g] = xn[i]
                g = g + 1
            i = i + 1

        if(a < 0):
            print("Al ser 'a' MENOR que 0, SÍ se refleja")
            tnd = -tnd

    data = {
        'graph_number': graph_number,
        'scaled': {
            'x': tnd if graph_number == '1' else None,
            'y': xndiez if abs(a) > 1 else None,
        },
        'zeros': {
            'x': tne2-3 if (a > 0 and graph_number == '3' and M == 3) else tne222+3 if (a < 0 and graph_number == '3' and M == 3) else tne222 if a < 0 and graph_number == '3' else tne2 if a > 0 and graph_number == '3' else None,
            'y': dnzero if graph_number == '3' else None,
        },
        'escalon': {
            'x': tne2-3 if (a > 0 and graph_number == '3' and M == 3) else tne222+3 if (a < 0 and graph_number == '3' and M == 3) else tne222 if a < 0 and graph_number == '3' else tne2 if a > 0 and graph_number == '3' else None,
            'y': dnesc if graph_number == '3' else None,
        },
        'linear': {
            'x': tne222 if a < 0 and graph_number == '3' else tne2 if a > 0 and graph_number == '3' else None,
            'y': xnm if graph_number == '3' else None,
        },
        'zeros_d': {
            'x': (tne2-n02)-3 if (a > 0 and graph_number == '3' and M == 3) else -(-tne222-n02)+3 if (a < 0 and graph_number == '3' and M==3) else -(-tne222-n02) if a < 0 and graph_number == '3' else (tne2-n02) if a > 0 and graph_number == '3' else None,
            'y': dnzero if graph_number == '3' else None,
        },
        'escalon_d': {
            'x': (tne2-n02)-3 if (a > 0 and graph_number == '3' and M == 3) else -(-tne222-n02)+3 if (a < 0 and graph_number == '3' and M==3) else -(-tne222-n02) if a < 0 and graph_number == '3' else (tne2-n02) if a > 0 and graph_number == '3' else None,
            'y': dnesc if graph_number == '3' else None,
        },
        'linear_d': {
            'x': -(-tne222-n02) if a < 0 and graph_number == '3' else (tne2-n02) if a > 0 and graph_number == '3' else None,
            'y': xnm if graph_number == '3' else None,
        },
        'shifted': {
            'x': None if abs(a) < 1 and a < 0 else None if abs(a) < 1 and a > 0 else tndcheat,
            'y': XNDIEZ_M2 if graph_number == '1' else None,
        },
    }
    return data, graph_number