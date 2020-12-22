# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 19:32:16 2020

Semesterarbeit Teil 2
@author: Norman
"""
import math

class Corpus:
    
    def __init__(self):
        self.documents = []
        
    def read_documents(self,document_name,path):
        
        text =[]
        with open(path) as datei:
            for line in datei:
                text += line.split()
                    
                
        result = {}
        for w in text:
            result[w] = text.count(w)
        
        self.documents.append(Document(document_name, path, result))
    
    def list_documents_names(self):
        
        result =[]
        for doc in self.documents:
            result.append(doc.name)
        return result
    

    def remove_document(self, document_name):
        for doc in self.documents:
            if document_name == doc.name:
                self.documents.remove(doc)
            
    def find_documents(self,document_name):
        for doc in self.documents:
            if doc.name == document_name:
                return doc
        print("Kein Dokument vorhanden")
        
        
    def tf(self, term, document_name):
        
        document = self.find_document(document_name)
        
        if term in document.word_count:
            x = document.word_count[term]
            return x / max(document.word_count.values())
        else:
            return 0
        
    def idf(self,term):
        
        zaehler =0
        for doc in self.documents:
            if term in doc.word_count:
                zahler += 1
        
        return math.log10( len((self.documents)/ ( zaehler+1))
                          
    def tf_idf(self, term, document_name) :
        
        return self.tf(term, document_name) * self.idf(term)
                          
   




class Document:
    
    def __init__(self, name, path, word_count):
        self.name = name
        self.path =path
        self.word_count = word_count
        
    def __repr__(self):
        return "Dokumentname: {}".format(self.name)
    
    def __str__(self):
        return "Dies ist Dokument:{} mit {}".format(self.name,self.word_count)
    
        
        