def recherche_dicho(tab, element):
    deb = 0
    fin = len(tab)- 1
    middle = (deb + fin)//2
    if tab[middle] == element :
        return middle
    while deb <= fin :
        middle= (deb + fin) // 2
        if tab[middle] == element :
            return middle
        if tab[middle] < element :
            deb = middle + 1
        if tab[middle] > element :
            fin = middle -1
    return -1


tab =[9,15,22,39,47,51,62,74,88,93]
element = 1
positions = recherche_dicho(tab,element)

if positions != -1 :
    print(element,"est présent à la position ", positions)
else :
    print(element,"ne se trouve pas dans le tableau")
