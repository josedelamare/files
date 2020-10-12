# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 14:59:05 2020

@author: José
"""

from collections import deque

def file():
    """retourne une liste vide
    Exemple :
    -------
    >>> file()
    deque([])
    """
    return deque()

def est_vide(f):
    """renvoie True si la file est vide et False sinon
    Exemple :
    -------
    >>> est_vide(file())
    True
    """
    return f==deque([])

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
    """dépile et renvoie l’élément au sommet de la file f
    Exemple :
    -------
    >>> t = deque([5])
    >>> defiler(t)
    5
    >>> print(t)
    deque([])
    """
    assert not est_vide(f), "File vide"
    return f.popleft()

