from pyrnassus.pyrnassus import *
from asyncio import *
import csv



a_avg = 0
b_avg = 0
t_avg = 0

def alpha_func(alpha_val):
	global a_avg
	a_avg = (alpha_val.TP9 + alpha_val.FP1 + alpha_val.FP2 + alpha_val.TP10)/4

def beta_func(beta_val):
	global b_avg
	b_avg = (beta_val.TP9 + beta_val.FP1 + beta_val.FP2 + beta_val.TP10)/4

def theta_func(theta_val):
    t_avg = (theta_val.TP9 + theta_val.FP1 + theta_val.FP2 + theta_val.TP10)/4
    with open('receiverFile.csv', 'w') as csvfile:
    	writer = csv.writer(csvfile, delimiter=',')
    	writer.writerow ([a_avg, b_avg, t_avg])

muse=Muse(5000)
muse.register_callback(ELEMENTS_ALPHA_RELATIVE, alpha_func)
muse.register_callback(ELEMENTS_BETA_RELATIVE,beta_func)
muse.register_callback(ELEMENTS_THETA_RELATIVE,theta_func)
muse.start()

loop = get_event_loop()

loop.run_forever()