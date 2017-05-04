import time, random
import math
from collections import deque
from Tkinter import *


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()


initial_time = time.strftime("%Y-%m-%d-%H:%M:%S")
f = open('logs/analisis-'+str(initial_time)+'.txt','w')
root = Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
var = StringVar()
var_max = StringVar()
l = Label(root, textvariable = var, font=("Courier", 44))
l2 = Label(root, textvariable = var_max, font=("Courier", 22),fg='red')
l.pack()
l2.pack()
sensores_max = [0,0,0,0,0,0]
try:
    while True:
        string = 'HORNO:HOS1,'+str(random.randint(1, 100))+';HOS2,'+str(random.randint(1, 100))+';HOS3,'+str(random.randint(1, 100))+';HOS4,'+str(random.randint(1, 100))+';HOS5,'+str(random.randint(1, 100))+';HOS6,'+str(random.randint(1, 100))+';'
        sensores = string.split(':')[1]
        sensores = sensores.replace(',','=')
        sensores = sensores.replace('S','T')
        sensores = sensores.replace('HO','')
        sensores = sensores.replace(';',' ')
        sensores = sensores + time.strftime("%H:%M:%S")
        sensors_array = sensores.split(' ')
        count = 0
        for i in sensores_max:
            value = sensores.split(' ')[count]
            value = value.split('=')[1]
            if int(value)>i:
                sensores_max[count] = int(value)
            count = count + 1
        sensores_2 = 'T1_Max='+str(sensores_max[0])+' T2_Max='+str(sensores_max[1])+' T3_Max='+str(sensores_max[2])+' T4_Max='+str(sensores_max[3])+' T5_Max='+str(sensores_max[4])+' T6_Max='+str(sensores_max[5])
        var.set(sensores)
        var_max.set(sensores_2)
        root.update_idletasks()
        f.write(sensores+'\n')
        time.sleep(1)
except KeyboardInterrupt:
    f.close()
    print 'exit'
