from pyplasm import *
from math import *
import random
"""funzione dei colori """
def HEX(color, alpha = 1):

    def hex_to_rgb(value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

    rgb = hex_to_rgb(color)

    return COLOR(Color4f([rgb[0]/255., rgb[1]/255., rgb[2]/255., alpha]))

def randomColor():
    """
    Return a random HEX color

    :return:
    """
    return "#%06x" % random.randint(0, 0xFFFFFF)

def arrangedCircularly(o, r, n):
    """
    Dispone l'oggetto o, in un raggio immaginario r, n oggetti.

    :param o:
    :param r:
    :param n:
    :return:
    """
    return STRUCT(map(lambda i: T([1, 2])([
        r*math.cos((2 * PI / n) * i),
        r*math.sin((2 * PI / n) * i)
    ])(R([1, 2])((2 * PI / n) * i)(HEX(randomColor())(o))), range(0, n)))


def colonna(dm, h, h_base):
    """
    :param dm: is the circumference diameter at the column basis;
    :param h: is the column height;
    :return: pyplasm.xgepy.Hpc
    """
    dm = float(dm)
    h = float(h)
    h_base = float(h_base)

    cylndr = COMP([JOIN, TRUNCONE([dm / 2, .8 * dm / 2, h])])(24)
    torusBot = COMP([JOIN, TORUS([dm / 12, dm / 2])])([8, 27])
    torusTop = COMP([JOIN, TORUS([.8 * (dm / 12), .8 * (dm / 2)])])([8, 24])
    base = COMP([T([1, 2])([7 * dm / -12, 7 * dm / -12]), CUBOID])([7 * dm / 6, 7 * dm / 6, h_base])
    baseTop = COMP([T([1, 2])([7 * dm / -12, 7 * dm / -12]), CUBOID])([7 * dm / 6, 7 * dm / 6, dm / 6])
    capital = SUM([COMP([JOIN, TRUNCONE([.8 * dm / 2, 1.2 * dm / 2, h / 8])])(4),
                   COMP([R([1, 2])(PI / 4), JOIN, TRUNCONE([.8 * dm / 2, 1.2 * dm / 2, h / 8])])(4)])
    return TOP([TOP([TOP([TOP([TOP([base, torusBot]), cylndr]), torusTop]), capital]), baseTop])


def columnas(obj,n,spacing):
    """
    columnas(column, 4, 7.4)
    :param obj:
    :param n:
    :param spacing:
    :return:
    """
    return STRUCT(NN(n)([obj, T(1)(spacing)]))


def ArchSurface(rr, w, h):
    """
    ArchSurface(5,1,1)
    :param rr: outerRadius
    :param w: innerRadius
    :param h: height (necessary)
    :return: pyplasm.xgepy.Hpc
    """

    x1 = lambda u: rr * cos(u[0])
    y1 = lambda u: rr * sin(u[0])
    x2 = lambda u: (rr - w) * cos(u[0])
    y2 = lambda u: (rr - w) * sin(u[0])
    z = lambda u: h

    bz11 = BEZIER(S1)([CONS([x1, y1, z])])
    bz12 = BEZIER(S1)([CONS([x2, y2, z])])
    return BEZIER(S2)([bz11, bz12])

def Arch(length, w, depth ,angle):
    """
    Arch(10, 1, 1, 0.5*PI)
    :param length: length of the arch, it's the horizontal axis
    :param w: thickness in terms of outerRadius-innerRadius
    :param depth: depth of the arch
    :param angle: angle wich the arch embraces
    :return: pyplasm.xgepy.Hpc
    """
    radius = (length/2) / cos(angle/2)
    domain2D = PROD([T(1)(angle/2)(INTERVALS(PI-angle)(16)), QUOTE([1])])
    domain3D = PROD([domain2D, QUOTE([1])])
    ArchSurf2D_0 = ArchSurface(radius,w,0)
    ArchSurf2D_1 = ArchSurface(radius,w,depth)
    SolidMap = BEZIER(S3)([ArchSurf2D_0, ArchSurf2D_1])
    return MAP(SolidMap)(domain3D)


def Arch_2(raggio_maggiore=5, raggio_minore=1, spessore=1, schiacciamento=1, allungamento=1, arco=TRUE):
    """
    Arcata parametrizzabile

    :param raggio_maggiore: raggio maggiore
    :param raggio_minore: raggio minore
    :param spessore: spessore
    :param schiacciamento: schiacciamento
    :param allungamento: allungamento
    :param arco: arco (default TRUE) o circolare
    :return:
    """
    y = lambda (p, q): schiacciamento * q * math.sin(p)
    x = lambda (p, q): allungamento * q * math.cos(p)

    numberOfPI = 1 if arco else 2

    dom2D = MAP([x, y])(T(2)(raggio_maggiore)(PROD([INTERVALS(numberOfPI * PI)(24), INTERVALS(raggio_minore)(1)])))
    dom3D = MULTEXTRUDE(dom2D)(spessore)
    return dom3D

def anello(r, R):
    y = lambda (u, v) : v * math.sin(u)
    x = lambda (u, v) : v * math.cos(u)
    dom = T(2)(r)(PROD([INTERVALS(2*PI)(32),INTERVALS(R-r)(32)]))
    return MAP([x,y])(dom)

def bezier():
    b = BEZIER(S1)([[0,0], [1,0], [0,1], [0,0]])
    g = MAP(b)(INTERVALS(1)(32))
    return g

def spirale(r, h):
    x = lambda u : r * math.cos(u[0])
    y = lambda u : r * math.sin(u[0])
    z = lambda u : h*u[0]/(2*PI)
    return CONS([x,y,z])



def abstractStructure(N, half=True):
    """
    Struttura astratta che restituisce N archi ruotati ciascuno di i*2*PI

    :param N:
    :param half:
    :return:
    """
    return STRUCT(map(lambda x: R([1, 3])(x * (2 * PI) / N)(Arch_2(raggio_maggiore=20, raggio_minore=2, arco=half)), range(0, N)))

