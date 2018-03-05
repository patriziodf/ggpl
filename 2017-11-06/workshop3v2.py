from pyplasm import *
from larlib import *

def torretta(raggio_esterno, raggio_interno, altezza, numero_muri):


    def torre2(h1, h2, distanza1, distanza2):

        torre = (DIFFERENCE([MY_CYLINDER([raggio_esterno, altezza])(numero_muri), MY_CYLINDER([raggio_interno, altezza])(16)]))
        cilindro_reggente = (STRUCT([T(3)(h1)(DIFFERENCE([MY_CYLINDER([raggio_esterno + distanza2, h2])(16), MY_CYLINDER([raggio_interno, h2])(16)])),
                                               DIFFERENCE([MY_CYLINDER([raggio_esterno + distanza1, h1])(16), MY_CYLINDER([raggio_interno, h1])(16)])]))
        corona = (DIFFERENCE([MY_CYLINDER([raggio_esterno + distanza1, h1])(16), MY_CYLINDER([raggio_esterno, h1])(16)]))
        colonna = COLOR([0.8784,1,1])(T([1, 2])([double((-raggio_esterno * 3) / 2), -0.15])(CUBOID([raggio_esterno * 3, 0.3, altezza - distanza1])))
        colonne = COLOR([0.8784,1,1])(STRUCT([colonna, R([1, 2])(PI / 6)(colonna), R([1, 2])(PI / 3)(colonna), R([1, 2])(-PI / 6)(colonna),
                          R([1, 2])(-PI / 3)(colonna)]))
        colonne_reggenti = (T(3)(h1)(INTERSECTION(
            [DIFFERENCE([MY_CYLINDER([raggio_esterno + distanza1, altezza - h1])(16), MY_CYLINDER([raggio_esterno, altezza - h1])(16)]), colonne])))

        return STRUCT([torre, T(3)(altezza)(cilindro_reggente), corona, colonne_reggenti])
    return torre2
def torremedia1(raggio_esterno, raggio_interno, altezza):

    def torreme1(altezza_parte1, altezza_parte2, distanza1, distanza2):

        torre = DIFFERENCE([MY_CYLINDER([raggio_esterno, altezza])(16), MY_CYLINDER([raggio_interno, altezza])(16)])
        elemento1 = STRUCT([T(3)(altezza_parte1)(DIFFERENCE([MY_CYLINDER([raggio_esterno + distanza2, altezza_parte2])(16), MY_CYLINDER([raggio_interno, altezza_parte2])(16)])),
                          DIFFERENCE([MY_CYLINDER([raggio_esterno + distanza1, altezza_parte1])(16), MY_CYLINDER([raggio_interno, altezza_parte1])(16)])])

        elemento2 = DIFFERENCE([MY_CYLINDER([raggio_esterno + distanza1, altezza_parte1])(16), MY_CYLINDER([raggio_esterno, altezza_parte1])(16)])
        colonna = T([1, 2])([double((-raggio_esterno * 3) / 2), -0.15])(CUBOID([raggio_esterno * 3, 0.3, altezza - distanza1]))
        colonne = STRUCT([colonna, R([1, 2])(PI / 3)(colonna), R([1, 2])(PI / 3)(colonna), R([1, 2])(-PI / 3)(colonna),
                          R([1, 2])(2*PI/3)(colonna), R([1, 2])(-2*PI/3)(colonna), R([1, 2])(PI)(colonna)])
        elemento3 = T(3)(altezza_parte1)(INTERSECTION([DIFFERENCE([MY_CYLINDER([raggio_esterno + double(distanza1 / 2), altezza - altezza_parte1])(16),MY_CYLINDER([raggio_esterno, altezza - altezza_parte1])(16)]), colonne]))
        finestra = MY_CYLINDER([0.225, 4])(16)
        finestre = STRUCT([R([1, 2])(PI/6)(T([1, 3])([2, 0.65])(R([1, 3])(PI/2)(finestra))),
                          R([1, 2])(-PI / 6)(T([1, 3])([2, 0.65])(R([1, 3])(PI / 2)(finestra))),
                          R([1, 2])(PI / 2)(T([1, 3])([2, 0.65])(R([1, 3])(PI / 2)(finestra)))])
        torre_result = STRUCT([torre, T(3)(altezza)(elemento1), elemento2, elemento3])
        return DIFFERENCE([torre_result, finestre])
    return torreme1
def torremedia2(raggio_esterno, raggio_interno, altezza):

    def torreme2(altezza_elemento1, altezza_elemento2, distanza1, distanza2):

        torre = DIFFERENCE([MY_CYLINDER([raggio_esterno, altezza])(8), MY_CYLINDER([raggio_interno, altezza])(16)])
        elemento1 = STRUCT([T(3)(altezza_elemento1)(DIFFERENCE([MY_CYLINDER([raggio_esterno + distanza2, altezza_elemento2])(16), MY_CYLINDER([raggio_interno, altezza_elemento2])(16)])),
                          DIFFERENCE([MY_CYLINDER([raggio_esterno + distanza1, altezza_elemento1])(16), MY_CYLINDER([raggio_interno, altezza_elemento1])(16)])])

        elemento2 = DIFFERENCE([MY_CYLINDER([raggio_esterno + distanza1, altezza_elemento1])(16), MY_CYLINDER([raggio_esterno, altezza_elemento1])(8)])
        colonna = T([1, 2])([double((-raggio_esterno * 3) / 2), -0.15])(CUBOID([raggio_esterno * 3, 0.3, altezza - distanza1]))
        colonne = STRUCT([colonna, R([1, 2])(PI/4)(colonna), R([1, 2])(-PI/4)(colonna), R([1, 2])(PI/2)(colonna)])
        elemento3 = T(3)(altezza_elemento1)(INTERSECTION([DIFFERENCE([MY_CYLINDER([raggio_esterno + double(distanza1 / 2), altezza - altezza_elemento1])(16),
                                                                    MY_CYLINDER([raggio_esterno, altezza - altezza_elemento1])(16)]), colonne]))
        finestra = MY_CYLINDER([0.225, 4])(16)
        finestre = T(3)(double(altezza / 2))(STRUCT([R([1, 2])(PI / 8)(T(1)(2)(R([1, 3])(PI / 2)(finestra))),
                                                    R([1, 2])(-PI/8)(T(1)(2)(R([1, 3])(PI/2)(finestra))),
                                                    R([1, 2])(3*PI/8)(T(1)(2)(R([1, 3])(PI / 2)(finestra))),
                                                    R([1, 2])(-3*PI/8)(T(1)(2)(R([1, 3])(PI / 2)(finestra)))]))

        torre_result = STRUCT([torre, T(3)(altezza)(elemento1), elemento2, elemento3])
        return DIFFERENCE([torre_result, finestre])
    return torreme2
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
def QUARTERSPHERE (radius):

	def QUARTERSPHERE0 (subds):
		N , M = subds
		domain = Hpc(Grid([N*[PI/(2*N)],M*[PI/M]]))
		domain = MAT([[1,0,0,0],[-PI/2,1,0,0],[-PI,0,1,0],[0,0,0,1]])(domain)
		fx  = lambda p: radius * math.cos(p[0]) * math.sin  (p[1])
		fy  = lambda p: radius * math.cos(p[0]) * math.cos (p[1])
		fz  = lambda p: radius * ABS(sin(p[0]))
		ret=  GMAP([fx, fy, fz])(domain)
		return ret
	return QUARTERSPHERE0
def torregrande(raggio_esterno, raggio_interno, altezza):

    def torreg(altezza_elemento1, altezza_elemento2, distanza1, distanza2):

        torre = DIFFERENCE([MY_CYLINDER([raggio_esterno, altezza])(16), MY_CYLINDER([raggio_interno, altezza])(16)])
        elemento1 = STRUCT([T(3)(altezza_elemento1)(DIFFERENCE([MY_CYLINDER([raggio_esterno + distanza2, altezza_elemento2])(16), MY_CYLINDER([raggio_interno, altezza_elemento2])(16)])),
                          DIFFERENCE([MY_CYLINDER([raggio_esterno + distanza1, altezza_elemento1])(16), MY_CYLINDER([raggio_interno, altezza_elemento1])(16)])])

        elemento2 = STRUCT([T(3)(altezza_elemento2)(DIFFERENCE([MY_CYLINDER([raggio_esterno + distanza1, altezza_elemento1])(16), MY_CYLINDER([raggio_esterno, altezza_elemento1])(16)])),
                          DIFFERENCE([MY_CYLINDER([raggio_esterno + distanza2, altezza_elemento2])(16), MY_CYLINDER([raggio_interno, altezza_elemento2])(16)])])
        colonna = T([1, 2])([double((-raggio_esterno * 3) / 2), -0.2])(CUBOID([raggio_esterno * 3, 0.4, altezza - distanza1]))
        colonne = STRUCT([R([1, 2])(PI/6)(colonna), R([1, 2])(-PI/6)(colonna), R([1, 2])(PI/3)(colonna), R([1, 2])(-PI/3)(colonna)])
        elemento3 = T(3)(altezza_elemento1)(INTERSECTION([DIFFERENCE([MY_CYLINDER([raggio_esterno + double(distanza1 / 2) + 0.05, altezza - altezza_elemento1])(16),
                                                                    MY_CYLINDER([raggio_esterno, altezza - altezza_elemento1])(16)]), colonne]))
        buco = STRUCT([T([1, 3])([0.15, 0.1])(CUBOID([0.1, 0.6, 0.4])), T([1, 3])([0.35, 0.1])(CUBOID([0.1, 0.6, 0.4])),
                          T([2, 3])([0.15, 0.1])(CUBOID([0.6, 0.1, 0.4])), T([2, 3])([0.35, 0.1])(CUBOID([0.6, 0.1, 0.4]))])
        elemento_app = DIFFERENCE([CUBOID([0.6, 0.6, 0.6]), buco])
        finestra1 = MY_CYLINDER([0.56, 8])(16)
        finestra2 = MY_CYLINDER([0.3, 8])(16)
        finestre = T(3)(double(altezza / 2) + altezza_elemento1 + altezza_elemento2)(STRUCT([T(1)(4)(R([1, 3])(PI / 2)(finestra1)),
                                                                                            R([1, 2])(PI/4)(T(1)(4)(R([1, 3])(PI/2)(finestra2))),
                                                                                            R([1, 2])(-PI/4)(T(1)(4)(R([1, 3])(PI/2)(finestra2))),
                                                                                            R([1, 2])(PI/2)(T(1)(4)(R([1, 3])(PI/2)(finestra1)))]))

        finalTower = STRUCT([torre, T(3)(altezza)(elemento1), elemento2, elemento3])
        return DIFFERENCE([finalTower, finestre])
    return torreg
def muro():
    muro1 = CUBOID([12.4, 0.2, 6.8])
    elemento1 = STRUCT([T([1, 2, 3])([-0.25, -0.25, 4.45])(CUBOID([12.9, 0.25, 0.3])), T([1, 2])([-0.15, -0.15])
                    (CUBOID([12.7, 0.15, 0.5]))])
    colonna = STRUCT([T([1, 2])([-0.2, -0.2])(CUBOID([0.5, 0.2, 6.3])), T([1, 2])([1.9, -0.2])(CUBOID([0.5, 0.2, 6.3])),T([1, 2])([4, -0.2])(CUBOID([0.5, 0.2, 6.3])), T([1, 2])([7.9, -0.2])(CUBOID([0.5, 0.2, 6.3])),T([1, 2])([10, -0.2])(CUBOID([0.5, 0.2, 6.3])), T([1, 2])([12.1, -0.2])(CUBOID([0.5, 0.2, 6.3]))])
    murointerno = OFFSET([0.05, 0.05, 0.05])(STRUCT(MKPOLS([[[3.3, 2.9, 0], [3.7, 3.3, 0], [4, 3, 0], [5.85, 3, 0], [5.85, 2.4, 0], [6.5, 2.4, 0],[6.5, 3, 0], [8.5, 3, 0],[8.65, 3.2, 0], [9.008, 2.85, 0], [3.3, 2.9, 6.5], [3.7, 3.3, 6.5], [4, 3, 6.5], [5.85, 3, 2],[5.85, 2.4, 2], [6.5, 2.4, 2], [6.5, 3, 2], [8.5, 3, 6.5], [8.65, 3.2, 6.5], [9.008, 2.85, 6.5], [5.85, 3, 6.5],[6.5, 3, 6.5]], [[0, 10, 11, 1], [1, 11, 12, 2], [2, 12, 20, 3], [3, 13, 14, 4], [5, 15, 16, 6],[6, 21, 17, 7], [7, 17, 18, 8], [8, 18, 19, 9], [13, 20, 21, 16], [14, 15, 16, 13]], [[1]]])))
    porta = STRUCT([R([1, 2])(PI / 4)(T([1, 2])([2, -0.25])(CUBOID([13, 0.5, 6.5]))), T(2)(12.3)(R([1, 2])(-PI / 4)(T([1, 2])([2, -0.25])(CUBOID([13, 0.5,6.5]))))])
    Tmedia = DIFFERENCE([MY_CYLINDER([1.8, 6.8])(16), MY_CYLINDER([1.6, 6.8])(16)])
    tmedia2 = DIFFERENCE([STRUCT([T([1, 2])([2, 2])(Tmedia), T([1, 2])([2, 10.4])(Tmedia), T([1, 2])([10.4, 2])(Tmedia), T([1, 2])([10.4, 10.4])(Tmedia)]), porta])
    murointerno2 = STRUCT([murointerno, T(1)(12.35)(R([1, 2])(PI/2)(murointerno)), T([1, 2])([12.4, 12.35])(R([1, 2])(PI)(murointerno)),T([1, 2])([0.03,12.4])(R([1, 2])(-PI/2)(murointerno))])
    elemento2 = STRUCT([T([1, 2, 3])([0.425, -0.1, 0.5])(MY_CYLINDER([0.225, 2.875])(16)), T([1, 2, 3])([1.175, -0.1, 0.5])(MY_CYLINDER([0.225, 2.875])(16))])
    elemento3 = STRUCT([DIFFERENCE([T([1, 2, 3])([0.425, 0.1, 2.875])(R([2, 3])(PI / 2)(MY_CYLINDER([0.225, 0.1])(16))),CUBOID([1.6, 0.1, 2.875])]), DIFFERENCE([T([1, 2, 3])([0.8, 0.05, 3.1])(R([2, 3])(PI / 2)(MY_CYLINDER([0.6, 0.1])(16))), T(2)(-0.05)(CUBOID([1.6, 0.1, 3.1]))]), DIFFERENCE([T([1, 2, 3])([1.175, 0.1, 2.875])(R([2, 3])(PI / 2)(MY_CYLINDER([0.225, 0.1])(16))), CUBOID([1.6, 0.1, 2.875])])])
    elemento4 = STRUCT([T(1)(0.3)(elemento2), T(1)(2.4)(elemento2), T(1)(8.4)(elemento2), T(1)(10.5)(elemento2)])
    elemento5 = T([2, 3])([-0.1, 0.5])(STRUCT([DIFFERENCE([CUBOID([1.6, 0.1, 3.95]), elemento3]), T([1, 3])([0.3, 4.5])(CUBOID([1, 0.1, 1]))]))
    muro2 = STRUCT([T(1)(0.3)(elemento5), T(1)(2.4)(elemento5), T(1)(8.4)(elemento5), T(1)(10.5)(elemento5)])
    finestra = MY_CYLINDER([0.225, 13])(16)
    finestre = T([2, 3])([12.8, 5.5])(R([2, 3])(PI / 2)(STRUCT([T(1)(1.1)(finestra), T(1)(3.2)(finestra), T(1)(9.2)(finestra),T(1)(11.3)(finestra)])))
    finestra2 = STRUCT([T([1, 2])([3.9, -2.3])(CUBOID([4.6, 4.6, 4.74])), T([1, 2, 3])([4.8, -1.4, 4.74])(CUBOID([2.8, 2.8, 0.35])), T([1, 2, 3])([6.2, -0.7, 5.09])(MY_CYLINDER([1.23, 3])(16))])
    lato = INTERSECTION([muro1, finestra2])
    lato2 = STRUCT([lato, T(2)(-0.2)(lato), T(2)(-0.4)(lato)])
    murocompleto = DIFFERENCE([STRUCT([muro1, elemento1, colonna, muro2]), STRUCT([elemento4, finestre, lato2])])
    muro_result = STRUCT([murocompleto, T(1)(12.4)(R([1, 2])(PI / 2)(murocompleto)), T([1, 2])([12.4, 12.4])(R([1, 2])(PI)(murocompleto)),T(2)(12.4)(R([1, 2])(3 * PI / 2)(murocompleto)), murointerno2, tmedia2])
    return muro_result
def Torri():

    #muro
    p1 = STRUCT([T([1, 2, 3])([4.6, 2.3, 3])(R([1, 3])(PI / 2)(MY_CYLINDER([0.9, 5])(16))),T([1, 2, 3])([2.3, 4.6, 3])(R([2, 3])(PI / 2)(MY_CYLINDER([0.9, 5])(16)))])
    p2 = STRUCT([T(1)(1.2)(CUBOID([2.2, 0.2, 3])), T([1, 2])([1.2, 4.4])(CUBOID([2.2, 0.2, 3])),T(2)(1.2)(CUBOID([0.2, 2.2, 3])), T([1, 2])([4.4, 1.2])(CUBOID([0.2, 2.2, 3]))])
    parte1 = STRUCT([p1, p2])
    muro1 =DIFFERENCE([CUBOID([4.6, 0.2, 4.3]), parte1])
    muri = STRUCT([muro1, T(1)(0.2)(R([1, 2])(PI / 2)(muro1)), T(2)(4.4)(muro1), T(1)(4.6)(R([1, 2])(PI / 2)(muro1))])
    murocompleto = STRUCT([T([1, 2])([1.3, 1.3])(muri)])

    porte = T(1)(3.3)(CUBOID([0.6, 7.2, 2]))
    t1 = DIFFERENCE([DIFFERENCE([T([1, 2])([3.6, 1.3])(torretta(1.1, 0.9, 2.5, 200)(0.3, 0.2, 0.07, 0.2)),T([1, 2])([1.5, 1.5])(CUBOID([4.2, 4.2, 3]))]), porte])
    t2 = DIFFERENCE([T([1, 2])([1.3, 3.6])(torretta(1.1, 0.9, 2.5, 200)(0.3, 0.2, 0.07, 0.2)),T([1, 2])([1.5, 1.5])(CUBOID([4.2, 4.2, 3]))])
    torre = STRUCT([t1, t2, T([1, 2])([7.2, 7.2])(R([1, 2])(PI)(t1)),T([1, 2])([7.2, 7.2])(R([1, 2])(-PI)(t2))])

    t1 = T([1, 2, 3])([1.05, 1.05, 4.3])(STRUCT([T(3)(0.15)(DIFFERENCE([CUBOID([5.1, 5.1, 0.3]), T([1, 2])([1.15, 1.15])
            (CUBOID([2.8, 2.8, 0.3]))])), T([1, 2])([0.15, 0.15])(DIFFERENCE([CUBOID([4.8, 4.8, 0.15]), T([1, 2])
            ([0.4, 0.4])(CUBOID([4, 4, 0.15]))])), T([1, 2, 3])([1.05, 1.05, 0.45])(DIFFERENCE([CUBOID([3, 3, 0.35]),
            T([1, 2])([0.1, 0.1])(CUBOID([2.8, 2.8, 0.25]))]))]))

    tetto = TEXTURE("marmo.png")(DIFFERENCE([t1, T([1, 2, 3])([3.6, 3.6, 4.75])(R([1, 2])(PI / 2)(MY_CYLINDER([1.15, 2.05])(16)))]))
    mediumTower = T([1, 2, 3])([3.6, 3.6, 5.1])(torremedia1(1.3, 1.1, 1.2)(0.2, 0.3, 0.15, 0.3))
    floorTower = MY_CYLINDER([1.3, 0.4])(16)
    floorA = TEXTURE("marmo.png")(T([1, 2])([1.2, 1.2])(STRUCT([T(1)(2.4)(floorTower), T(2)(2.4)(floorTower), T([1,2])([2.4, 4.8])(floorTower),
                     T([1,2])([4.8,2.4])(floorTower), CUBOID([4.8, 4.8, 0.4])])))
    dome = QUARTERSPHERE(1.1)([32, 32])
    domes = STRUCT([T([1, 2, 3])([3.6, 1.3, 3])(R([1, 2])(PI/2)(dome)), T([1, 2, 3])([1.3, 3.6, 3])(dome),
                    T([1, 2, 3])([3.6, 5.9, 3])(R([1, 2])(-PI/2)(dome)), T([1, 2,3])([5.9, 3.6, 3])(R([1, 2])(PI)(dome)),
                    T([1, 2, 3])([3.6, 3.6, 6.8])(HALFSPHERE(1.3)([32, 32]))])

    structure = STRUCT([T(3)(0.4)(STRUCT([torre, murocompleto, tetto, mediumTower])), floorA])

    #per visualizzare senza tetto
    #structure2 = STRUCT([T(3)(0.4)(STRUCT([torre, murocompleto, mediumTower])), floorA])
    #VIEW(structure2)
    return STRUCT([structure, TEXTURE("tegole2.png")(T(3)(0.4)(domes))])

def ggpl_leonardoChurch(dx, dy, dz):

    muro1 = muro()
    tetto = TEXTURE("marmo.png")(T([1, 2, 3])([-0.3, -0.3, 6.3])(STRUCT([T(3)(0.2)(CUBOID([13, 13, 0.3])),T([1, 2])([0.15, 0.15])(DIFFERENCE([CUBOID([12.7, 12.7, 0.2]),T([1, 2])([0.15, 0.15])(CUBOID([12.4, 12.4, 0.2]))]))])))
    buco1 = STRUCT([T([1, 2, 3])([2, 2, 6.5])(MY_CYLINDER([1.4, 0.4])(16)), T([1, 2, 3])([2, 10.4, 6.5])(MY_CYLINDER([1.4, 0.4])(16)), T([1, 2, 3])([10.4, 2, 6.5])(MY_CYLINDER([1.4, 0.4])(16)),T([1, 2, 3])([10.4, 10.4, 6.5])(MY_CYLINDER([1.4, 0.4])(16)), T([1, 2, 3])([6.2, 6.2, 6.5])(MY_CYLINDER([3, 0.4])(16))])
    buco2 = STRUCT([T([1, 2])([3.9, -2.3])(CUBOID([4.6, 4.6, 4.74])), T([1, 2, 3])([4.8, -1.4, 4.74])(CUBOID([2.8, 2.8, 0.35])), T([1, 2, 3])([6.2, -0.7, 5.09])(MY_CYLINDER([1.23, 3])(16))])
    lato = INTERSECTION([muro1, buco2])
    lato2 = STRUCT([lato, T(2)(-0.2)(lato), T(2)(-0.4)(lato)])
    laterale = STRUCT([lato2, T(1)(-0.2)(R([1, 2])(PI / 2)(lato2)),T(2)(12.6)(lato2), T(1)(12.4)(R([1, 2])(PI / 2)(lato2))])
    tetto2 = TEXTURE("marmo.png")(DIFFERENCE([tetto, STRUCT([buco1, laterale])]))
    torrem = STRUCT([T(3)(6.8)(torremedia2(1.6, 1.4, 1.5)(0.25, 0.25, 0.1, 0.25)), TEXTURE("tegole2.png")(T(3)(8.8)(HALFSPHERE(1.6)([16, 16])))])
    torrem2 = STRUCT([T([1, 2])([2, 2])(torrem), T([1, 2])([2, 10.4])(torrem), T([1, 2])([10.4, 2])(torrem), T([1, 2])([10.4, 10.4])(torrem)])
    torreg = STRUCT([T([1, 2, 3])([6.2, 6.2, 6.8])(torregrande(3, 2.8, 3)(0.5, 0.5, 0.2, 0.35)), T([1, 2, 3])([6.2, 6.2, 10.8])(TEXTURE("tegole2.png")(HALFSPHERE(2.8)([16, 16])))])

    #sostituendo queste istruzioni si puo vedere la struttura scoperchiata
    #torrem = STRUCT([T(3)(6.8)(torremedia2(1.6, 1.4, 1.5)(0.25, 0.25, 0.1, 0.25))
                     #])
    #torrem2 = STRUCT([T([1, 2])([2, 2])(torrem), T([1, 2])([2, 10.4])(torrem), T([1, 2])([10.4, 2])(torrem),T([1, 2])([10.4, 10.4])(torrem)])
    #torreg = STRUCT([T([1, 2, 3])([6.2, 6.2, 6.8])(torregrande(3, 2.8, 3)(0.5, 0.5, 0.2, 0.35))])
    gruppo_torri = Torri()
    fiancata  = STRUCT([T([1, 2])([2.6, -4.5])(gruppo_torri), T([1, 2])([2.7, 2.6])(R([1, 2])(PI/2)(gruppo_torri)),T([1, 2])([16.9, 2.6])(R([1, 2])(PI/2)(gruppo_torri)), T([1, 2])([2.6, 9.7])(gruppo_torri)])
    floor = TEXTURE("marmo.png")(T([1, 2])([-0.25, -0.25])(CUBOID([12.9, 12.9, 0.4])))
    base = TEXTURE("marmo.png")(STRUCT([T([1,2])([-3.2, -3.2])(CUBOID([18.8, 18.8, 0.5])), T([1,2])([1.6, -5.5])(CUBOID([9.8, 23.4, 0.5])),
                   T([1,2])([-5.5, 1.6])(CUBOID([23.4, 9.8, 0.5]))]))
    composozione = STRUCT([muro1, torrem2, torreg, tetto2])
    #composozione2 = STRUCT([muro1, torrem2, torreg])
    #VIEW(composozione2)
    leonardo_result = T([1, 2])([5.5, 5.5])(STRUCT([T(3)(0.9)(composozione), T(3)(0.5)(floor), base, T(3)(0.5)(fiancata)]))
    return S([1, 2, 3])([double(dx/23.4), double(dy/23.4), double(dz/16.35)])(leonardo_result)


#VIEW(STRUCT([torretta(1.1, 0.9, 2.5, 200)(0.3, 0.2, 0.07, 0.2),TEXTURE("tegole2.png")(T(3)(3)(HALFSPHERE(1.1)([16, 16])))]))
#VIEW(STRUCT([torremedia1(1.3, 1.1, 1.2)(0.2, 0.3, 0.15, 0.3), TEXTURE("tegole2.png")(T(3)(1.7)(HALFSPHERE(1.3)([16, 16])))]))
#VIEW(STRUCT([torremedia2(1.6, 1.4, 1.5)(0.25, 0.25, 0.1, 0.25), TEXTURE("tegole2.png")(T(3)(2)(HALFSPHERE(1.6)([16, 16])))]))
#VIEW(STRUCT([torregrande(3, 2.8, 3)(0.5, 0.5, 0.2, 0.35), TEXTURE("tegole2.png")(T(3)(4)(HALFSPHERE(2.8)([16, 16])))]))
#VIEW(Torri())


#dx, dy, dz = 23.4, 23.4, 16.35
dx, dy, dz = 11.7, 11.7, 8.175
VIEW(ggpl_leonardoChurch(dx, dy, dz))




