#you may use gradient descent and plotting python file with just changing the number that is worked on, the starting number, iteration number, missout function and its derivative, and also alpha. unfortunately i cannot find a way to automatically take derivative.
#importings
import matplotlib.pyplot as plt
import numpy as np
#star is the number that is worked on
star=100
#definitions of missing and differentiation functions
def missout(w):
    return ((w-3)**2)+5
def diff(w):
    return 2*w-6
#number of loops
iteration=20
#starting number
startnum=94
#definition of gradient descent function
def gradientdescent(number):
    alpha=0.025 #descent rate
    w=[startnum] #making startnum the first element of list
    for i in range(iteration):
        w.append(w[i]-alpha*diff(w[i])) #appending other elements to list
    return w
t1=np.arange(-star,star+1,1) #using numpy, creating a interval to plot. interval goes from minus star(the number worked on) to star plus one to neglect the effect of the number 0. it is ascending 1 by 1.
drawmiss = list() #created in order to plot
drawbase= list() #created in order to plot
for i in gradientdescent(star):
    drawmiss.append(missout(i)) #finding y components of graph
for i in range(-star,star+1):
    drawbase.append(missout(i)) #finding base of graph to see points clearly as in r
plt.plot(t1,drawbase,"k") #plotting base
plt.plot(gradientdescent(star), drawmiss, "k", color='red') #plotting points and making connections between them
plt.plot(gradientdescent(star), drawmiss, "o", color='blue') #making points more distinguishable
plt.show() #showing final graph.
#created with love
