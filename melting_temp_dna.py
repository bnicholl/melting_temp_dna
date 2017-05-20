#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 12:31:54 2017

@author: bennicholl
"""

from Bio import Entrez
from Bio import SeqIO
from Bio.SeqUtils import MeltingTemp as mt

  #  This algorithm gives you the melting temperature on DNA sequences    

  #  create an object on GetSample, then type in the gi number when it
  #  tells you to do so


class GetSample(object):
    
    def __init__(self):
        
        self.sequence = input('type in entrez gi number: ') 
        self.get_sequence()
        self.melting_temp()
      
#  Type in your object.record.record to get 
#  genbank file
#  Type in your object.dna_sequence to get dna sequence    
    
    
    def get_sequence(self):  
        
        Entrez.email = "bnicholl66@gmail.com"  #  Prerequisite for obtaining information from Entrez server
        handle = Entrez.efetch(db = 'nucleotide', id = self.sequence,
                       rettype = 'gb',retmode='text')
#  a file handle is a filename, or in this case the method for getting an adress
        self.record = list(SeqIO.parse(handle,'genbank')) #  can also use .read without using list
        handle.close()
        self.dna_sequence = self.record[0].seq



  #  Type in you object.mt_wallace to get wallace rule 
  #  Type in your object.mt_gc to get empirical formulas based on GC content
                                       
    def melting_temp(self):
        
        self.mt_wallace = '{:0.3f}'.format(mt.Tm_Wallace(self.dna_sequence, 
                            check = True, strict = False))
        self.mt_gc = '{:0.3f}'.format(mt.Tm_GC(self.dna_sequence,
                              check = True, strict = False))
        
        
        
        

     
    
    
    

    
  
               
               

    

          
    


