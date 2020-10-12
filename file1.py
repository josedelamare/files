# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 13:53:10 2020

@author: José
"""

def file():
    """retourne une file vide
    Exemple :
    -------
    >>> file()
    []
    """
    return[]

def est_vide(f):
    """renvoie True si la file est vide et False sinon
    Exemple :
    -------
    >>> est_vide([])
    True
    >>> est_vide([1, 2])
    False
    """
    return f==[]

def enfiler(f,x):
    """Ajoute l’élément x à la file f
    Exemple :
    -------
    >>> t = []
    >>> enfiler(t, 5)
    >>> print(t)
    [5]
    """
    f.append(x)

def defiler(f):
    """défile et renvoie l’élément au sommet de la file f
    Exemple :
    -------
    >>> t = [5, 6]
    >>> defiler(t)
    5
    >>> print(t)
    [6]
    """
    assert not est_vide(f), "Pile vide"
    return f.pop(0)

import doctest
doctest.testmod(verbose = True)
