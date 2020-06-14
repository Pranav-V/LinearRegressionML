import numpy as np

m=0
b=0
#9 13 21 30 31 32 34
#260 320 420 530 560 580 590

x = np.matrix('9 13 21 30 31 32 34')  #initialize matrix
y = np.matrix('260 320 420 530 560 580 590')


m=y.size  #size of matrix
lrate = .005

for iter in range(10000):  #iterate
    diff = ((x*m)+b) - y  #calculate diff
    cost = (1/(2*m))*((diff*diff.getT()).sum()) #cost function
    b = b-((1/m)*(diff.sum())*(lrate))
    m = m-((1/m)*(float(diff*x.getT()))*(lrate))  #m/b reassignment
    print('M:',m,'B:',b,'C:',cost)  #print values
