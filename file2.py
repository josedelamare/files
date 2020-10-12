# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 13:36:07 2020

@author: José
"""
import doctest

class File:
    """ classe File
    création d’une instance File avec une liste
    Exemple
    -------
    >>> t = File()
    >>> t.est_vide()
    True
    >>> t.enfiler(5)
    >>> print(t)
    [5]
    >>> t.est_vide()
    False
    >>> t.defiler()
    5
    >>> print(t)
    []

    """

    def __init__(self):
        """"Initialisation d’une file vide"""
        self.file=[]

    def __str__(self):
        return f"{self.file}"

    def est_vide(self):
        """teste si la file est vide"""
        return self.file==[]

    def defiler(self):
        """défile"""
        assert not self.est_vide(),"File vide"
        return self.file.pop(0)

    def enfiler(self,x):
        """enfile"""
        self.file.append(x)

