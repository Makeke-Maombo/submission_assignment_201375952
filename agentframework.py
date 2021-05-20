# -*- coding: utf-8 -*-
"""
Created on Tue May 18 21:46:22 2021

@author: ADMIN
"""

class Agent():
    
    def __init__(self,geology,transport, population):
        '''
        This instantiates the datasets as inputs

        Parameters
        ----------
        geology : TYPE
            DESCRIPTION.
        transport : TYPE
            DESCRIPTION.
        population : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        self.geology = geology
        self.population= transport
        self.transport= population
       
        
      
    def weighting(self):
        '''
        This functions intend is to implement the scrollbar values

        Returns
        -------
       A weighted list of the datasets

        '''
        for i in self.geology:
            self.geology= i*3
        for i in self.transport:
            self.transport= i*3
        for i in self.population:
            self.population= i*4

   
    def add(geology,tansport,population):
        '''
        This fuction intends to append the values from the weighted matrix

        Parameters
        ----------
        geology : TYPE
            DESCRIPTION.
        tansport : TYPE
            DESCRIPTION.
        population : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        best_site=[]
        for i,j,k in (geology,tansport,population):
            best_site=i+j+k
        #print(best_site)
    
    
