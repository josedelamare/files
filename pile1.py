# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 13:53:10 2020

@author: José
"""

def pile():
    """retourne une liste vide
    Exemple :
    -------
    >>> pile()
    []
    """
    return[]

def est_vide(p):
    """renvoie True si la pile est vide et False sinon
    Exemple :
    -------
    >>> est_vide([])
    True
    >>> est_vide([1, 2])
    False
    """
    return p==[]

def empiler(p,x):
    """Ajoute l’élément x à la pile p
    Exemple :
    -------
    >>> t = []
    >>> empiler(t, 5)
    >>> print(t)
    [5]
    """
    p.append(x)

def depiler(p):
    """dépile et renvoie l’élément au sommet de la pile p
    Exemple :
    -------
    >>> t = [5]
    >>> depiler(t)
    5
    >>> print(t)
    []
    """
    assert not est_vide(p), "Pile vide"
    return p.pop()
