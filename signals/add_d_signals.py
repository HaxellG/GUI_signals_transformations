import numpy as np
from scipy.interpolate import interp1d

def generate_first_d1_signal_transformaded():
    xn=[0,0,0,0,0,-3,0,5,4,-2,-4,-1,2,5,7,4,-2,0,0,0,0,0]
    tn=np.arange(-5,17)
    a=-1/3
    n0=4
    M=abs(int(1/a))
    tnt=tn-n0
    H=len(tnt)

    if(abs(a) < 1): #Cuando se cumple esta condición, se interpola

        tne=np.arange(tnt[0]*M, tnt[H-1]*M+1)
        dnzero=np.zeros(len(tne))
        dnesc=np.zeros(len(tne))
        Ln=len(tne)
        k=0
        lnm=len(tne)
        xnm=np.arange(1,lnm+1, dtype=float)


        ln=len(xn)
        for s in range(ln-1): #INTERPOLACION LINEAL
            xnm[k]=xn[s]
            for j in range(1,M):
                dif=xn[s+1]-xn[s]
                C=dif*j*abs(a)+xn[s]
                xnm[k+1]= C
                k=k+1
            k=k+1
        xnm[lnm-1]=xn[ln-1]

        if(a<0):
            print("Se realiza una interpolación. Al ser 'a' mMENOR que 0, SÍ se refleja")
            print("")
            tne22=-tne #SE MULTIPLICA EL TIEMPO POR -1
    
    return tne22, xnm

def generate_first_d2_signal_transformaded():
    xn=[0,0,0,0,0,-3,0,5,4,-2,-4,-1,2,5,7,4,-2,0,0,0,0,0]
    tn=np.arange(-5,17)
    a=1/4
    n0=-3
    M=abs(int(1/a))
    tnt=tn-n0
    H=len(tnt)

    if(abs(a)<1): #Cuando se cumple esta condición, se interpola
        tne1=np.arange(tnt[0]*M, tnt[H-1]*M+1)
        print(tne1)
        k=0
        lnm=len(tne1)
        xnmq=np.arange(1,lnm+1, dtype=float)


        ln=len(xn)
        for s in range(ln-1): #INTERPOLACION LINEAL
            xnmq[k]=xn[s]
            for j in range(1,M):
                dif=xn[s+1]-xn[s]
                C=dif*j*abs(a)+xn[s]
                xnmq[k+1]= C
                k=k+1
            k=k+1
        xnmq[lnm-1]=xn[ln-1]

        if (a>0):
            print("Se realiza una interpolación. Al ser 'a' MAYOR que 0, NO se refleja")
    
    return tne1, xnmq

def generate_preview_first_sum_d_signal():
    xn=[0,0,0,0,0,-3,0,5,4,-2,-4,-1,2,5,7,4,-2,0,0,0,0,0]
    tn=np.arange(-5,17)
    a=-1/3
    n0=4
    M=abs(int(1/a))
    tnt=tn-n0
    H=len(tnt)

    if(abs(a) < 1): #Cuando se cumple esta condición, se interpola

        tne=np.arange(tnt[0]*M, tnt[H-1]*M+1)
        dnzero=np.zeros(len(tne))
        dnesc=np.zeros(len(tne))
        Ln=len(tne)
        k=0
        lnm=len(tne)
        xnm=np.arange(1,lnm+1, dtype=float)


        ln=len(xn)
        for s in range(ln-1): #INTERPOLACION LINEAL
            xnm[k]=xn[s]
            for j in range(1,M):
                dif=xn[s+1]-xn[s]
                C=dif*j*abs(a)+xn[s]
                xnm[k+1]= C
                k=k+1
            k=k+1
        xnm[lnm-1]=xn[ln-1]

        if(a<0):
            print("Se realiza una interpolación. Al ser 'a' mMENOR que 0, SÍ se refleja")
            print("")
            tne22=-tne #SE MULTIPLICA EL TIEMPO POR -1
    
    xn=[0,0,0,0,0,-3,0,5,4,-2,-4,-1,2,5,7,4,-2,0,0,0,0,0]
    tn=np.arange(-5,17)
    a=1/4
    n0=-3
    M=abs(int(1/a))
    tnt=tn-n0
    H=len(tnt)

    if(abs(a)<1): #Cuando se cumple esta condición, se interpola
        tne1=np.arange(tnt[0]*M, tnt[H-1]*M+1)
        print(tne1)
        k=0
        lnm=len(tne1)
        xnmq=np.arange(1,lnm+1, dtype=float)


        ln=len(xn)
        for s in range(ln-1): #INTERPOLACION LINEAL
            xnmq[k]=xn[s]
            for j in range(1,M):
                dif=xn[s+1]-xn[s]
                C=dif*j*abs(a)+xn[s]
                xnmq[k+1]= C
                k=k+1
            k=k+1
        xnmq[lnm-1]=xn[ln-1] 

        if (a>0):
            print("Se realiza una interpolación. Al ser 'a' MAYOR que 0, NO se refleja")
    
    return tne22, tne1, xnm, xnmq

def generate_result_first_sum_d_signal():
    xn=[0,0,0,0,0,-3,0,5,4,-2,-4,-1,2,5,7,4,-2,0,0,0,0,0]
    tn=np.arange(-5,17)
    a=-1/3
    n0=4
    M=abs(int(1/a))
    tnt=tn-n0
    H=len(tnt)

    if(abs(a) < 1): #Cuando se cumple esta condición, se interpola

        tne=np.arange(tnt[0]*M, tnt[H-1]*M+1)
        dnzero=np.zeros(len(tne))
        dnesc=np.zeros(len(tne))
        Ln=len(tne)
        k=0
        lnm=len(tne)
        xnm=np.arange(1,lnm+1, dtype=float)


        ln=len(xn)
        for s in range(ln-1): #INTERPOLACION LINEAL
            xnm[k]=xn[s]
            for j in range(1,M):
                dif=xn[s+1]-xn[s]
                C=dif*j*abs(a)+xn[s]
                xnm[k+1]= C
                k=k+1
            k=k+1
        xnm[lnm-1]=xn[ln-1]

        if(a<0):
            print("Se realiza una interpolación. Al ser 'a' mMENOR que 0, SÍ se refleja")
            print("")
            tne22=-tne #SE MULTIPLICA EL TIEMPO POR -1
    
    xn=[0,0,0,0,0,-3,0,5,4,-2,-4,-1,2,5,7,4,-2,0,0,0,0,0]
    tn=np.arange(-5,17)
    a=1/4
    n0=-3
    M=abs(int(1/a))
    tnt=tn-n0
    H=len(tnt)

    if(abs(a)<1): #Cuando se cumple esta condición, se interpola
        tne1=np.arange(tnt[0]*M, tnt[H-1]*M+1)
        print(tne1)
        k=0
        lnm=len(tne1)
        xnmq=np.arange(1,lnm+1, dtype=float)


        ln=len(xn)
        for s in range(ln-1): #INTERPOLACION LINEAL
            xnmq[k]=xn[s]
            for j in range(1,M):
                dif=xn[s+1]-xn[s]
                C=dif*j*abs(a)+xn[s]
                xnmq[k+1]= C
                k=k+1
            k=k+1
        xnmq[lnm-1]=xn[ln-1] 

        if (a>0):
            print("Se realiza una interpolación. Al ser 'a' MAYOR que 0, NO se refleja")

    max_length = max(tne1.max(), tne22.max())
    min_length = min(tne1.min(), tne22.min())
    nt = np.arange(min_length,max_length+1)

    ip1= interp1d(tne1, xnmq, fill_value=0, bounds_error=False)
    ip2= interp1d(tne22, xnm, fill_value=0, bounds_error=False)
    x_nt1 = ip1(nt)
    x_nt2 = ip2(nt)

    x_tsuma = x_nt1 + x_nt2
    
    return nt, x_tsuma




def generate_second_d1_signal_transformaded():
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

    #Segundo señal
    a=-1/3
    n0=4
    M=abs(int(1/a))
    tnt=tn2-n0
    H=len(tnt)

    if(abs(a) < 1): #Cuando se cumple esta condición, se interpola
        tne=np.arange(tnt[0]*M, tnt[H-1]*M+1)

        k=0
        lnm=len(tne)
        xnm=np.arange(1,lnm+1, dtype=float)


        ln=len(xn2)
        for s in range(ln-1): #INTERPOLACION LINEAL
            xnm[k]=xn2[s]
            for j in range(1,M):
                dif=xn2[s+1]-xn2[s]
                C=dif*j*abs(a)+xn2[s]
                xnm[k+1]= C
                k=k+1
            k=k+1
        xnm[lnm-1]=xn2[ln-1]

        if(a<0):
            print("Se realiza una interpolación. Al ser 'a' mMENOR que 0, SÍ se refleja")
            print("")


            tne22=-tne #SE MULTIPLICA EL TIEMPO POR -1
    
    return tne22, xnm

def generate_second_d2_signal_transformaded():
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

    a=1/4
    n0=-3
    M=(int(1/a))
    n02=M*n0 #CALCULO DEL TIEMPO NUEVO
    tnt=tn2-n0
    H=len(tnt)

    if(abs(a)<1): #Cuando se cumple esta condición, se interpola
        A=abs(a)
        tne=np.arange(tnt[0]*M, tnt[H-1]*M+1)
        dnzero=np.zeros(len(tne))
        dnesc=np.zeros(len(tne))
        Ln=len(tne)
        k=0
        lnm=len(tne)
        xnmq=np.arange(1,lnm+1, dtype=float)


    ln=len(xn2)
    for s in range(ln-1): #INTERPOLACION LINEAL
        xnmq[k]=xn2[s]
        for j in range(1,M):
            dif=xn2[s+1]-xn2[s]
            C=dif*j*abs(a)+xn2[s]
            xnmq[k+1]= C
            k=k+1
        k=k+1
    xnmq[lnm-1]=xn2[ln-1]

    if (a>0):
        print("Se realiza una interpolación. Al ser 'a' MAYOR que 0, NO se refleja")
    
    return tne, xnmq

def generate_preview_second_sum_d_signal():
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

    #Segundo señal
    a=-1/3
    n0=4
    M=abs(int(1/a))
    tnt=tn2-n0
    H=len(tnt)

    if(abs(a) < 1): #Cuando se cumple esta condición, se interpola
        tne=np.arange(tnt[0]*M, tnt[H-1]*M+1)

        k=0
        lnm=len(tne)
        xnm=np.arange(1,lnm+1, dtype=float)


        ln=len(xn2)
        for s in range(ln-1): #INTERPOLACION LINEAL
            xnm[k]=xn2[s]
            for j in range(1,M):
                dif=xn2[s+1]-xn2[s]
                C=dif*j*abs(a)+xn2[s]
                xnm[k+1]= C
                k=k+1
            k=k+1
        xnm[lnm-1]=xn2[ln-1]

        if(a<0):
            print("Se realiza una interpolación. Al ser 'a' mMENOR que 0, SÍ se refleja")
            print("")


            tne22=-tne #SE MULTIPLICA EL TIEMPO POR -1
    
    a=1/4
    n0=-3
    M=(int(1/a))
    n02=M*n0 #CALCULO DEL TIEMPO NUEVO
    tnt=tn2-n0
    H=len(tnt)

    if(abs(a)<1): #Cuando se cumple esta condición, se interpola
        A=abs(a)
        tne=np.arange(tnt[0]*M, tnt[H-1]*M+1)
        dnzero=np.zeros(len(tne))
        dnesc=np.zeros(len(tne))
        Ln=len(tne)
        k=0
        lnm=len(tne)
        xnmq=np.arange(1,lnm+1, dtype=float)


    ln=len(xn2)
    for s in range(ln-1): #INTERPOLACION LINEAL
        xnmq[k]=xn2[s]
        for j in range(1,M):
            dif=xn2[s+1]-xn2[s]
            C=dif*j*abs(a)+xn2[s]
            xnmq[k+1]= C
            k=k+1
        k=k+1
    xnmq[lnm-1]=xn2[ln-1]

    if (a>0):
        print("Se realiza una interpolación. Al ser 'a' MAYOR que 0, NO se refleja")
    
    return tne22, tne, xnm, xnmq


def generate_result_second_sum_d_signal():
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

    #Segundo señal
    a=-1/3
    n0=4
    M=abs(int(1/a))
    tnt=tn2-n0
    H=len(tnt)

    if(abs(a) < 1): #Cuando se cumple esta condición, se interpola
        tne=np.arange(tnt[0]*M, tnt[H-1]*M+1)

        k=0
        lnm=len(tne)
        xnm=np.arange(1,lnm+1, dtype=float)


        ln=len(xn2)
        for s in range(ln-1): #INTERPOLACION LINEAL
            xnm[k]=xn2[s]
            for j in range(1,M):
                dif=xn2[s+1]-xn2[s]
                C=dif*j*abs(a)+xn2[s]
                xnm[k+1]= C
                k=k+1
            k=k+1
        xnm[lnm-1]=xn2[ln-1]

        if(a<0):
            print("Se realiza una interpolación. Al ser 'a' mMENOR que 0, SÍ se refleja")
            print("")


            tne22=-tne #SE MULTIPLICA EL TIEMPO POR -1
    
    a=1/4
    n0=-3
    M=(int(1/a))
    n02=M*n0 #CALCULO DEL TIEMPO NUEVO
    tnt=tn2-n0
    H=len(tnt)

    if(abs(a)<1): #Cuando se cumple esta condición, se interpola
        A=abs(a)
        tne=np.arange(tnt[0]*M, tnt[H-1]*M+1)
        dnzero=np.zeros(len(tne))
        dnesc=np.zeros(len(tne))
        Ln=len(tne)
        k=0
        lnm=len(tne)
        xnmq=np.arange(1,lnm+1, dtype=float)


    ln=len(xn2)
    for s in range(ln-1): #INTERPOLACION LINEAL
        xnmq[k]=xn2[s]
        for j in range(1,M):
            dif=xn2[s+1]-xn2[s]
            C=dif*j*abs(a)+xn2[s]
            xnmq[k+1]= C
            k=k+1
        k=k+1
    xnmq[lnm-1]=xn2[ln-1]

    if (a>0):
        print("Se realiza una interpolación. Al ser 'a' MAYOR que 0, NO se refleja")

    max_length = max(tne.max(), tne22.max())
    min_length = min(tne.min(), tne22.min())
    nt = np.arange(min_length,max_length+1)

    ip1= interp1d(tne, xnmq, fill_value=0, bounds_error=False)
    ip2= interp1d(tne22, xnm, fill_value=0, bounds_error=False)
    x_nt1 = ip1(nt)
    x_nt2 = ip2(nt)

    x_tsuma = x_nt1+ x_nt2
        
    return nt, x_tsuma