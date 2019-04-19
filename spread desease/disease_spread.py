# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 21:22:13 2017

@author: Albert % Enes % Loris
"""

#### DISEASE SPREADING SIMULATION

import time
import numpy as np
import scipy
import matplotlib.pyplot as plt


def limit(array, low_limit, high_limit):
    #Returns all the values in "array" in the range defined by the low and high limits
    return np.minimum(np.maximum(array, low_limit), high_limit)

def spread_sim(N, T, sick_i, beta, gamma, periodic = True):
    ''' Simulates the disease spread in a lattice of size N, during T iterations, with a starting proportion of sick_i individuals.
    Returns the entire NxT lattice, and the proportion of sick individuals at all times    
    '''
    #Healthy (H) is 0, sick (S) is 1
    lattice = np.random.random(N) < sick_i #Each cell is randomly assigned H or S
    lattice_show = lattice.copy() #Will store all state vectors as a matrix
    sick_p = [np.sum(lattice)/float(N)] #Proportion of sick individuals over time
    
    if periodic == True:
        check_boundary = check_boundary_periodic
    else:
        check_boundary = check_boundary_nonperiodic
    
    plt.figure(1)
    for i in range(T-1):
        sick_ind = np.where(lattice)[0] #Index of sick cells
        sick_total = len(sick_ind)
        
        #Spread phase       
        sick_chances = np.random.rand(sick_total*2)
        neighbours = np.hstack((sick_ind-1, sick_ind+1)) #Indexes of neighbours to S cells
        infected = set(neighbours[sick_chances < beta]) #Indexes of infected neighbours
        
        infected = check_boundary(infected,N) #Boundary condition 
        
        #Recovery phase
        recovered_ind = sick_ind[np.random.random(sick_total) < gamma]
        lattice[recovered_ind] = 0 #Sick -> Healthy
        
        #Infection phase (Recovered individuals might turn sick in the same step)
        lattice[infected] = 1 #Healthy -> Sick
        
        #Store data
        lattice_show = np.vstack((lattice_show, lattice))
        sick_p.append(sick_total/float(N))
        
    return sick_p, lattice_show

    
def get_statistics_sim(repetitions, N, T, sick_i, beta, gamma):
    ''' Simulates the disease with the given parameters a specific number of times, returning an average of the results'''
    store_lattice = np.zeros((T,N))
    store_sick_p = np.zeros(T)
    for j in range(repetitions):
        sick_p, lattice_show = spread_sim(N, T, sick_i, beta, gamma)
        store_sick_p += sick_p
        store_lattice += lattice_show
        
    store_sick_p = store_sick_p/float(repetitions)
    store_lattice = store_lattice/float(repetitions)
    
    return store_sick_p, store_lattice
    
def check_boundary_periodic(l,N):
    ''' Returns the list of indices l as if the cell was periodic '''
    return [i % N for i in l]
    
def check_boundary_nonperiodic(l,N):
    ''' Returns the list of indices l as if the cell was not periodic '''
    return [i for i in l if i not in [-1, N]]
    
    
def spread_sim_eff(N, T, sick_i, beta, gamma, periodic = True):  
    ''' Simulates the disease spread in a lattice of size N, during T iterations, with a starting proportion of sick_i individuals.
    Returns only the proportion of sick individuals at the end of the simulation.  
    '''
    #Healthy (H) is 0, sick (S) is 1
    lattice = np.random.random(N) < sick_i #Each cell is randomly assigned H or S
    sick_p = [np.sum(lattice)/float(N)] #Proportion of sick individuals over time
    
    if periodic == True:
        check_boundary = check_boundary_periodic
    else:
        check_boundary = check_boundary_nonperiodic
    
    plt.figure(1)
    for i in range(T-1):
        sick_ind = np.where(lattice)[0] #Index of sick cells
        sick_total = len(sick_ind)
        
        #Spread phase       
        sick_chances = np.random.rand(sick_total*2)
        neighbours = np.hstack((sick_ind-1, sick_ind+1)) #Indexes of neighbours to S cells
        infected = set(neighbours[sick_chances < beta]) #Indexes of infected neighbours
        
        infected = check_boundary(infected,N) #Boundary condition
        
        #Recovery phase
        recovered_ind = sick_ind[np.random.random(sick_total) < gamma]
        lattice[recovered_ind] = 0 #Sick -> Healthy
        
        #Infection phase (Recovered individuals might turn sick in the same step)
        lattice[infected] = 1 #Healthy -> Sick

    sick_p = sick_total/float(N)
    return sick_p
    
    
def get_statistics_sim_eff(repetitions, N, T, sick_i, beta, gamma, periodic = True):
    ''' Simulates the disease with the given parameters a specific number of times, returning an average of the results'''
    store_sick_p = 0
    for j in range(repetitions):
        sick_p = spread_sim_eff(N, T, sick_i, beta, gamma, periodic = True)
        store_sick_p += sick_p
        
    store_sick_p = store_sick_p/float(repetitions)
    
    return store_sick_p
    
    
def find_critical_point_index(l, thresh = 0.02):
    #Finds the critical point of a bifurcation map
    l_thresh = np.array(l) > thresh
    try:
        return list(l_thresh).index(True)
    except ValueError:
        return -1

def figure_1():
 
    ##### FIGURE 1 & 2 #####
    ## Plots the system for three different values of beta
    N = 150 #Number of cells
    T = 250 #Time steps
    sick_i = 0.5 #Chance of being sick at the start
    gamma = 0.5 #Chance of recovery
    
    repetitions = 1000
    beta_list = [0.25, 0.4, 0.6]
    sick_final = []
    
    for ii,beta in enumerate(beta_list):
        sick_p, lattice_show = get_statistics_sim(repetitions, N, T, sick_i, beta, gamma)
        sick_final.append(sick_p[-1]) #Get the last value of sick population
        
        plt.matshow(lattice_show, fignum = ii+1)
        plt.axis([0, N-1, 0, T])
        plt.xlabel('Cells'); plt.ylabel('Time'); plt.title(r'Disease spread for $\beta$ = %.2f' %beta) 
        
        print 'Beta is %.2f, %d out of %d' %(beta, ii+1, len(beta_list))
            
def figure_3(rep = 10, b_rep = 10):
 
    ###### FIGURE 3 ######
    #Bifurcation map for N = 150 and T = 250
    N = 150 #Number of cells
    T = 250 #Time steps
    sick_i = 0.5 #Chance of being sick at the start
    gamma = 0.5 #Chance of recovery
    
    beta_list = np.linspace(0,1,b_rep)
    
    sick_final = []
    plt.figure(1)
    for ii,beta in enumerate(beta_list):
        sick_p = get_statistics_sim_eff(rep, N, T, sick_i, beta, gamma)
        sick_final.append(sick_p) #Get the last value of sick population
        

        
        if ii%10 == 0:
            print 'Beta is %.2f, %d out of %d' %(beta, ii, b_rep)
    print beta_list[find_critical_point_index(sick_final)]
    
    plt.plot(beta_list, sick_final, 'r', label = 'Simulation', linewidth = 3)
    plt.xlabel(r'$\beta$'); plt.ylabel('Final sick population'); plt.title(r'Disease spread as a function of $\beta$')
    plt.grid()
    
def figure_4(parameter = 'N'):
    #### FIGURE 4 ######
    if parameter == 'N':
        #Critical point as a function of N
        T = 150 #Time steps
        sick_i = 0.5 #Chance of being sick at the start
        beta = 0.4 #Chance of infection
        gamma = 0.5 #Chance of recovery
        
        repetitions = 100
        beta_amount = 50
        beta_list = np.linspace(0,1,beta_amount)
        N_amount = 30
        N_list = 1*(10**np.linspace(1, 3, N_amount)).astype(int)
        N_list = np.linspace(10,500,N_amount).astype(int)
        
        critical_list = []
        for jj,N in enumerate(N_list):
            sick_final = []
            plt.figure(1)
            for ii,beta in enumerate(beta_list):
                sick_p = get_statistics_sim_eff(repetitions, N, T, sick_i, beta, gamma)
                sick_final.append(sick_p) #Get the last value of sick population       
        
            if jj%(N_amount/10) == 0:
                print 'N is %d, %d out of %d' %(N, jj, N_amount)
            critical = beta_list[find_critical_point_index(sick_final)]
            critical_list.append(critical)
        
        plt.plot(N_list, critical_list, 'ro', linewidth = 2)
        plt.xlabel('Population size'); plt.ylabel(r'Critical point $\beta_c$'); plt.title(r'Critical point as a function of population')
        plt.axis([N_list[0], N_list[-1], 0, 1])
        plt.grid()
        
    elif parameter == 'T':
        #Critical point as a function of T
        N = 150 #Number of cells
        sick_i = 0.5 #Chance of being sick at the start
        beta = 0.4 #Chance of infection
        gamma = 0.5 #Chance of recovery
        
        repetitions = 100
        beta_amount = 50
        beta_list = np.linspace(0,1,beta_amount)
        T_amount = 30
        T_list = np.linspace(10,500,T_amount).astype(int)

        
        critical_list = []
        for jj,T in enumerate(T_list):
            sick_final = []
            plt.figure(1)
            for ii,beta in enumerate(beta_list):
                sick_p = get_statistics_sim_eff(repetitions, N, T, sick_i, beta, gamma)
                sick_final.append(sick_p) #Get the last value of sick population       
        
            if jj%(T_amount/10) == 0:
                print 'N is %d, %d out of %d' %(N, jj, T_amount)
            critical = beta_list[find_critical_point_index(sick_final)]
            critical_list.append(critical)
        
        plt.plot(T_list, critical_list, 'ro', linewidth = 2)
        plt.xlabel('Simulation time'); plt.ylabel(r'Critical point $\beta_c$'); plt.title(r'Critical point as a function of simulation time')
        plt.axis([T_list[0], T_list[-1], 0, 1])
        plt.grid()
        
def figure_5():

    #### FIGURE 5 ######
    #Critical point as a function of N and T
    sick_i = 0.5 #Chance of being sick at the start
    gamma = 0.5 #Chance of recovery
    
    repetitions = 50
    beta_amount = 50
    N_amount = 30
    T_amount = 30
    beta_list = np.linspace(0,1,beta_amount)
    N_list = np.linspace(10, 500, N_amount).astype(int)
    T_list = np.linspace(10, 500, T_amount).astype(int)
    
    plt.figure(1)
    critical_array = np.zeros((len(T_list), len(N_list)))
    for kk, T in enumerate(T_list):
        for jj,N in enumerate(N_list):
            sick_final = []
            plt.figure(1)
            for ii,beta in enumerate(beta_list):
                sick_p = get_statistics_sim_eff(repetitions, N, T, sick_i, beta, gamma)
                sick_final.append(sick_p) #Get the last value of sick population
            critical = beta_list[find_critical_point_index(sick_final)]
            critical_array[kk,jj] = critical
#            if jj%(N_amount/10) == 0:
#                print 'N is %d, %d out of %d' %(N, jj, N_amount)
            
        if T_amount < 10 or kk%(T_amount/(10)) == 0:
            print 'T is %d and N is %d, %d out of %d' %(T, N, kk, T_amount)
    plt.pcolor(T_list, N_list, critical_array.T, cmap='RdBu', vmin=0, vmax=1)
    plt.xlabel('Simulation time'); plt.ylabel('Population size')
    plt.title('Critical point')

    plt.colorbar()
    plt.grid()

def figure_6():
    ###### FIGURE 6 ######
    #Periodic vs non-periodic
    N = 150 #Number of cells
    T = 250 #Time steps
    sick_i = 0.5 #Chance of being sick at the start
    beta = 0.4 #Chance of infection
    gamma = 0.5 #Chance of recovery
    
    repetitions = 100
    beta_amount = 100
    beta_list = np.linspace(0,1,beta_amount)
    #beta_list = [beta]
    
    plt.figure(1)
    for periodic in [True,False]:
        sick_final = []
        for ii,beta in enumerate(beta_list):
            sick_p = get_statistics_sim_eff(repetitions, N, T, sick_i, beta, gamma, periodic = periodic)
            sick_final.append(sick_p) #Get the last value of sick population
            
            if ii%10 == 0:
                print 'Beta is %.2f, %d out of %d' %(beta, ii, beta_amount)
        print beta_list[find_critical_point_index(sick_final)]
        
        if periodic == True:
            plt.plot(beta_list, sick_final, 'r', linewidth = 1, label = 'Periodic')
        else:
            plt.plot(beta_list, sick_final, 'r--', linewidth = 1, label = 'Non-periodic')
            
    plt.xlabel(r'$\beta$'); plt.ylabel('Final sick population'); plt.title(r'Disease spread as a function of $\beta$')
    plt.grid()
    plt.legend(loc = 2)
    
def figure_theory_1():
    figure_3(rep = 10, b_rep = 10)
    nn = 10000; lw = 3
    gamma = 0.5
    
    def s_fun(b, sign):
        #Sign must be 1 or -1
        num = 2 + b - 2*gamma + sign * np.sqrt(4-4*b+b**2-4*gamma + 4*b*gamma)
        den = 2*b*(1-gamma)
        return num/den    

    b0 = np.linspace(0,.25, nn)
    b1 = np.linspace(0.25,1, nn)
    plt.plot(b0, [0]*nn, 'b--', linewidth = lw)
    plt.plot(b1, s_fun(b1,-1), 'b--', label = 'Discrete model', linewidth = lw)
    plt.plot(b0, [0]*nn, 'g-.', label = 'Continuous model', linewidth = lw)
    plt.plot(b1, 1-1/(4*b1), 'g-.', linewidth = lw)
#    plt.legend(['Simulation', 'Analytical model','Continuous model'], loc = 2)
    plt.legend(loc = 2)
    plt.axis([0, 1, 0, 1])
    
    
def figure_theory_1_alt():
    bp = np.linspace(-50,0,10000)
    bm = np.linspace(0,50, 10000)
    gamma = 0.5
    
    def s_fun(b, sign):
        #Sign must be 1 or -1
        num = 2 + b - 2*gamma + sign * np.sqrt(4-4*b+b**2-4*gamma + 4*b*gamma)
        den = 2*b*(1-gamma)
        return num/den
        
    plt.plot(bp, s_fun(bp,1), 'b'); plt.plot(bm, s_fun(bm,1), 'b')
    plt.plot(bp, s_fun(bp,-1), 'r'); plt.plot(bm, s_fun(bm,-1), 'r')
    plt.axis([-1,3,-1,5])
    plt.grid()

if __name__ == '__main__':
    
    t0 = time.time()
    figure_theory_1_alt() #Call figure to draw
    print time.time()-t0    
    plt.show()
