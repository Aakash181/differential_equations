import numpy
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import matplotlib.animation as animation


def deriv(y,t,alpha,bheta,gama,delta,omega):
    dy_dt=y[1]
    dv_dt= -(delta*y[1])-(bheta*y[0])-(alpha*y[0]**3)+(gama*numpy.cos(omega*t))
    y_and_v=numpy.array([dy_dt,dv_dt])
    return y_and_v


def euler(y,t,deriv1d,dt):
    #k1=deriv1d(y+k0,t+dt)*dt
    y_next= y+deriv1d(y,t,alpha,bheta,gama,delta,omega)*dt
    return y_next
 
def rk2(y,t,Aakash,dt):
    k0=Aakash(y,t,alpha,bheta,gama,delta,omega)*dt
    k1=Aakash(y+k,t+dt,alpha,bheta,gama,delta,omega)*dt
    y_next=y+(k0+k1)/2

def rk4(y,t,Aakash,dt):
    k1=Aakash(y,t,alpha,bheta,gama,delta,omega)*dt
    k2=Aakash(y+k1/2,t+dt/2,alpha,bheta,gama,delta,omega)*dt
    k3=Aakash(y+k2/2,t+dt/2,alpha,bheta,gama,delta,omega)*dt
    k4=Aakash(y+k3,t+dt,alpha,bheta,gama,delta,omega)*dt
    y_next=y+(k1+2*k2+2*k3+k4)/6
    return y_next

 

y=[0,0]
k=numpy.zeros([1000,2])
n=numpy.zeros([1000,2])
l=numpy.zeros([1000,2])
k[0,0]=0
k[0,1]=0

n[0,0]=0
n[0,1]=0

l[0,0]=0
l[0,1]=0

alpha=1
bheta=-1
gama=0.3 
delta=.5
omega=1.1
t=numpy.linspace(1,100,1000)
dt=100/1000


for j in range(999):
    n[j+1,:]=rk2(n[j],t[j],deriv,dt)


for j in range(999):
    l[j+1,:]=rk4(l[j],t[j],deriv,dt)

for j in range(999):
    k[j+1,:]=euler(k[j,:],t[j],deriv,dt)

x_euler_data=[k[j,0] for j in range(1000)]
y_euler_data=[k[j,1] for j in range(1000)]


x_rk2_data=[k[j,0] for j in range(1000)]
y_rk2_data=[k[j,1] for j in range(1000)]


x_rk4_data=[l[j,0] for j in range(1000)]
y_rk4_data=[l[j,1] for j in range(1000)]


result=odeint(deriv,y,t,args=(alpha,bheta,gama,delta,omega))
x_data=[result[j,0] for j in range (1000)]
y_data=[result[j,1] for j in range (1000)]




#_____________________________________________________________________________________________________________
#animation part
fig = plt.figure()
fig.set_facecolor("xkcd:mint green")
axis = plt.axes(xlim =(0,100),ylim =(-4,2)) 
line, = axis.plot([], [], 'r-')
line1, =axis.plot([],[], 'g-')
line2, =axis.plot([],[], 'b-')
line3, =axis.plot([],[], 'y-')

def init():
    line.set_data([],[])
    line1.set_data([],[])
    line2.set_data([],[])
    line3.set_data([],[])
    return line,line1,line2,line3
    
    	 
    

xdata, ydata = [],[] 
x1data, y1data = [], []
x2data, y2data = [], []
x3data, y3data = [], []


def animate(i):
    y =  [x_euler_data[i]-2]
    x =  [t[i]]
    yy=  [x_rk4_data[i]+1]
    yyy=  [x_rk2_data[i]]
    yyyy=  [x_data[i]]
    xdata.append(x)
    x1data.append(x)
    x2data.append(x)
    x3data.append(x)
    ydata.append(y)
    y1data.append(yy)
    y2data.append(yyy)
    y3data.append(yyyy)
    line.set_data(xdata, ydata)
    line1.set_data(x1data,y1data)
    line2.set_data(x2data,y2data)
    line3.set_data(x3data,y3data)
    return line,line1,line2,line3  
#ax=plt.axes()
#ax.set_facecolor("xkcd:mint green")
	
anims1 = animation.FuncAnimation(fig, animate, init_func = init, 
							frames = 1000, interval = 5, blit = True,repeat=False) 
fig.set_facecolor("xkcd:mint green")                            
plt.title("y Vs t")
#____________________________________________________________________________________________________
plt.legend(['euler','rk4','rk2','odeint'])

#plt.show()
"""
plt.plot(t,y_euler_data,'b.')
plt.plot(t,y_data,'r-')
plt.plot(t,y_rk2_data,'g-')
plt.plot(t,y_rk4_data,'y.')
plt.legend(['euler','odeint','rk2','rk4'])
plt.title("dy/dt Vs t")
plt.figure()
plt.plot(t,x_euler_data,'b.')
plt.plot(t,x_data,'r-')
plt.plot(t,x_rk2_data,'g-')
plt.plot(t,x_rk4_data,'y.')
plt.legend(['euler','odeint','rk2','rk4'])
plt.title("y Vs t")"""
#plt.title("y Vs t")

fig2 = plt.figure()
fig2.patch.set_facecolor("xkcd:mint green")
a_xis = plt.axes(xlim =(0,100),ylim =(-2,2)) 
l_ine, = a_xis.plot([], [], 'r-')
l_ine1, =a_xis.plot([],[], 'g*')
l_ine2, =a_xis.plot([],[], 'b-')
l_ine3, =a_xis.plot([],[], 'y.')

def inits():
    l_ine.set_data([],[])
    l_ine1.set_data([],[])
    l_ine2.set_data([],[])
    l_ine3.set_data([],[])
    return l_ine,l_ine1,l_ine2,l_ine3
    
    	 
    

xdatas, ydatas = [],[] 
x1datas, y1datas = [], []
x2datas, y2datas = [], []
x3datas, y3datas = [], []


def animates(i):
    y =  [y_euler_data[i]]
    x =  [t[i]]
    yy=  [y_rk4_data[i]+1]
    yyy=  [y_rk2_data[i]+2]
    yyyy=  [y_data[i]+3]
    xdatas.append(x)
    x1datas.append(x)
    x2datas.append(x)
    x3datas.append(x)
    ydatas.append(y)
    y1datas.append(yy)
    y2datas.append(yyy)
    y3datas.append(yyyy)
    l_ine.set_data(xdatas, ydatas)
    l_ine1.set_data(x1datas,y1datas)
    l_ine2.set_data(x1datas,y1datas)
    l_ine3.set_data(x1datas,y1datas)
    return l_ine,l_ine1,l_ine2,l_ine3  
	
anims2 = animation.FuncAnimation(fig2, animates, init_func = inits, 
							frames = 1000, interval = 5, blit = True,repeat=False) 

plt.title("dy/dt Vs t")
plt.legend(['euler','rk4','rk2','odeint'])


plt.draw()
plt.show()

 

 
