import numpy as np
from scipy.interpolate import interp1d

def generate_first_c1_signal_transformaded():
    Delta = 0.01
    tc_1 = np.arange(-2,-1+Delta,Delta)
    tc_2 = np.arange(-1,1+Delta,Delta)
    tc_3 = np.arange(1,2+Delta,Delta)

    # Definir la señal en cada tramo
    xc_1 = (tc_1)*2 + 4
    xc_2 = 2*np.ones(len(tc_2))
    xc_3 = -2*tc_3 + 4
    
    # Concatenar los valores de la señal y el tiempo
    xc1 = np.concatenate((xc_1,xc_2,xc_3))
    tc1 = np.concatenate((tc_1,tc_2,tc_3))

    # Crear los intervalos de tiempo para cada tramo de la señal
    tf2 = (tc1+1/4)*(-3)
    
    return tf2, xc1

def generate_first_c2_signal_transformaded():
    Delta = 0.01
    tc_1 = np.arange(-2,-1+Delta,Delta)
    tc_2 = np.arange(-1,1+Delta,Delta)
    tc_3 = np.arange(1,2+Delta,Delta)

    # Definir la señal en cada tramo
    xc_1 = (tc_1)*2 + 4
    xc_2 = 2*np.ones(len(tc_2))
    xc_3 = -2*tc_3 + 4
    
    # Concatenar los valores de la señal y el tiempo
    xc1 = np.concatenate((xc_1,xc_2,xc_3))
    tc1 = np.concatenate((tc_1,tc_2,tc_3))

    # Crear los intervalos de tiempo para cada tramo de la señal
    tf1 = (tc1+1/4)*(-3)
    
    return tf1, xc1

def generate_preview_first_sum_c_signal():
    Delta = 0.01
    tc_1 = np.arange(-2,-1+Delta,Delta)
    tc_2 = np.arange(-1,1+Delta,Delta)
    tc_3 = np.arange(1,2+Delta,Delta)

    # Definir la señal en cada tramo
    xc_1 = (tc_1)*2 + 4
    xc_2 = 2*np.ones(len(tc_2))
    xc_3 = -2*tc_3 + 4
    
    # Concatenar los valores de la señal y el tiempo
    xc1 = np.concatenate((xc_1,xc_2,xc_3))
    tc1 = np.concatenate((tc_1,tc_2,tc_3))

    # Crear los intervalos de tiempo para cada tramo de la señal
    tf1 = (tc1-1/3)*(2)
    tf2 = (tc1+1/4)*(-3)
    
    return tf1, tf2, xc1

def generate_result_first_sum_c_signal():
    Delta = 0.01
    tc_1 = np.arange(-2,-1+Delta,Delta)
    tc_2 = np.arange(-1,1+Delta,Delta)
    tc_3 = np.arange(1,2+Delta,Delta)

    # Definir la señal en cada tramo
    xc_1 = (tc_1)*2 + 4
    xc_2 = 2*np.ones(len(tc_2))
    xc_3 = -2*tc_3 + 4
    
    # Concatenar los valores de la señal y el tiempo
    xc1 = np.concatenate((xc_1,xc_2,xc_3))
    tc1 = np.concatenate((tc_1,tc_2,tc_3))

    # Crear los intervalos de tiempo para cada tramo de la señal
    tf1 = (tc1-1/3)*(2)
    tf2 = (tc1+1/4)*(-3)

    interp_func1 = interp1d(tf1 , xc1, kind='linear', fill_value=0, bounds_error=False)
    interp_func2 = interp1d(tf2, xc1, kind='linear', fill_value=0, bounds_error=False)

    min_bound = min(tf1.min(), tf2.min())
    max_bound = max(tf1.max(), tf2.max())

    common_tdf = np.linspace(min_bound, max_bound , 15000)

    x_t1_interp = interp_func1(common_tdf)
    x_t2interp = interp_func2(common_tdf)

    x_tsuma = x_t1_interp + x_t2interp
    
    return common_tdf, x_tsuma





def generate_second_c1_signal_transformaded():
    Delta = 0.01
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

    # Crear los intervalos de tiempo para cada tramo de la señal
    tf21 = (tc2+1/3)*(2)
    
    return tf21, xc2

def generate_second_c2_signal_transformaded():
    Delta = 0.01
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

    # Crear los intervalos de tiempo para cada tramo de la señal
    tf22 = (tc2-1/4)*(-3)
    
    return tf22, xc2

def generate_preview_second_sum_c_signal():
    Delta = 0.01
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

    # Crear los intervalos de tiempo para cada tramo de la señal
    tf21 = (tc2+1/3)*(2)
    tf22 = (tc2-1/4)*(-3) 
    
    return tf21, tf22, xc2


def generate_result_second_sum_c_signal():
    Delta = 0.01
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

    # Crear los intervalos de tiempo para cada tramo de la señal
    tf21 = (tc2+1/3)*(2)
    tf22 = (tc2-1/4)*(-3) 
    interp_func21 = interp1d(tf21 , xc2, kind='linear', fill_value=0, bounds_error=False)
    interp_func22 = interp1d(tf22, xc2, kind='linear', fill_value=0, bounds_error=False)

    min_bound2 = min(tf21.min(), tf22.min())
    max_bound2 = max(tf21.max(), tf22.max())

    common_tdf2 = np.linspace(min_bound2, max_bound2 , 15000)

    x_t1_interp2 = interp_func21(common_tdf2)
    x_t2interp2 = interp_func22(common_tdf2)

    x_tsuma2 = x_t1_interp2 + x_t2interp2
    
    return common_tdf2, x_tsuma2