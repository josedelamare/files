# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 13:36:07 2020

@author: José
"""
import doctest

class Pile:
    """ classe Pilecréation d’une instance Pile avec une liste
    Exemple
    -------
    >>> t = Pile()
    >>> t.est_vide()
    True
    >>> t.empiler(5)
    >>> print(t)
    [5]
    >>> t.est_vide()
    False
    >>> t.depiler()
    5
    >>> print(t)
    []

    """

    def __init__(self):
        """"Initialisation d’une pile vide"""
        self.pile=[]

    def __str__(self):
        return f"{self.pile}"

    def est_vide(self):
        """teste si la pile est vide"""
        return self.pile==[]

    def depiler(self):
        """dépile"""
        assert not self.est_vide(),"Pile vide"
        return self.pile.pop()

    def empiler(self,x):
        """empile"""
        self.pile.append(x)

