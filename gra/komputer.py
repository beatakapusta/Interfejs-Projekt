"""
Class Komputer
"""
as_kier = ['s','11']
dziesiatka_kier = ['s','10']
krol_kier = ['s','4']
dama_kier = ['s','3']
walet_kier = ['s','2']
dziewiatka_kier = ['s','0']

as_karo = ['d','11']
dziesiatka_karo = ['d','10']
krol_karo = ['d','4']
dama_karo = ['d','3']
walet_karo = ['d','2']
dziewiatka_karo = ['d','0']

as_trefl = ['t','11']
dziesiatka_trefl = ['t','10']
krol_trefl = ['t','4']
dama_trefl = ['t','3']
walet_trefl = ['t','2']
dziewiatka_trefl= ['t','0']

as_pik = ['p','11']
dziesiatka_pik = ['p','10']
krol_pik = ['p','4']
dama_pik = ['p','3']
walet_pik = ['p','2']
dziewiatka_pik = ['p','0']




class Komputer:
    """
    Komputer
    """
    def __init__(self):

    A = 0
    T = 0
    K = 0
    D = 0
    W = 0
    N = 0

    para_kier = 0
    para_karo = 0
    para_trefl = 0
    para_pik = 0

    """
    Proces licytacji komputera
    """
    def policz_karty(self, karty):
        """
        Liczy liczbę wystąpienia danej karty
        """
        global A
        global T
        global K
        global D

        for i in karty:
            if i is as_kier or as_karo or as_trefl or as_pik: A += 1
            if i is dziesiatka_kier or dziesiatka_karo or dziesiatka_trefl or dziesiatka_pik: T +=1
            if i is krol_kier or krol_karo or krol_trefl or krol_pik: K +=1
            if i is dama_kier or dama_karo or dama_trefl or dama_pik: D +=1

        return A, T, K, D

    def policz_pary(self, karty):
        """
        Sprawdza czy posiada parę
        """
        if K == 0 or D == 0: return -1
        elif dama_kier and krol_kier in karty:
            para_kier = 1
            return para_kier

        elif dama_karo and krol_karo in karty:
            para_karo = 1
            return para_karo

        elif dama_trefl and krol_trefl in karty:
            para_trefl = 1
            return para_trefl

        elif dama_pik and krol_pik in karty:
            para_pik = 1
            return para_pik


