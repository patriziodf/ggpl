from pyplasm import *
from larlib import *
from numpy import *
from random import randint
import csv


#colori utilizzati
Color1=[0.9, 0.855, 0.702]
Color2=[0.9,0.88,0.88]
Color3=[0.9,0.808,0.54]
Color4=[0.678,0.678,0.678]
Color5=[0.949, 0.949, 0.949]

def fileReader(filename,h):

    with open(filename, "rb") as file:
        reader = csv.reader(file, delimiter=",")
        externalWalls = []

        for row in reader:
            x1 = float(row[0])
            x2 = float(row[1])
            y1 = float(row[2])
            y2 = float(row[3])
            externalWalls.append(OFFSET([0.15, 0.15])(POLYLINE([[x1, y1], [x2, y2]])))
        walls = PROD([STRUCT(externalWalls), Q(h)])

    return walls
def fileReader2(filename,h):

    with open(filename, "rb") as file:
        reader = csv.reader(file, delimiter=",")
        externalWalls = []

        for row in reader:
            x1 = float(row[0])
            y1 = float(row[1])
            x2 = float(row[2])
            y2 = float(row[3])
            externalWalls.append(OFFSET([0.15, 0.15])(POLYLINE([[x1, y1], [x2, y2]])))
        walls = PROD([STRUCT(externalWalls), Q(h)])

    return walls
def hex_material(color, light, trasparence):
    def hex_to_rgb(value):
        value = value.lstrip('#')
        lv = len(value)
        return map(lambda x: x / 255., list(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3)))

    params = hex_to_rgb(color) + [.1] + \
             hex_to_rgb(light) + [trasparence] + \
             hex_to_rgb(light) + [.1] + \
             hex_to_rgb("#000000") + [.1] + \
             [100]

    return MATERIAL(params)




#######################
###Piani della villa###
#######################

def piano_terra():

    muri = fileReader("walls.lines", 1.1)
    #VIEW(muri)
    muro1 = T([1,2])([-0.03,-0.03])(CUBOID([7.41, 0.03,0.5]))
    muro2 = T([1,2])([-0.06,-0.06])(CUBOID([7.47, 0.03,0.3]))
    muro3 = T([1, 2, 3])([-0.06, -0.06, 0.95])(CUBOID([7.47, 0.06, 0.15]))
    muroesterno_altezza1 = STRUCT([muro1, T(2)(7.38)(muro1), T(1)(-0.03)(R([1,2])(PI/2)(muro1)), T(1)(7.35)(R([1,2])(PI/2)(muro1))])
    muroesterno_altezza2 = STRUCT([muro2, T(2)(7.44)(muro2), T(1)(-0.09)(R([1,2])(PI/2)(muro2)), T(1)(7.35)(R([1,2])(PI/2)(muro2))])
    muroesterno_altezza3 = STRUCT([muro3, T(2)(7.41)(muro3), T(1)(-0.06)(R([1, 2])(PI / 2)(muro3)), T(1)(7.35)(R([1, 2])(PI / 2)(muro3))])
    #VIEW(muroesterno_altezza1)
    #VIEW(muroesterno_altezza2)
    #VIEW(muroesterno_altezza3)
    port = CUBOID([0.6, 0.21, 0.9])
    porta2 = STRUCT([T([1, 2])([3.4, -0.06])(port), T([1, 2])([3.4, 7.2])(port),T([1, 2])([0.15, 3.4])(R([1, 2])(PI / 2)(port)),T([1, 2])([7.41, 3.4])(R([1, 2])(PI / 2)(port))])
    portaf = STRUCT([R([1, 2])(PI / 4)(T([1, 2])([3.1, -0.15])(CUBOID([4.2, 0.3, 0.75]))),T(1)(7.4)(R([1, 2])(3 * PI / 4)(T([1, 2])([3.1, -0.15])(CUBOID([4.2, 0.3, 0.75])))),T([1,2])([3.4, 1.85])(OFFSET([0.0, 4.0])(port)),T([1, 2])([1.7, 4.05])(R([1, 2])(-PI / 2)(OFFSET([0.0, 4.0])(S(1)([0.75 / 0.6])(port))))])
    centrale = DIFFERENCE([T([1, 2])([3.7, 3.675])(DIFFERENCE([MY_CYLINDER([1.71, 1.1])(32),MY_CYLINDER([1.21, 1.1])(32)]))])
    struttura = STRUCT([fileReader("internalDoors.lines", 1), T(3)(0.575)(fileReader("windows2.lines", 0.3)), porta2,portaf])
    pavimento = STRUCT([TEXTURE("marmo_rosso2.png")(T(3)(-0.005)(CUBOID([7.35, 7.35, 0.005]))),COLOR(Color1)(T(3)(-0.012)(CUBOID([7.35, 7.35, 0.005])))])
    struttura_pavimentazione_result = COLOR(Color2)(DIFFERENCE([STRUCT([muri, centrale]), struttura]))
    #VIEW(struttura_pavimentazione_result)
    struttura2 = COLOR(Color1)(DIFFERENCE([STRUCT([muroesterno_altezza1, muroesterno_altezza2, muroesterno_altezza3]), struttura]))
    finestra1 = T([2, 3])([0.02, 0.575])(finestra2(3))
    finestrelle1 = STRUCT([T(1)(0.6)(finestra1), T(1)(2.1)(finestra1), T(1)(4.9)(finestra1),T(1)(6.35)(finestra1)])
    finestrelle2 = STRUCT([T([1,2])([0.07,0.8])(R([1, 2])(PI / 2)(finestra1)), T([1,2])([0.07,2.1])(R([1, 2])(PI / 2)(finestra1)),T([1, 2])([0.07, 4.9])(R([1, 2])(PI / 2)(finestra1)),T([1,2])([0.07,6.1])(R([1, 2])(PI / 2)(finestra1))])

    finestrelle_result = STRUCT([finestrelle1, T(1)(0.02)(finestrelle2), T(2)(7.26)(finestrelle1), T(1)(7.28)(finestrelle2)])
    #VIEW(finestrelle_result)

    portapp = T(1)(3.4)(porta(2))
    porta1 = STRUCT([portapp, T(1)(7.35)(R([1, 2])(PI / 2)(portapp)), T(2)(7.4)(R([1, 2])(-PI / 2)(portapp)),T([1, 2])([7.4, 7.35])(R([1, 2])(PI)(portapp))])
    #VIEW(porta1)
    porta2 = porta(3)
    porta2_v = STRUCT([T([1,2])([0.6,1.875])(porta2),T([1,2])([0.6,3.175])(porta2),T([1,2])([0.6,4.075])(porta2),T([1,2])([0.6,5.375])(porta2)])
    porta2_h = STRUCT([T([1,2])([2.975,0.75])(R([1,2])(PI/2)(porta(5))), T([1, 2])([2.975, 6.15])(R([1, 2])(PI / 2)(porta(5)))])
    porteInterne = STRUCT([porta2_v,porta2_h,T(1)(5.8)(porta2_v),T(1)(1.525)(porta2_h)])
    #VIEW(porteInterne)

    app2 = T([1, 2])([1.2, 0.15])(R([1, 2])(-PI / 2)(porta(4)))
    porteInterne2 = STRUCT([R([1, 2])(PI / 4)(app2), R([1, 2])(3 * PI / 4)(T([1, 2])([0.096, 0.085])(app2)),R([1, 2])(-3 * PI / 4)(T([1, 2])([0.205, -0.002])(app2)),R([1, 2])(-PI / 4)(T([1, 2])([0.1165, -0.086])(app2))])
    #VIEW(porteInterne2)
    piano_terra_result=STRUCT([struttura_pavimentazione_result, pavimento, finestrelle_result, porta1, porteInterne,T([1,2])([3.76,3.76])(porteInterne2),struttura2])
    #return STRUCT([finalGroundFloor, floor, finalDetw, finalDetd, porteInterne,T([1,2])([3.76,3.76])(porteInterne2),finalDetails])
    #vedo pavimento dall'alto
    #VIEW(piano_terra_result)

    return piano_terra_result
def piano_primo():

    muri = fileReader("walls.lines", 2.2)
    muro1 = T([1, 2])([-0.03, -0.03])(CUBOID([7.41, 0.03, 0.15]))
    muro2 = T([1, 2])([-0.06, -0.06])(CUBOID([7.47, 0.06, 0.15]))
    muroesterno_altezza1 = STRUCT([muro1, T(2)(7.38)(muro1), T(1)(-0.03)(R([1, 2])(PI / 2)(muro1)), T(1)(7.35)(R([1, 2])(PI / 2)(muro1))])
    muroesterno_altezza2 = STRUCT([muro2, T(2)(7.41)(muro2), T(1)(-0.06)(R([1, 2])(PI / 2)(muro2)), T(1)(7.35)(R([1, 2])(PI / 2)(muro2))])
    muricompletinterni = STRUCT([muri, T([1,2])([3.37,2])(CUBOID([0.66,0.3,2.1])), T([1,2])([3.37,5.05])(CUBOID([0.66,0.3,2.1])),T([1,2])([2.05,3.27])(CUBOID([0.3,0.86,2.1])), T([1,2])([5.05,3.27])(CUBOID([0.3,0.86,2.1]))])
    #VIEW(muroesterno_altezza1)
    #VIEW(muroesterno_altezza2)
    #VIEW(muricompletinterni)
    porta1 = STRUCT([CUBOID([0.6, 0.21, 1.5]), T([1, 3])([0.3, 1.5])(R([2, 3])(-PI / 2)(MY_CYLINDER([0.3, 0.21])(64)))])
    muroporta = CUBOID([0.6, 0.21, 1.4])
    muroesternoporta = STRUCT([T([1, 2])([3.4, -0.06])(muroporta), T([1, 2])([3.4, 7.2])(muroporta),T([1, 2])([0.15, 3.4])(R([1, 2])(PI / 2)(muroporta)),T([1, 2])([7.41, 3.4])(R([1, 2])(PI / 2)(muroporta))])

    elementi1 = STRUCT([R([1, 2])(PI / 4)(T([1, 2])([3.1, -0.15])(CUBOID([4.2, 0.3, 0.75]))),T(1)(7.4)(R([1, 2])(3 * PI / 4)(T([1, 2])([3.1, -0.15])(CUBOID([4.2, 0.3, 0.75])))),T([1, 2])([3.4, 1.85])(OFFSET([0.0, 4.0])(porta1)),T([1, 2])([1.7, 4.05])(R([1, 2])(-PI / 2)(OFFSET([0.0, 4.0])(S(1)([0.75 / 0.6])(porta1))))])
    elementi2 = STRUCT([R([1, 2])(PI / 4)(T([1, 2])([3.1, -0.15])(CUBOID([4.2, 0.3, 0.3]))),T(1)(7.4)(R([1, 2])(3 * PI / 4)(T([1, 2])([3.1, -0.15])(CUBOID([4.2, 0.3, 0.33]))))])
    #VIEW(elementi1)
    #VIEW(elementi2)
    elementi3 = T([1, 2])([3.7,3.675])(DIFFERENCE([MY_CYLINDER([1.45,2.16])(32),MY_CYLINDER([1.35,2.16])(100)]))
    elementi4 = COLOR(Color2)(T([1, 2,3])([3.7, 3.675, 2.16])(DIFFERENCE([MY_CYLINDER([1.71, 0.04])(32),MY_CYLINDER([1.18, 0.04])(100)])))
    #VIEW(elementi3)
    #VIEW(elementi4)
    struttura = STRUCT([fileReader("internalDoors.lines", 1), T(3)(0.3)(fileReader("windows.lines", 0.9)), muroesternoporta,elementi1, T(3)(1.25)(elementi2)])
    bordo_2livelli = COLOR(Color1)(DIFFERENCE([STRUCT([muroesterno_altezza1, T(3)(1.9)(muroesterno_altezza1), T(3)(2.05)(muroesterno_altezza2)]), muroesternoporta]))
    pavimento = STRUCT([TEXTURE("marmo_rosso2.png")(T(3)(0.001)(MKPOL([[[0,0],[0,7.35],[7.35,0],[7.35,7.35]],[[1, 2, 3, 4]],[[1]]]))), COLOR(Color2)(T(3)(-0.011)(CUBOID([7.35,7.35,0.01])))])

    piano1finale = COLOR(Color2)(DIFFERENCE([STRUCT([muricompletinterni, elementi3]), struttura]))
    #VIEW(piano1finale)

    fapp = STRUCT([finestra(1), T([1, 3])([0.09, 0.3])(finestra2(1))])
    finestrelle1 = STRUCT([ T(1)(0.51)(fapp), T(1)(6.26)(fapp)])
    finestrelle2 = STRUCT([T(2)(1.29)(R([1,2])(-PI/2)(fapp)),T(2)(6.59)(R([1,2])(-PI/2)(fapp))])
    finestrelle_result = STRUCT([finestrelle1,finestrelle2,T([1,2])([7.35,7.35])(R([1,2])(PI)(finestrelle1)), T([1,2])([7.35,7.35])(R([1,2])(-PI)(finestrelle2))])
    papp = T(1)(3.145)(STRUCT([porta_struttura(1), T(1)(0.255)(porta(1))]))
    porta1 = STRUCT([papp,T(1)(7.35)(R([1,2])(PI/2)(papp)), T(2)(7.4)(R([1,2])(-PI/2)(papp)), T([1,2])([7.4,7.35])(R([1,2])(PI)(papp))])
    finestra1 = finestra2(1)
    finestre2 = STRUCT([T([1,2,3])([2.1,0.02,0.3])(finestra1),T([1,2,3])([4.9,0.02,0.3])(finestra1),T([1,2,3])([2.1,7.23,0.3])(finestra1), T([1,2,3])([4.9,7.23,0.3])(finestra1)])
    finestravetro = T([1,3])([0.077,0.3])(R([1,2])(PI/2)(finestra2(4)))
    finestrevetro = STRUCT([T(2)(2.1)(finestravetro),T(2)(2.75)(finestravetro),T(2)(4.25)(finestravetro),T(2)(4.95)(finestravetro), T([1,2])([7.271,2.1])(finestravetro),T([1,2])([7.271,2.75])(finestravetro), T([1,2])([7.271,4.25])(finestravetro), T([1,2])([7.271,4.95])(finestravetro)])
    #VIEW(finestravetro)
    porta2 = porta(3)
    porta2_v = STRUCT([T([1, 2])([0.6, 1.875])(porta2), T([1, 2])([0.6, 3.175])(porta2), T([1, 2])([0.6, 4.075])(porta2),T([1, 2])([0.6, 5.375])(porta2)])
    porta2_h = STRUCT([T([1, 2])([2.975, 0.75])(R([1, 2])(PI / 2)(porta(5))),T([1, 2])([2.975, 6.15])(R([1, 2])(PI / 2)(porta(5)))])
    porteInterne = STRUCT([porta2_v, porta2_h, T(1)(5.8)(porta2_v), T(1)(1.525)(porta2_h)])
    app2 = T([1,2])([1.23,0.15])(R([1,2])(-PI/2)(STRUCT([porta_struttura(2), porta(4)])))
    porteInterne2 = STRUCT([R([1,2])(PI/4)(app2), R([1,2])(3*PI/4)(T([1,2])([0.096,0.085])(app2)),R([1,2])(-3*PI/4)(T([1,2])([0.205, -0.002])(app2)),R([1,2])(-PI/4)(T([1,2])([0.1165,-0.086])(app2))])
    cornice_finestra_app = T([1,2,3])([1.23,0.15,1.25])(R([1,2])(-PI/2)(finestra(2)))
    finestre_cornice = STRUCT([R([1, 2])(PI / 4)(cornice_finestra_app), R([1, 2])(3 * PI / 4)(T([1, 2])([0.096, 0.085])(cornice_finestra_app)),R([1, 2])(-3 * PI / 4)(T([1, 2])([0.205, -0.002])(cornice_finestra_app)),R([1, 2])(-PI / 4)(T([1, 2])([0.1165, -0.086])(cornice_finestra_app))])
    app_scala = T(1)(0.075)(DIFFERENCE([T(2)(-0.085)(CUBOID([0.25, 0.17, 0.055])), R([1, 2])(PI / 12)(T(2)(0.17)(CUBOID([0.35, 0.17, 0.055])))]))
    scala_interna = []
    scala_interna.append(app_scala)
    for i in range(1, 40):
        gradino = T(3)(0.055 * i)(R([1, 2])(PI / 8 * i)(app_scala))
        scala_interna.append(gradino)
    scala_chiocciola = COLOR(Color3)(STRUCT(scala_interna))
    app_scale = STRUCT([T([1,2])([5,4.9])(scala_chiocciola),T([1,2])([4.9,2.35])(R([1,2])(-PI/2)(scala_chiocciola)),T([1, 2])([2.35, 2.25])(R([1, 2])(-PI / 2)(scala_chiocciola)),T([1,2])([2.25,5])(R([1,2])(-PI)(scala_chiocciola))])
    piano_senza_muri = STRUCT([T([1, 2, 3])([3.7, 3.675, 1.9])(contorno_cupola([1.35, 1.22, 1.3, 0.13, 0.07])([1.22, 1.18, 0.03])),finestrelle_result, porta1, finestre2, finestrevetro,porteInterne, T([1,2])([3.76,3.76])(porteInterne2),T([1,2])([3.76,3.76])(finestre_cornice),app_scale, bordo_2livelli])
    #VIEW(scala_chiocciola)
    #VIEW(piano_senza_muri)
    primo_piano_result = STRUCT([piano1finale, pavimento, COLOR(Color2)(elementi4), piano_senza_muri])
    #VIEW(primo_piano_result)
    return primo_piano_result
def piano_secondo():

    muri = fileReader("walls.lines", 1.1)
    muro1 = T([1, 2])([-0.045, -0.045])(CUBOID([7.44, 0.045, 0.25]))
    muro2 = T([1, 2,3])([-0.07, -0.07,0.25])(CUBOID([7.49, 0.07, 0.05]))
    muroesterno_altezza1 = STRUCT([muro1, T(2)(7.395)(muro1), T(1)(-0.045)(R([1, 2])(PI / 2)(muro1)), T(1)(7.35)(R([1, 2])(PI / 2)(muro1))])
    muroesterno_altezza2 = STRUCT([muro2, T(2)(7.42)(muro2), T(1)(-0.07)(R([1, 2])(PI / 2)(muro2)), T(1)(7.35)(R([1, 2])(PI / 2)(muro2))])
    muroporta = CUBOID([0.6, 0.22, 0.85])
    muroesternoporta = STRUCT([T([1, 2])([3.4, -0.07])(muroporta), T([1, 2])([3.4, 7.2])(muroporta),T([1, 2])([0.15, 3.4])(R([1, 2])(PI / 2)(muroporta)),T([1, 2])([7.42, 3.4])(R([1, 2])(PI / 2)(muroporta))])
    portaf = STRUCT([R([1, 2])(PI / 4)(T([1, 2])([3.1, -0.15])(CUBOID([4.2, 0.3, 0.75]))),T(1)(7.4)(R([1, 2])(3 * PI / 4)(T([1, 2])([3.1, -0.15])(CUBOID([4.2, 0.3, 0.75]))))])
    centrale = DIFFERENCE([T([1, 2])([3.7,3.675])(DIFFERENCE([MY_CYLINDER([1.71,1.1])(32), MY_CYLINDER([1.61, 1.1])(100)]))])

    struttura = STRUCT([fileReader("internalDoors2.lines", 1), T(3)(0.6)(fileReader("windows2.lines", 0.3)),portaf, muroesternoporta])
    pavimentazione = COLOR(Color1)((DIFFERENCE([T(3)(-0.014)(CUBOID([7.35, 7.35, 0.015])), T([1, 2, 3])([2, 2, -0.014])(CUBOID([3.35, 3.35, 0.015]))])))

    struttura_pavimentazione_result = COLOR(Color2)(DIFFERENCE([STRUCT([muri, centrale]), struttura]))
    finaldetails = COLOR(Color1)(DIFFERENCE([STRUCT([muroesterno_altezza1,muroesterno_altezza2]),muroesternoporta]))
    finestra1 = T([2, 3])([0.02, 0.6])(finestra2(2))
    finestrelle1 = STRUCT([T(1)(0.6)(finestra1), T(1)(2.1)(finestra1), T(1)(4.9)(finestra1), T(1)(6.35)(finestra1)])
    finestrelle2 = STRUCT([T([1, 2])([0.07, 0.8])(R([1, 2])(PI / 2)(finestra1)), T([1, 2])([0.07, 2.1])(R([1, 2])(PI / 2)(finestra1)),T([1, 2])([0.07, 4.9])(R([1, 2])(PI / 2)(finestra1)), T([1, 2])([0.07, 6.1])(R([1, 2])(PI / 2)(finestra1))])
    finestrelle_result = STRUCT([finestrelle1, T(1)(0.07)(finestrelle2), T(2)(7.21)(finestrelle1), T(1)(7.28)(finestrelle2)])
    porta2 = porta(3)
    porta2_v = STRUCT([T([1, 2])([0.6, 1.875])(porta2), T([1, 2])([0.6, 3.175])(porta2), T([1, 2])([0.6, 4.075])(porta2),T([1, 2])([0.6, 5.375])(porta2)])
    porta2_h = STRUCT([T([1, 2])([2.975, 0.75])(R([1, 2])(PI / 2)(porta(5))), T([1, 2])([2.975, 6.15])(R([1, 2])(PI / 2)(porta(5)))])
    porteInterne = STRUCT([porta2_v, porta2_h, T(1)(5.8)(porta2_v), T(1)(1.525)(porta2_h)])
    portapp = T(1)(3.4)(porta(2))
    porta1 = STRUCT([portapp, T(1)(7.35)(R([1, 2])(PI / 2)(portapp)), T(2)(7.4)(R([1, 2])(-PI / 2)(portapp)),T([1, 2])([7.4, 7.35])(R([1, 2])(PI)(portapp))])
    app2 = T([1, 2])([1.5, 0.15])(R([1, 2])(-PI / 2)(porta(4)))
    porteInterne2 = STRUCT([R([1, 2])(PI / 4)(app2), R([1, 2])(3 * PI / 4)(T([1, 2])([0.096, 0.085])(app2)),R([1, 2])(-3 * PI / 4)(T([1, 2])([0.205, -0.002])(app2)),R([1, 2])(-PI / 4)(T([1, 2])([0.1165, -0.086])(app2))])
    secondo_piano_result=STRUCT([struttura_pavimentazione_result, finaldetails,pavimentazione, finestrelle_result, porteInterne, porta1,T([1,2])([3.76,3.76])(porteInterne2)])
    #VIEW(secondo_piano_result)
    return secondo_piano_result

#######################
####Porte e Finestre###
#######################

def finestra(tipologia):
    # tipologia == 1 finestra allungata
    # tipologia == 2 finestra bassa

    if tipologia == 1:
        app1 = T(3)(0.25)(CUBOID([0.58, 0.05, 0.05]))
        app2 = T([1, 2, 3])([0.03, 0.01, 0.2])(CUBOID([0.52, 0.04, 0.05]))
        app3 = OFFSET([0, 0.03, 0])(MKPOL([[[0.03, 0.02, 0.2], [0.04, 0.02, 0.15], [0.54, 0.02, 0.15], [0.55, 0.02, 0.2]], [[1, 2, 3, 4]], [[1]]]))
        app_buco = T([1, 3])([0.09, 0.3])(CUBOID([0.4, 0.2, 0.9]))
        fessura = DIFFERENCE([T([1, 2, 3])([0.03, 0.01, 0.3])(CUBOID([0.52, 0.04, 1.02])), app_buco])
        finestra1 = STRUCT([T([2, 3])([-0.02, 1.12])(app2), T([2, 3])([-0.04, 1.17])(app2), app1, app2, app3, fessura])

        app_ornamento_finestra = DIFFERENCE([T([2, 3])([0.06, 0.21])(R([1, 3])(-PI / 2)(MY_CYLINDER([0.06, 0.05])(16))),T(2)(0.09)(CUBOID([0.05, 0.1, 0.27]))])
        app_ornamento_finestra2 = T([2, 3])([0.07, 0.03])(R([1, 3])(-PI / 2)(MY_CYLINDER([0.03, 0.05])(16)))
        app_ornamnetno_finestra3 = OFFSET([0.05, 0, 0])(MKPOL([[[0, 0.09, 0.03], [0, 0.005, 0.19], [0, 0.045, 0.19]], [[1, 2, 3]], [[1]]]))

        ornamento_finestra = STRUCT([app_ornamento_finestra, app_ornamento_finestra2, app_ornamnetno_finestra3])

        app_tetto_finestra = OFFSET([0, 0.12, 0])(MKPOL([[[0, 0, 0], [0.345, 0, 0.2], [0.69, 0, 0], [0.05, 0, 0],[0.343, 0, 0.17], [0.66, 0, 0], [0.06, 0, 0.03],[0.63, 0, 0.03]], [[1, 2, 5, 4], [2, 3, 6, 5]], [[1]]]))
        app_tetto_finestra2 = OFFSET([0, 0.09, 0])(MKPOL([[[0, 0, 0], [0.06, 0, 0.03], [0.63, 0, 0.03], [0.69, 0, 0]], [[1, 2, 3, 4]], [[1]]]))

        tetto_finestra = STRUCT([app_tetto_finestra, T(2)(0.03)(app_tetto_finestra2)])
        finestra_result = T(2)(-0.12)(STRUCT([T(2)(0.07)(finestra1), T([1, 2, 3])([-0.02, 0.03, 1.15])(ornamento_finestra),T([1, 2, 3])([0.55, 0.03, 1.15])(ornamento_finestra), T([1, 3])([-0.055, 1.42])(tetto_finestra)]))
        finestra_result = COLOR(Color1)(finestra_result)

        # VIEW(fessura)
        # VIEW(finestra1)
        # VIEW(ornamento_finestra)
        # VIEW(tetto_finestra)
        # VIEW(finestra_result)
        return finestra_result

    elif tipologia == 2:

        app_tetto_finestra = T(2)(-0.04)(DIFFERENCE([T([1, 3])([-0.04, -0.04])(CUBOID([0.38, 0.04, 0.38])), CUBOID([0.3, 0.04, 0.3])]))
        app_tetto_finestra2 = T([1, 2, 3])([-0.04, -0.07, 0.34])(CUBOID([0.38, 0.07, 0.04]))
        app_tetto_finestra3 = T([1, 2, 3])([-0.12, -0.10, 0.38])(CUBOID([0.54, 0.10, 0.04]))
        finestra1 = STRUCT([app_tetto_finestra, app_tetto_finestra2, app_tetto_finestra3])

        app_ornamento_finestra = DIFFERENCE([T([2, 3])([0.06, 0.21])(R([1, 3])(-PI / 2)(MY_CYLINDER([0.06, 0.05])(16))),T(2)(0.09)(CUBOID([0.05, 0.1, 0.27]))])
        app_ornamento_finestra2 = T([2, 3])([0.07, 0.03])(R([1, 3])(-PI / 2)(MY_CYLINDER([0.03, 0.05])(16)))
        app_ornamnetno_finestra3 = OFFSET([0.05, 0, 0])(MKPOL([[[0, 0.09, 0.03], [0, 0.005, 0.19], [0, 0.045, 0.19]], [[1, 2, 3]], [[1]]]))

        ornamento_finestra = T([2, 3])([-0.09, 0.11])(STRUCT([app_ornamento_finestra, app_ornamento_finestra2, app_ornamnetno_finestra3]))

        finestra_result2 = STRUCT([finestra1, T(1)(-0.09)(ornamento_finestra), T(1)(0.34)(ornamento_finestra)])
        finestra_result2 = COLOR(Color1)(finestra_result2)
        # VIEW(finestra1)
        # VIEW(finestra_result2)

        return finestra_result2
def finestra2(tipologia):
    # tipologia == 1 finestre del primo piano esterne
    # tipologia == 2 finestre secondo piano esterne
    # tipologia == 3 finestre piano terra e scalinata
    # tipologia == 4 finestre primo piano piu piccole


    if tipologia == 1:
        x = [0.04, 0.14, 0.04, 0.14, 0.04]
        y = [0.04, 0.02, 0.04]
        z = [0.04, 0.6, 0.04, 0.18, 0.04]
        bool = [[[True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True]],[[True, False, True, False, True], [True, True, True, False, True], [True, False, True, False, True]],[[True, True, True, False, True], [True, True, True, False, True], [True, True, True, False, True]],[[True, False, True, False, True], [True, True, False, True, True], [True, False, True, False, True]],[[True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True]]]
        #vetro = TEXTURE("grass3.png")(OFFSET([0, 0.024, 0])(MKPOL([[[0.04, 0.038, 0.68], [0.04, 0.038, 0.86], [0.36, 0.038, 0.86], [0.36, 0.038, 0.68]],[[1, 2, 3, 4]],[[1]]])))
        vetro = (OFFSET([0, 0.024, 0])(MKPOL([[[0.04, 0.038, 0.68], [0.04, 0.038, 0.86], [0.36, 0.038, 0.86], [0.36, 0.038, 0.68]],[[1, 2, 3, 4]],[[1]]])))
        vetro=hex_material("#71b2cf", "#71b2cf", .85)(vetro)
        finestra_result = STRUCT([porte_e_finestre(x, y, z, bool, "finestra2"), vetro])
        # VIEW(finestra_result)
        return finestra_result
    elif tipologia == 2:
        x = [0.04, 0.145, 0.03, 0.145, 0.04]
        y = [0.04, 0.02, 0.04]
        z = [0.04, 0.22, 0.04]
        bool = [[[True, True, True], [True, True, True], [True, True, True]],[[True, False, True], [True, True, True], [True, False, True]],[[True, True, True], [True, True, True], [True, True, True]],[[True, False, True], [True, True, True], [True, False, True]],[[True, True, True], [True, True, True], [True, True, True]]]
        finestra_result2 = porte_e_finestre(x, y, z, bool, "finestra2")
        # VIEW(finestra_result2)
        return finestra_result2
    elif tipologia == 3:
        x = [0.03, 0.052, 0.02, 0.052, 0.02, 0.052, 0.02, 0.052, 0.02, 0.052, 0.03]
        y = [0.02, 0.01, 0.02]
        z = [0.03, 0.032, 0.02, 0.032, 0.02, 0.032, 0.02, 0.032, 0.02, 0.032, 0.03]
        bool = [[[True, True, True, True, True, True, True, True, True, True, True],[True, True, True, True, True, True, True, True, True, True, True],[True, True, True, True, True, True, True, True, True, True, True]], [[True, False, True, False, True, False, True, False, True, False, True],[True, True, True, True, True, True, True, True, True, True, True],[True, False, True, False, True, False, True, False, True, False, True]],[[True, True, True, True, True, True, True, True, True, True, True],[True, True, True, True, True, True, True, True, True, True, True],[True, True, True, True, True, True, True, True, True, True, True]], [[True, False, True, False, True, False, True, False, True, False, True],[True, True, True, True, True, True, True, True, True, True, True], [True, False, True, False, True, False, True, False, True, False, True]], [[True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True],[True, True, True, True, True, True, True, True, True, True, True]], [[True, False, True, False, True, False, True, False, True, False, True],[True, True, True, True, True, True, True, True, True, True, True],[True, False, True, False, True, False, True, False, True, False, True]],[[True, True, True, True, True, True, True, True, True, True, True], [True, True, True, True, True, True, True, True, True, True, True],[True, True, True, True, True, True, True, True, True, True, True]],[[True, False, True, False, True, False, True, False, True, False, True],[True, True, True, True, True, True, True, True, True, True, True],[True, False, True, False, True, False, True, False, True, False, True]],[[True, True, True, True, True, True, True, True, True, True, True],[True, True, True, True, True, True, True, True, True, True, True],[True, True, True, True, True, True, True, True, True, True, True]],[[True, False, True, False, True, False, True, False, True, False, True],[True, True, True, True, True, True, True, True, True, True, True],[True, False, True, False, True, False, True, False, True, False, True]],[[True, True, True, True, True, True, True, True, True, True, True],[True, True, True, True, True, True, True, True, True, True, True],[True, True, True, True, True, True, True, True, True, True, True]]]
        finestra_result3 = porte_e_finestre(x, y, z, bool, "finestra2")
        # VIEW(finestra_result3)
        return finestra_result3
    elif tipologia == 4:
        x = [0.02, 0.12, 0.02, 0.12, 0.02]
        y = [0.03, 0.015, 0.03]
        z = [0.035, 0.6, 0.04, 0.19, 0.035]
        bool = [[[True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True]],[[True, False, True, False, True], [True, True, True, False, True], [True, False, True, False, True]],[[True, True, True, False, True], [True, True, True, False, True], [True, True, True, False, True]], [[True, False, True, False, True], [True, True, False, True, True], [True, False, True, False, True]],[[True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True]]]
        #vetro = TEXTURE("grass3.png")(OFFSET([0, 0.019, 0])(MKPOL([[[0.02, 0.028, 0.675], [0.02, 0.028, 0.865], [0.28, 0.028, 0.865], [0.28, 0.028, 0.675]], [[1, 2, 3, 4]],[[1]]])))
        vetro = (OFFSET([0, 0.019, 0])(MKPOL([[[0.02, 0.028, 0.675], [0.02, 0.028, 0.865], [0.28, 0.028, 0.865], [0.28, 0.028, 0.675]], [[1, 2, 3, 4]],[[1]]])))
        vetro = hex_material("#71b2cf", "#71b2cf", .85)(vetro)
        finestra_result4 = STRUCT([porte_e_finestre(x, y, z, bool, "finestra2"), vetro])
        # VIEW(finestra_result4)
        return finestra_result4
def porta_struttura(tipologia):
    # tipologia == 1 porta esterna
    # tipologia == 2 porta interna

    if tipologia == 1:

        app_porta = STRUCT([T([1, 2])([0.195, 0.075])(CUBOID([0.72, 0.08, 1.52])),T([1, 2])([0.135, 0.115])(CUBOID([0.84, 0.04, 1.64]))])
        fessura_porta = COLOR(Color1)(DIFFERENCE([app_porta, T(1)(0.255)(CUBOID([0.6, 0.5, 1.4]))]))

        app_ornamento = OFFSET([0.1, 0, 0])(MKPOL([[[0, 0.135, 0.03], [0, 0.015, 0.255], [0, 0.08, 0.255]], [[1, 2, 3]], [[1]]]))
        app_ornamento_porta = DIFFERENCE([T([2, 3])([0.09, 0.3])(R([1, 3])(-PI / 2)(MY_CYLINDER([0.09, 0.1])(16))), T(2)(0.135)(CUBOID([0.2, 0.7, 0.4]))])
        app_ornamento_porta2 = T([2, 3])([0.105, 0.03])(R([1, 3])(-PI / 2)(MY_CYLINDER([0.03, 0.1])(16)))
        ornamento_porta = COLOR(Color1)(STRUCT([app_ornamento, app_ornamento_porta, app_ornamento_porta2]))

        app_tetto_porta = T(2)(0.035)(OFFSET([0, 0.12, 0])(MKPOL([[[0, 0, 1.64], [0.555, 0, 1.87], [1.11, 0, 1.64], [1.035, 0, 1.64], [0.075, 0, 1.64], [0.555, 0, 1.83]],[[1, 2, 6, 5], [2, 6, 4, 3]], [[1]]])))
        app_tetto_porta2 = T(2)(0.065)(OFFSET([0, 0.09, 0])(MKPOL([[[0, 0, 1.64], [0.1, 0, 1.68], [1.01, 0, 1.68], [1.11, 0, 1.64]], [[1, 2, 3, 4]], [[1]]])))
        app_tetto_porta3 = COLOR(Color2)(T(2)(0.115)(OFFSET([0, 0.04, 0])(MKPOL([[[1.035, 0, 1.64], [0.075, 0, 1.64], [0.555, 0, 1.83]], [[1, 2, 3]], [[1]]]))))
        v1 = []
        app1 = CUBOID([0.049, 0.035, 0.04])
        for j in range(1, 10):
            detr1 = T([1, 3])([0.049 * (j * 2 - 1), 1.6])(app1)
            v1.append(detr1)

        v2 = []
        app2 = CUBOID([0.046, 0.035, 0.04])
        for m in range(1, 6):
            app3 = T([1, 3])([0.049 * (m * 2 - 1), 1.625 + 0.0195 * (m * 2 - 1)])(app2)
            v2.append(app3)

        tetto_porta = STRUCT([app_tetto_porta, app_tetto_porta2, app_tetto_porta3, T([1, 2])([0.086, 0.08])(STRUCT(v1)),T([1, 2])([0.089, 0.08])(STRUCT(v2)),T([1, 2])([1.02, 0.115])(R([1, 2])(PI)(STRUCT(v2)))])
        struttura_porta_result = T(2)(-0.155)(STRUCT([fessura_porta, T([1, 2, 3])([0.035, 0.02, 1.25])(ornamento_porta),T([1, 2, 3])([0.975, 0.02, 1.25])(ornamento_porta), tetto_porta]))
        struttura_porta_result = COLOR(Color1)(struttura_porta_result)
        # VIEW(fessura_porta)
        # VIEW(ornamento_porta)
        # VIEW(tetto_porta)
        # VIEW(struttura_porta_result)
        return struttura_porta_result

    elif tipologia == 2:
        app_ornamento = DIFFERENCE([T([1, 2])([-0.04, -0.04])(CUBOID([0.38, 0.04, 0.83])), T(2)(-0.04)(CUBOID([0.3, 0.04, 0.75]))])
        app_ornamento_porta = T([1, 2, 3])([-0.04, -0.06, 0.83])(CUBOID([0.38, 0.06, 0.04]))
        fessura_porta = STRUCT([app_ornamento, app_ornamento_porta, T([2, 3])([-0.02, 0.04])(app_ornamento_porta)])

        app_tetto_porta = DIFFERENCE([T([2, 3])([0.06, 0.21])(R([1, 3])(-PI / 2)(MY_CYLINDER([0.06, 0.05])(16))),T(2)(0.09)(CUBOID([0.05, 0.1, 0.27]))])
        app_tetto_porta2 = T([2, 3])([0.07, 0.03])(R([1, 3])(-PI / 2)(MY_CYLINDER([0.03, 0.05])(16)))
        app_tetto_porta3 = OFFSET([0.05, 0, 0])(MKPOL([[[0, 0.09, 0.03], [0, 0.005, 0.19], [0, 0.045, 0.19]], [[1, 2, 3]], [[1]]]))

        ornamento_porta = T([2, 3])([-0.09, 0.64])(STRUCT([app_tetto_porta, app_tetto_porta2, app_tetto_porta3]))

        app_tetto_porta4 = OFFSET([0, 0.12, 0])(MKPOL([[[-0.12, -0.12, 0.91], [0.15, -0.12, 1.11], [0.42, -0.12, 0.91],[0.37, -0.12, 0.91], [0.15, -0.12, 1.08], [-0.07, -0.12, 0.91]],[[1, 2, 5, 6], [2, 3, 4, 5]], [[1]]]))
        app_tetto_porta6 = OFFSET([0, 0.09, 0])(MKPOL([[[-0.08, -0.09, 0.91], [-0.03, -0.09, 0.94], [0.37, -0.09, 0.94], [0.42, -0.09, 0.91]], [[1, 2, 3, 4]],[[1]]]))

        tetto_porta = STRUCT([app_tetto_porta4, app_tetto_porta6])
        struttura_porta_result2 = COLOR(Color1)(STRUCT([fessura_porta, T(1)(-0.09)(ornamento_porta), T(1)(0.34)(ornamento_porta), tetto_porta]))
        # VIEW(struttura_porta_result2)
        return struttura_porta_result2
def balcone_sporgenza_interna():
    colonna_cilindrica = MY_CYLINDER([0.015, 0.36])(16)
    colonna_quadrata = T([1, 2])([1.23, -0.036])(CUBOID([0.037, 0.036, 0.36]))
    app = R([1, 2])(PI / 20)(STRUCT([T([1, 2])([1.25, 0.035])(colonna_cilindrica), T([1, 2])([1.245, 0.105])(colonna_cilindrica), T([1, 2])([1.25, -0.035])(colonna_cilindrica),T([1, 2])([1.245, -0.105])(colonna_cilindrica), R([1, 2])(PI / 20)(colonna_quadrata), R([1, 2])(-PI / 20)(T(2)(0.036)(colonna_quadrata))]))
    #VIEW(app)
    sporgenza_app = STRUCT([app, R([1, 2])(PI / 10)(app), R([1, 2])(2 * PI / 10)(app), R([1, 2])(3 * PI / 10)(app),R([1, 2])(4 * PI / 10)(app)])
    #VIEW(sporgenza_app)
    sporgenza1 = STRUCT([sporgenza_app, R([1, 2])(PI / 2)(sporgenza_app), R([1, 2])(PI)(sporgenza_app), R([1, 2])(-PI / 2)(sporgenza_app),T(3)(0.36)(DIFFERENCE([MY_CYLINDER([1.3, 0.04])(32), MY_CYLINDER([1.21, 0.04])(32)]))])
    sporgenza_result=COLOR(Color1)(sporgenza1)
    #VIEW(sporgenza_result)
    return sporgenza_result
def porte_e_finestre(distanze_x, distanze_y, distanze_z, matrice, tipologia):
    # la tipologia indica se porta o finestra

    app = []
    x = 0
    for l in range(0, len(matrice)):
        # su tutte le x
        y = 0
        for w in range(0, len(matrice[l])):
            # su tutte le y
            z = 0
            for h in range(0, len(matrice[l][w])):
                # su tutte le z
                if (w > 0) and (w < len(matrice[l]) - 1):
                    if ((matrice[l][w][h] is True) and (matrice[l][w - 1][h] is False) and (
                        matrice[l][w + 1][h] is False)):
                        if (tipologia == "finestra2"):
                            app.append(hex_material("#71b2cf", "#71b2cf", .85)(T([1, 2, 3])([x, y, z])(CUBOID([distanze_x[l], distanze_y[w], distanze_z[h]]))))
                        elif tipologia == "porta":
                            app.append(TEXTURE("wood2.png")(T([1, 2, 3])([x, y, z])(CUBOID([distanze_x[l], distanze_y[w], distanze_z[h]]))))
                    elif (matrice[l][w][h]):
                        app.append(TEXTURE("wood2.png")(T([1, 2, 3])([x, y, z])(CUBOID([distanze_x[l], distanze_y[w], distanze_z[h]]))))
                elif (matrice[l][w][h]):
                    app.append(TEXTURE("wood2.png")(T([1, 2, 3])([x, y, z])(CUBOID([distanze_x[l], distanze_y[w], distanze_z[h]]))))

                z += distanze_z[h]
            y += distanze_y[w]
        x += distanze_x[l]
    result = STRUCT(app)
    # VIEW(result)
    return result
def porta(tipologia):
    # tipologia == 1 porta esterna primo piano
    # tipologia == 2 porta esterna piano terra
    # tipologia == 3 porta interna primo piano
    # tipologia == 4 porta interna pinao terra e secondo


    if tipologia == 1:
        x = [0.04, 0.24, 0.04, 0.24, 0.04]
        y = [0.02, 0.06, 0.02]
        z = [0.04, 0.45, 0.04, 0.45, 0.08, 0.3, 0.04]
        bool = [[[True, True, True, True, True, True, True], [True, True, True, True, True, True, True],[True, True, True, True, True, True, True]],[[True, False, True, False, True, False, True], [True, True, True, True, True, True, True],[True, False, True, False, True, False, True]],[[True, True, True, True, True, True, True], [True, True, True, True, True, True, True],[True, True, True, True, True, True, True]],[[True, False, True, False, True, False, True], [True, True, True, True, True, True, True],[True, False, True, False, True, False, True]],[[True, True, True, True, True, True, True], [True, True, True, True, True, True, True],[True, True, True, True, True, True, True]]]
        porta_result1 = porte_e_finestre(x, y, z, bool, "porta")
        # VIEW(porta_result1)
        return porta_result1

    elif tipologia == 2:
        x = [0.05, 0.225, 0.05, 0.225, 0.05]
        y = [0.02, 0.06, 0.02]
        z = [0.05, 0.375, 0.05, 0.375, 0.05]
        bool = [[[True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True]],[[True, False, True, False, True], [True, True, True, True, True], [True, False, True, False, True]],[[True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True]], [[True, False, True, False, True], [True, True, True, True, True], [True, False, True, False, True]],[[True, True, True, True, True], [True, True, True, True, True], [True, True, True, True, True]]]
        porta_result2 = porte_e_finestre(x, y, z, bool, "porta")
        # VIEW(porta_result2)
        return porta_result2

    elif tipologia == 3:

        x = [0.05, 0.3, 0.05]
        y = [0.02, 0.06, 0.02]
        z = [0.95, 0.05]
        bool = [[[True, True], [True, True], [True, True]], [[False, True], [True, True], [False, True]],[[True, True], [True, True], [True, True]]]
        porta_result3 = porte_e_finestre(x, y, z, bool, "porta")
        # VIEW(porta_result3)
        return porta_result3

    elif tipologia == 4:
        x = [0.03, 0.24, 0.03]
        y = [0.02, 0.04, 0.02]
        z = [0.72, 0.03]
        bool = [[[True, True], [True, True], [True, True]], [[False, True], [True, True], [False, True]],[[True, True], [True, True], [True, True]]]
        porta_result4 = porte_e_finestre(x, y, z, bool, "porta")
        # VIEW(porta_result4)
        return porta_result4

    else:
        x = [0.05, 0.35, 0.05]
        y = [0.02, 0.06, 0.02]
        z = [0.95, 0.05]
        bool = [[[True, True], [True, True], [True, True]], [[False, True], [True, True], [False, True]],[[True, True], [True, True], [True, True]]]
        porta_result5 = porte_e_finestre(x, y, z, bool, "porta")
        # VIEW(porta_result5)
        return porta_result5



#############
##Ingresso###
#############

def scalinata_ingresso():
    app = COLOR(Color4)(CUBOID([0.1079, 3.4, 0.055]))
    scalinata = []
    for i in range(1, 20):
        gradino = T([1, 3])([2.05 - (0.1079 * i), 0.055 * (i - 1)])(app)
        scalinata.append(gradino)
    scale_result=STRUCT(scalinata)
    #VIEW(scale_result)
    return scale_result
def parete_laterale():

    # Ingresso

    cubetto = CUBOID([1.6, 0.25, 0.95])
    cubetto2 = T(1)(1.6)(CUBOID([2.05, 0.25, 0.95]))
    app_scalinata1 = DIFFERENCE([STRUCT([T(2)(-0.06)(CUBOID([3.71, 0.37, 0.3])), T(2)(-0.03)(CUBOID([3.68, 0.31, 0.5]))]), cubetto])
    app_scalinata2 = COLOR(Color4)(DIFFERENCE([T(1)(1.6)(STRUCT([T(2)(-0.06)(CUBOID([2.11, 0.37, 0.3])),T(2)(-0.03)(CUBOID([2.08, 0.31, 0.5]))])), cubetto2]))
    #VIEW(app_scalinata2)
    muro_Scaletta = STRUCT([cubetto, T(2)(3.65)(cubetto), T([1,2])([1.3,0.25])(CUBOID([0.15,3.4,0.95]))])
    muro_scaletta2 = STRUCT([cubetto2, T(2)(3.65)(cubetto2)])
    pre_scalinata =  COLOR(Color1)(T([2,3])([-0.06,0.95])(CUBOID([1.6,4.02,0.15])))
    #VIEW(muro_Scaletta)
    #VIEW(muro_scaletta2)
    #VIEW(pre_scalinata)
    d1 = STRUCT([T(2)(-0.1)(CUBOID([0.8,0.5,0.65])), DIFFERENCE([T([1,2,3])([0.4,0.31,-0.095])(R([2,3])(PI/2)(MY_CYLINDER([0.85,0.31])(32))),T([1,3])([-0.7,-1.3])(CUBOID([2,0.31,1.95]))])])
    cubetto3 = T([1,3])([1.6,0.575])(CUBOID([0.4,0.25,0.3]))
    app_muro_porta = STRUCT([T([1,2])([0.25,-0.06])(d1), T([1,2])([0.25,3.65])(d1), T([1,2])([1.3,1.65])(CUBOID([0.15,0.6,0.9]))])
    app_muro_porta2 = STRUCT([T([1, 2])([0.25, -0.06])(d1), T([1, 2])([0.25, 3.65])(d1)])
    dj = COLOR(Color1)(DIFFERENCE([STRUCT([app_scalinata1, T(2)(3.65)(app_scalinata1)]),app_muro_porta]))
    dp = DIFFERENCE([muro_Scaletta,app_muro_porta])
    dp2 = DIFFERENCE([muro_Scaletta, app_muro_porta2])
    pre_scalinata2 = COLOR(Color1)(DIFFERENCE([pre_scalinata,app_muro_porta]))
    holew12 = STRUCT([cubetto3, T(2)(3.65)(cubetto3)])
    #VIEW(dp)
    #VIEW(muro_Scaletta)
    #VIEW(app_muro_porta)
    #VIEW(app_muro_porta2)
    #VIEW(holew12)
    scorrimano = COLOR(Color4)(T([1,3])([1.6,0.95])(CUBOID([2.11,0.37,0.15])))
    scalinata_result = STRUCT([T([1,2])([1.6,0.25])(scalinata_ingresso()), COLOR(Color5)(DIFFERENCE([muro_scaletta2, holew12])),T(2)(-0.06)(scorrimano), T(2)(3.59)(scorrimano), app_scalinata2, T(2)(3.65)(app_scalinata2)])
    finestrella = T([1,2, 3])([1.6,0.02,0.575])(finestra2(3))
    finestrelle_con_porta = STRUCT([finestrella, T(2)(3.81)(finestrella), T([1,2])([1.32,2.25])(R([1,2])(-PI/2)(porta(2)))])
    finestrelle = STRUCT([finestrella, T(2)(3.81)(finestrella)])
    piano = COLOR(Color4)(T([1,2,3])([1.3,-0.06,-0.01])(CUBOID([2.41,4.02,0.03])))
    #VIEW(scalinata_result)
    #VIEW(finestrella)
    #VIEW(finestrelle)
    #finalGroundFloor = STRUCT([dj,dp,pre_scalinata2, scalinata_result, finestrelle_con_porta, piano])
    finalGroundFloor = STRUCT([dj,dp2,pre_scalinata2, scalinata_result, finestrelle, piano])
    #VIEW(finalGroundFloor)

    # Primo piano

    cubetto21 = T(3)(1.1)(CUBOID([1.27, 0.25, 1.9]))

    app_muro_finestra = STRUCT([CUBOID([0.8, 0.25, 1.25]), T([1, 3])([0.4, 1.25])(R([2, 3])(-PI / 2)(MY_CYLINDER([0.4, 0.25])(32)))])
    muri_con_fessure = DIFFERENCE([STRUCT([cubetto21,T(2)(3.65)(cubetto21)]), T([1,3])([0.25,1.1])(app_muro_finestra),T([1,2,3])([0.25,3.65,1.1])(app_muro_finestra)])
    elemento_fin =  COLOR(Color1)(OFFSET([0, 0.035, 0])(MKPOL([[[0.45, -0.035, 3], [0.85, -0.035, 3], [0.7, -0.035, 2.74],[0.6, -0.035, 2.74]],[[1, 2, 3, 4]], [[1]]])))
    elemento = T([1,2,3])([-0.03,-0.03, 2.2])(CUBOID([0.31,0.31,0.15]))
    elementi = COLOR(Color1)(STRUCT([elemento, T(2)(3.65)(elemento),T(1)(1.03)(elemento),T([1,2])([1.03,3.65])(elemento)]))
    elemento2 = T([1, 3])([0.25, 1.1])(CUBOID([0.8, 0.1, 0.35]))
    elemento3 = COLOR(Color1)(T([2,3])([-0.03, 1.1])(CUBOID([1.27,0.03,0.15])))
    elementi_finali = STRUCT([elemento2, T(2)(3.8)(elemento2), elemento3, T(2)(3.93)(elemento3), elemento_fin,T(2)(3.935)(elemento_fin), elementi])
    #VIEW(muri_con_fessure)
    #VIEW(elementi_finali)

    colonna = MY_CYLINDER([0.1,1.75])(32)
    base_colonna = MY_CYLINDER([0.14, 0.07])(32)
    colonna2 = R([1,3])(-PI/2)(MY_CYLINDER([0.05,0.25])(16))
    colonna3 = STRUCT([T([1,2,3])([1.32,0,2.954])(colonna2),T([1,2,3])([1.32,0.2,2.954])(colonna2)])
    colonne = []
    #VIEW(colonna)
    #VIEW(base_colonna)
    for i in range (1,7):
        base = COLOR(Color1)(T([1,2,3])([1.3,0.72*(i-1),1.1])(CUBOID([0.3,0.3,0.15])))
        col = T([1,2,3])([1.45,0.15+0.72*(i-1),1.25])(colonna)
        det01 = T([1,2,3])([1.45,0.15+0.72*(i-1),1.25])(base_colonna)
        det02 = T(2)(0.05+0.72*(i-1))(colonna3)
        column = STRUCT([base,col,det01, T(3)(1.68)(det01), det02])
        colonne.append(column)

    app_per_fessura_tetto = OFFSET([0,3.4])(T([1,2,3])([0.65,0.25,-0.558])(R([2,3])(-PI/2)(MY_CYLINDER([0.85,0.06])(64))))
    pre_scalinata = COLOR(Color1)(DIFFERENCE([STRUCT([T(2)(-0.03)(CUBOID([1.63,3.96,0.15])),T([2,3])([-0.06,0.15])(CUBOID([1.66,4.02,0.15]))]), app_per_fessura_tetto]))
    facciata_primopiano = STRUCT([muri_con_fessure, elementi_finali, STRUCT(colonne), T(3)(3)(pre_scalinata)])
    #VIEW(facciata_primopiano)

    # Secondo Piano


    elem1 = DIFFERENCE([T(2)(-0.035)(CUBOID([1.635,3.97,0.17])), CUBOID([1.6,3.9,0.3])])
    elem2 = COLOR(Color1)(DIFFERENCE([T([2,3])([-0.065,0.17])(CUBOID([1.665,4.03,0.05])), CUBOID([1.6,3.9,0.3])]))
    elem3 = STRUCT([elem1,elem2])
    app_buco = R([1,3])(-PI/2)(MY_CYLINDER([0.1,0.15])(16))
    app_buco2 = STRUCT([T([1,2,3])([1.45,1.22,0.45])(app_buco), T([1,2,3])([1.45,2.68,0.45])(app_buco)])
    triangolo_tetto = OFFSET([0.15,0,0])(MKPOL([[[1.45,0,0.22],[1.45,3.9,0.22],[1.45,1.95,0.95]],[[1,2,3]],[[1]]]))
    app_tetto1 = OFFSET([1.665,0,0])(MKPOL([[[0, -0.094, 0.22],[0,-0.065, 0.17],[0, 1.95, 0.95],[0, 1.95, 1]],[[1, 2, 3, 4]], [[1]]]))
    app_tetto2 = OFFSET([1.7,0,0])(MKPOL([[[0, -0.14, 0.3],[0,-0.094, 0.22],[0, 1.95, 1],[0, 1.95, 1.08]],[[1, 2, 3, 4]], [[1]]]))
    app_tetto3 = TEXTURE("tegole4.png")(OFFSET([1.72, 0, 0])(MKPOL([[[0, -0.2015, 0.28], [0, -0.19, 0.26], [0, 1.95, 1.08], [0, 1.95, 1.1]], [[1, 2, 3, 4]], [[1]]])))
    tetto1 = COLOR(Color1)(STRUCT([app_tetto1, T([1, 2])([1.665, 3.9])(R([1, 2])(PI)(app_tetto1))]))
    tetto2 = STRUCT([app_tetto2, T([1, 2])([1.7, 3.9])(R([1, 2])(PI)(app_tetto2))])
    tetto3 = STRUCT([app_tetto3, T([1, 2])([1.72, 3.9])(R([1, 2])(PI)(app_tetto3))])
    vtetto = []
    app_vtetto = CUBOID([0.061,0.03,0.061])
    #VIEW(elem3)
    #VIEW(triangolo_tetto)
    #VIEW(tetto1)
    #VIEW(tetto2)
    #VIEW(tetto3)
    #VIEW(app_vtetto)
    for j in range(1,14):
        app_vtetto1 = T([1,2,3])([0.061*(j*2-1),-0.065,0.109])(app_vtetto)
        vtetto.append(app_vtetto1)
    vtetto2 = []
    elemento2 = CUBOID([0.03,0.061,0.061])
    for k in range(1,33):
        app_vtetto2 = T([1, 2, 3])([1.635, 0.061 * (k * 2 - 1), 0.109])(elemento2)
        vtetto2.append(app_vtetto2)
    vtetto3 =[]
    for scorrimano in range(1,17):
        app_vtetto3 = T([1,2,3])([1.6, 0.061*(scorrimano*2-1),0.0235*(scorrimano*2-1)])(elemento2)
        vtetto3.append(app_vtetto3)
    cub_tetto = T(3)(0.16)(STRUCT(vtetto3))

    colonnine_tetto = STRUCT([T([1,2,3])([1.35,0.05,0.33])(CUBOID([0.2,0.2,0.15])), TEXTURE("tegole4.png")(T([1,2,3])([1.32,0.02,0.48])(CUBOID([0.26,0.26,0.05])))])
    finestrela_tonda = R([1, 3])(-PI / 2)(STRUCT([TEXTURE("wood2.png")(DIFFERENCE([MY_CYLINDER([0.1, 0.07])(16), MY_CYLINDER([0.075, 0.07])(16)])),hex_material("#71b2cf", "#71b2cf", .85)(T(3)(0.03)(MY_CYLINDER([0.075, 0.01])(16)))]))
    composizione_facciata_tetto = COLOR(Color1)(STRUCT([STRUCT(vtetto), T(2)(3.995)(STRUCT(vtetto)), T(2)(-0.0305)(STRUCT(vtetto2)),T([1,2])([3.23,3.9])(R([1,2])(PI)(cub_tetto)), cub_tetto,colonnine_tetto,T(2)(3.6)(colonnine_tetto), T([2,3])([1.8,0.66])(colonnine_tetto)]))
    tetto_result = STRUCT([elem3,DIFFERENCE([triangolo_tetto, app_buco2]), tetto1, tetto2, tetto3,composizione_facciata_tetto])

    facciata_finale = COLOR(Color2)(STRUCT([finalGroundFloor, facciata_primopiano, T(3)(3.3)(tetto_result)]))
    facciata_laterale_result=STRUCT([facciata_finale, T([1,2,3])([1.51,1.22,3.75])(finestrela_tonda), T([1,2,3])([1.51,2.68,3.75])(finestrela_tonda)])
    #VIEW(cub_tetto)
    #VIEW(colonnine_tetto)
    #VIEW(finestrela_tonda)
    #VIEW(composizione_facciata_tetto)
    #VIEW(tetto_result)
    #VIEW(facciata_finale)
    #VIEW(facciata_laterale_result)
    return facciata_laterale_result

####################
###Tetto e Cupola###
####################

def contorno_cupola(parametri):
    raggio_esterno1, raggio_interno1, raggio_interno2, altezza11, altezza12 = parametri
    def contorno_cupola2(parametri2):

        raggio_esterno2, raggio_interno22, altezza2 = parametri2
        elemento1 = T([1, 3])([raggio_interno1, 0.02])(CUBOID([0.08, 0.08, altezza11-0.02]))
        v1 = []
        for i in range(1, 6):
            app = R([1, 2])(PI / 10 * (i - 1))(elemento1)
            v1.append(app)
        elemento2 = STRUCT(v1)
        #VIEW(elemento2)
        elemento3 = STRUCT([elemento2, R([1, 2])(PI / 2)(elemento2), R([1, 2])(PI)(elemento2), R([1, 2])(-PI / 2)(elemento2)])
        #VIEW(elemento3)
        elemento4 = STRUCT([DIFFERENCE([MY_CYLINDER([raggio_esterno1,altezza11])(16), MY_CYLINDER([raggio_interno2,altezza11])(32)]),T(3)(altezza11)(DIFFERENCE([MY_CYLINDER([raggio_esterno1, altezza12])(16), MY_CYLINDER([raggio_interno1+0.01, altezza12])(32)]))])
        #VIEW(elemento4)
        result1 = STRUCT([elemento3, elemento4])
        #VIEW(result1)
        elemento21 = T(1)(raggio_interno22)(CUBOID([0.045, 0.08, 0.03]))
        v2 = []
        for i in range(1, 6):
            app = R([1, 2])(PI / 10 * (i - 1))(elemento21)
            v2.append(app)
        elemento22 = STRUCT(v2)
        elemento23 = STRUCT([elemento22, R([1, 2])(PI / 2)(elemento22), R([1, 2])(PI)(elemento22), R([1, 2])(-PI / 2)(elemento22)])
        elemento24 = T(3)(0.03)(DIFFERENCE([MY_CYLINDER([raggio_esterno1, altezza2])(16), MY_CYLINDER([raggio_interno22+0.01, altezza2])(32)]))
        result2 = STRUCT([elemento23, elemento24])
        result_finale= COLOR(Color1)(STRUCT([result1, T(3)(altezza11+altezza12)(result2)]))
        #VIEW(result_finale)
        return result_finale

    return contorno_cupola2
def HALFSPHERE(radius):

    def HALFSPHERE0(subds):
        N, M = subds
        domain = Hpc(Grid([N * [PI / N], M * [2 * PI / M]]))
        domain = MAT([[1, 0, 0, 0], [-PI / 2, 1, 0, 0], [-PI, 0, 1, 0], [0, 0, 0, 1]])(domain)
        fx = lambda p: radius * math.cos(p[0]) * math.sin(p[1])
        fy = lambda p: radius * math.cos(p[0]) * math.cos(p[1])
        fz = lambda p: radius * ABS(math.sin(p[0]))
        ret = GMAP([fx, fy, fz])(domain)
        return ret
    return HALFSPHERE0
def base_cupola(parametri):
    raggio_esterno,raggio_interno,altezza,tipo = parametri

    base = COLOR(Color2)(DIFFERENCE([MY_CYLINDER([raggio_esterno,altezza])(100),MY_CYLINDER([raggio_interno,altezza])(32)]))
    angolo = (3.14*(raggio_esterno+0.02))/20
    if(tipo==1):
        app2 = R([1, 2])(PI / 40)(TEXTURE("tegole1.png")(T(1)(raggio_esterno + 0.02)(R([1, 3])(PI / 12 * 4)(T([1, 2])([-0.005, -(angolo / 2)])(CUBOID([0.005, angolo, 0.25]))))))
    if(tipo ==2):
        app2 = R([1, 2])(PI / 40)(TEXTURE("tegole1.png")(T(1)(raggio_esterno+0.02)(R([1, 3])(PI / 14* 4)(T([1, 2])([-0.005, -(angolo/2)])(CUBOID([0.005, angolo, 0.25]))))))
    if(tipo==3):
        app2 = R([1, 2])(PI / 40)(TEXTURE("tegole1.png")(T(1)(raggio_esterno+0.02)(R([1, 3])(PI / 10 * 4)(T([1, 2])([-0.005, -(angolo/2)])(CUBOID([0.005, angolo, 0.25]))))))
    vettore = []
    for i in range(1, 11):
        app = R([1, 2])(PI / 20 * (i - 1))(app2)
        vettore.append(app)
    cupola1 = STRUCT(vettore)
    cupola2 = STRUCT([cupola1, R([1, 2])(PI / 2)(cupola1), R([1, 2])(PI)(cupola1), R([1, 2])(-PI / 2)(cupola1)])
    cupola_result=STRUCT([base, T(3)(altezza)(cupola2)])
    #VIEW(cupola1)
    #VIEW(cupola2)
    #VIEW(cupola_result)
    return cupola_result
def tetto():

    base_app = OFFSET([0,3.9,0])(T(3)(-0.12)(MKPOL([[[-0.03,-0.03,0],[-0.18,-0.18,0.12],[7.53,-0.18,0.12],[7.38,-0.03,0]],[[1,2,3,4]],[[1]]])))
    base = STRUCT([base_app, T([1,2])([7.35,7.35])(R([1,2])(PI)(base_app))])
    app_tri = OFFSET([0,0,0.04])(MKPOL([[[-0.2,-0.2,0],[3.675,3.675,1.65],[7.55,-0.2,0]],[[1,2,3]],[[1]]]))
    tetto1 = TEXTURE("tegole3.png")(DIFFERENCE([app_tri,T([1,2])([3.7,3.675])(MY_CYLINDER([1.71, 1.8])(64))]))
    tetto_bucato = STRUCT([tetto1,T(1)(7.35)(R([1,2])(PI/2)(tetto1)),T([1,2])([7.35,7.35])(R([1,2])(PI)(tetto1)),T(2)(7.35)(R([1,2])(-PI/2)(tetto1))])
    muro_tetto_centrale = DIFFERENCE([STRUCT([T([1,2])([3.7,3.675])(MY_CYLINDER([1.71, 1.2])(64)), base]),T([1,2,3])([3.7,3.675,-0.12])(MY_CYLINDER([1.61, 1.9])(64))])
    tetto_finale = COLOR(Color2)(STRUCT([tetto_bucato, muro_tetto_centrale]))
    cupola_affresco = T([1, 2])([3.7, 3.675])(TEXTURE("cupola.png")(HALFSPHERE(1.6)([32, 32])))
    #VIEW(tetto1)
    #VIEW(tetto_bucato)
    #VIEW(tetto_finale)
    #VIEW(cupola_affresco)

    anello1 = base_cupola([1.77, 1.61, 0.15, 1])
    anello2 = base_cupola([1.61, 1.52, 0.15, 3])
    anello3 = base_cupola([1.48, 1.45, 0.1, 2])
    anello4 = base_cupola([1.34, 1.32, 0.13, 2])
    anello5 = base_cupola([1.21, 1.19, 0.11, 1])
    anello6 = base_cupola([1.05, 1.02, 0.11, 1])
    anello7 = base_cupola([0.905, 0.87, 0.08, 3])
    anello8 = base_cupola([0.72, 0.7, 0.05, 3])
    anello9 = base_cupola([0.56, 0.5, 0.02, 3])
    #VIEW(anello1)
    #VIEW(anello2)
    #VIEW(anello3)
    #VIEW(anello4)
    #VIEW(anello5)
    #VIEW(anello6)
    #VIEW(anello7)
    #VIEW(anello8)
    #VIEW(anello9)
    app1_tetto = MKPOL([[[0.32, 0.137, 0], [0.32, -0.137, 0], [0.1, -0.0475, 0.16], [0.1, 0.0475, 0.16]], [[4, 3, 2, 1]], [[1]]])
    app2_tetto = MKPOL([[[0.15, 0.062, 0], [0.15, -0.062, 0], [0, 0, 0.08]], [[3, 2, 1]], [[1]]])
    app3_anello = STRUCT([contorno_cupola([1.63, 1.46, 1.56, 0.13, 0.07])([1.46, 1.42, 0.03]),R([1, 2])(PI / 20)(contorno_cupola([1.63, 1.46, 1.56, 0.13, 0.07])([1.46, 1.42, 0.03]))])
    app4_anello = R([1, 2])(PI / 15)(contorno_cupola([1.52, 1.37, 1.47, 0.13, 0.07])([1.37, 1.33, 0.03]))
    elemento_tetto1 = STRUCT([app1_tetto, R([1, 2])(PI / 4)(app1_tetto), R([1, 2])(PI / 2)(app1_tetto), R([1, 2])(PI / 4 * 3)(app1_tetto), R([1, 2])(PI)(app1_tetto),R([1, 2])(-PI / 4)(app1_tetto),R([1, 2])(-PI / 2)(app1_tetto), R([1, 2])(-PI / 4 * 3)(app1_tetto)])
    elemento_tetto2 = STRUCT([app2_tetto, R([1, 2])(PI / 4)(app2_tetto), R([1, 2])(PI / 2)(app2_tetto), R([1, 2])(PI / 4 * 3)(app2_tetto), R([1, 2])(PI)(app2_tetto),R([1, 2])(-PI / 4)(app2_tetto), R([1, 2])(-PI / 2)(app2_tetto), R([1, 2])(-PI / 4 * 3)(app2_tetto)])
    cupola1 = COLOR(Color2)(STRUCT([T(3)(1.099)(MY_CYLINDER([0.35, 0.03])(64)), T(3)(1.129)(MY_CYLINDER([0.37, 0.02])(64)), T(3)(1.149)(elemento_tetto1),T(3)(1.309)(MY_CYLINDER([0.1, 0.01])(64)), T(3)(1.319)(elemento_tetto2)]))
    cupola_finale = STRUCT([anello1,T(3)(0.15)(anello2), T(3)(0.3)(anello3), T(3)(0.41)(anello4), T(3)(0.56)(anello5), T(3)(0.67)(anello6),T(3)(0.805)(anello7), T(3)(0.909)(anello8), T(3)(1)(anello9), cupola1])
    anello_esterno = STRUCT([app3_anello, T(3)(0.25)(app4_anello)])


    #VIEW(elemento_tetto1)
    #VIEW(elemento_tetto2)
    #VIEW(cupola1)
    #VIEW(cupola_finale)
    #VIEW(app3_anello)
    #VIEW(anello_esterno)

    tetto_result=STRUCT([tetto_finale, T([1,2,3])([3.7,3.675,1.2])(cupola_finale), cupola_affresco, T([1, 2])([3.7,3.675])(anello_esterno)])
    #VIEW(tetto_result)
    return tetto_result


##########
##Esterno###
##########
def bottomArc(d):
    return BEZIER(S1)([[0, 0], [0, 2 * d / 3], [d, 2 * d / 3], [d, 0]])
def topArc(d):
    return BEZIER(S1)([[0, 2 * d / 3], [d, 2 * d / 3]])
def arc2D(d):
    return BEZIER(S2)([bottomArc(d), topArc(d)])
def arc3D(d):
    def arc3D1(w):
        arco = arc2D(2.9)
        dominio = PROD([INTERVALS(1)(8), INTERVALS(1)(1)])
        ar = MAP(arco)(dominio)
        domin = PROD([ar, QUOTE([0.1])])
        return COMP([T(2)(w), R([2, 3])(PI / 2)])(domin)

    return arc3D1
def arc3D2(d):
    def arc3D1(w):
        arco = arc2D(2.9)
        dominio = PROD([INTERVALS(1)(8), INTERVALS(1)(1)])
        ar = MAP(arco)(dominio)
        domin = PROD([ar, QUOTE([2])])
        return COMP([T(2)(w), R([2, 3])(PI / 2)])(domin)

    return arc3D1
def foglie():
    celement = T(3)(0.2)(R([1,2])(PI)(S(3)(2)(SPHERE(0.3)([8,8]))))
    sramo = (CYLINDER([0.1,0.8])(15))
    sram = STRUCT([sramo,S([1,2,3])([2.9,2.9,2.3])(celement)])
    sramo = T(1)(0.15)(R([1,3])(-1*PI/4)(sramo))
    sramo = STRUCT([sramo,T(1)(0.7)(S([1,2,3])([3,3,2])(celement))])
    for i in range(5):
        el = R([1,2])(i*2*PI/5)(sramo)
        sram = STRUCT([sram,el])
    sram = T(3)(2.5)(sram)
    random = randint(1,4)
    sram = TEXTURE("foglie.jpeg")(sram)
    return sram
def foglie2():
    celement = T(3)(0.2)(R([1,2])(PI)(S(3)(2)(SPHERE(0.3)([8,8]))))
    sramo = (CYLINDER([0.1,0.8])(15))
    sram = STRUCT([sramo,S([1,2,3])([2.9,2.9,2.3])(celement)])
    sramo = T(1)(0.15)(R([1,3])(-1*PI/4)(sramo))
    sramo = STRUCT([sramo,T(1)(0.7)(S([1,2,3])([3,3,2])(celement))])
    for i in range(5):
        el = R([1,2])(i*2*PI/5)(sramo)
        sram = STRUCT([sram,el])
    sram = T(3)(3)(sram)
    random = randint(1,4)
    sram = TEXTURE("foglie.jpeg")(sram)
    return sram
def tronco():
	return TEXTURE("tronco.jpeg")(CYLINDER([0.2,3])(40))
def tronco2():
	return TEXTURE("tronco.jpeg")(CYLINDER([0.4,3.5])(40))
def albero():
	return STRUCT([foglie(),tronco()])
def albero2():
	return STRUCT([foglie2(),tronco2()])
def recinsione():
    muri = fileReader2("recinsione.lines", 2)
    muri2=fileReader2("siepe.lines", 1)
    aiuola = TEXTURE("prato1.jpeg")(T([1, 2])([7, 15])(CUBOID([1.85, 3.8])))
    aiuola2 = T(1)(11.5)(aiuola)
    prato_sx = TEXTURE("prato1.jpeg")(T([1, 2])([1, 20.5])(CUBOID([2.5, 3.4])))
    prato_sx_app = TEXTURE("prato1.jpeg")(T([1, 2])([1, 20.5])(CUBOID([2.5, 3.4, 0.1])))
    prato_sx2 = TEXTURE("prato1.jpeg")(T([1, 2])([1, 25])(CUBOID([2.5, 2.5])))
    prato_sx2_app =TEXTURE("prato1.jpeg")( T([1, 2])([1, 25])(CUBOID([2.5, 2.5, 0.1])))
    prato_sx_grande = TEXTURE("prato1.jpeg")(T([1,2])([1,13])(CUBOID([2.5, 5.8])))
    prato_sx_grande_app = TEXTURE("prato1.jpeg")(T([1,2])([1,13])(CUBOID([2.5, 5.8, 0.1])))
    prato_grande = TEXTURE("prato1.jpeg")(T(1)(1)(CUBOID([19.35, 13])))
    prato_grande_app = TEXTURE("prato1.jpeg")(T(1)(1)(CUBOID([19.35, 13, 0.1])))
    viale1 = TEXTURE("ghiaia.jpeg")(T([1, 2])([10.9, 3.02])(CUBOID([1.2, 10, 0.1])))
    viale2 = TEXTURE("ghiaia.jpeg")(T(1)(4.1)(viale1))
    viale3 = TEXTURE("ghiaia.jpeg")(T(1)(12.1)(CUBOID([2.9, 3.1, 0.1])))
    k = TEXTURE("ghiaia.jpeg")(T([1, 2])([12.1, 5])(R([2, 3])(PI / 2)(arc3D(50)(0.1))))
    k2 = TEXTURE("ghiaia.jpeg")(T([1, 2])([12.1, 5])(R([2, 3])(PI / 2)(arc3D2(50)(0.1))))
    prato_grande_app2 = TEXTURE("prato1.jpeg")(DIFFERENCE([prato_grande_app, k2]))
    # prato_grande_app2=STRUCT([prato_grande_app2,k])
    # VIEW(prato_grande_app2)
    #prato_grande_app = COLOR([0.2, 0.4, 0.05])(DIFFERENCE([STRUCT([prato_grande_app, viale2, viale1, viale3]), STRUCT([viale1, viale2, k2, viale3])]))
    prato_grande_app = TEXTURE("prato1.jpeg")(
        DIFFERENCE([STRUCT([prato_grande_app, viale2, viale1, viale3]), STRUCT([viale1, viale2, k2, viale3])]))
    # VIEW(prato_grande_app)
    layer = TEXTURE("ghiaia.jpeg")(CUBOID([26, 30]))
    diff = TEXTURE("ghiaia.jpeg")(CUBOID([6, 2]))
    diff = TEXTURE("ghiaia.jpeg")(T(2)(28)(diff))
    diff2 = TEXTURE("ghiaia.jpeg")(CUBOID([12, 2]))
    diff2 = TEXTURE("ghiaia.jpeg")(T([1, 2])([17, 28])(diff2))
    diff3 = TEXTURE("ghiaia.jpeg")(CUBOID([5, 13]))
    diff3 = TEXTURE("ghiaia.jpeg")(T([1, 2])([22, 15])(diff3))
    viale1 = TEXTURE("ghiaia.jpeg")(T([1, 2])([10.9, 3.02])(CUBOID([1.2, 10])))
    viale2 = TEXTURE("ghiaia.jpeg")(T(1)(4.1)(viale1))
    a = STRUCT([layer, diff, diff2, diff3, aiuola, aiuola2, prato_sx, prato_sx2, prato_sx_grande, prato_grande, viale1,
                viale2])
    a = (DIFFERENCE([layer, STRUCT([diff, diff2, diff3, aiuola, aiuola2, prato_sx, prato_sx2, prato_sx_grande, prato_grande, viale1, viale2])]))
    aiuola_res = TEXTURE("prato1.jpeg")(T([1, 2])([7, 15])(CUBOID([1.85, 3.8, 0.04])))
    aiuola2_res = T(1)(11.5)(aiuola)
    per_aiuola = TEXTURE("fiori_text.jpeg")(T([1, 2])([7.1, 15.1])(CUBOID([1.5, 3.5, 0.2])))
    per_aiuola2 = T(1)(11.5)(per_aiuola)
    c = T([1, 2])([21, 1.2])(albero())
    c2 = T(1)(1)(c)
    c3 = T(1)(1)(c2)
    c4 = T(1)(1)(c3)
    c5 = T(1)(1)(c4)
    albero_app=STRUCT([c2,c3,c4])
    d1=T([1, 2])([1, 3.2])(albero())
    alberisx1=STRUCT([d1,T(1)(1)(d1),T(1)(2)(d1)])
    alberisx1=STRUCT([alberisx1,T(2)(1.3)(alberisx1),T(2)(2.6)(alberisx1),T(2)(3.9)(alberisx1),T(2)(5.2)(alberisx1)])
    alb1 = T([1, 2])([20.62, 1.2])(albero2())
    alb2 = T(1)(1)(alb1)
    alb3 = T(1)(1)(alb2)
    alb4 = T(1)(1)(alb3)
    alb5 = T(1)(1)(alb4)
    alb6=T(1)(1)(alb5)
    alberi=STRUCT([alb3,alb4,alb5,alb6])
    alberi=T(2)(15.15)(alberi)
    alberi_sx=STRUCT([alberi,T(2)(0.9)(alberi),T(2)(1.8)(alberi),T(2)(2.7)(alberi),T(2)(3.6)(alberi),T(2)(4.5)(alberi),T(2)(5.4)(alberi),T(2)(6.3)(alberi),T(2)(7.2)(alberi),T(2)(8.1)(alberi),T(2)(9)(alberi),T(2)(9.9)(alberi),T(2)(10.8)(alberi),T(2)(11.7)(alberi),T(2)(12.6)(alberi),T(2)(13.5)(alberi),T(2)(14.4)(alberi),T(2)(15.3)(alberi),T([1,2])([-4,12.6])(alberi),T([1,2])([-4,13.5])(alberi),T([1,2])([-4,14.4])(alberi),T([1,2])([-4,15.3])(alberi)])
    albdx1=albero2()
    albdx2 = T(1)(1)(albdx1)
    albdx3 = T(1)(1)(albdx2)
    albdx4 = T(1)(1)(albdx3)
    albdx5 = T(1)(1)(albdx4)
    albdx6 = T(1)(1)(albdx5)
    alb_ext=T(2)(31.6)(STRUCT([albdx1,albdx2]))
    alb_ext2=(alb_ext)
    for i in range(35):
        alb_ext2=STRUCT([alb_ext2,T(2)(-i*0.9)(alb_ext)])
    alb_ext2=T(1)(26.7)(alb_ext2)
    alberiext_sx=albero2()
    alberiext_sx=T([1,2])([0.6,17])(STRUCT([alberiext_sx,T(2)(1)(alberiext_sx)]))
    alberi_dx_app=T([1,2])([0.5,29])(STRUCT([albdx1,albdx2,albdx3,albdx4,albdx5,albdx6]))
    alb_app = STRUCT([T(2)(1.8)(alberi_dx_app), T(2)(2.7)(alberi_dx_app)])
    alberi_dx=STRUCT([alberi_dx_app,T(2)(0.9)(alberi_dx_app),T(2)(1.8)(alberi_dx_app),T(2)(2.7)(alberi_dx_app),T(1)(4)(alb_app),T(1)(8)(alb_app),T(1)(12)(alb_app)])
    terreno=TEXTURE("prato1.jpeg")(T([1,3])([-4,-0.51])(CUBOID([32.1,32.1,0.5])))
    a = STRUCT([TEXTURE("ghiaia.jpeg")(a), TEXTURE("muro1.jpeg")(muri),TEXTURE("siepe.jpg")(muri2), aiuola_res, aiuola2_res, prato_sx_app, prato_sx2_app, prato_sx_grande_app, prato_grande_app, viale1,viale2, k, viale3,per_aiuola2,per_aiuola,albero_app,c,alberisx1,terreno,alberi_sx,alberi_dx,alb_ext2,alberiext_sx])

    #VIEW(a)
    return a




############
###Villa####
############



def Villa_Finale(parametri):
    x,y,z = parametri
    pianoterra = piano_terra()
    piano1 = piano_primo()
    piano2 = piano_secondo()
    tetto1 = tetto()
    #VIEW(pianoterra)
    #VIEW(piano1)
    #VIEW(piano2)
    #VIEW(tetto1)
    edificio = T([1,2])([3.65,3.65])(STRUCT([pianoterra, T(3)(1.1)(piano1), T(3)(3.3)(piano2), T([1, 2, 3])([3.7,3.675,3.3])(balcone_sporgenza_interna()), T(3)(4.4)(tetto1)]))
    ingressi = parete_laterale()
    #VIEW(edificio)
    ingressi_app = STRUCT([T([1,2])([11,5.38])(ingressi), T([1,2])([9.28,11])(R([1,2])(PI/2)(ingressi)),T([1,2])([3.65,9.28])(R([1,2])(PI)(ingressi)), T([1,2])([5.38,3.65])(R([1,2])(-PI/2)(ingressi))])

    recins=recinsione()
    villa_result = STRUCT([edificio, ingressi_app])
    villa_app= T([1,2])([6.1,15])(villa_result)
    villa_app2=STRUCT([villa_app,recins])
    return S([1, 2, 3])([double(x/20), double(y/20), double(z/8.5)])(villa_app2)



VIEW(Villa_Finale([20, 20, 8.5]))







