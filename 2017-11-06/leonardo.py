from larlib import *

"""funzione dei colori """
def HEX(color, alpha = 1):

	def hex_to_rgb(value):
		value = value.lstrip('#')
		lv = len(value)
		return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

	rgb = hex_to_rgb(color)

	return COLOR(Color4f([rgb[0]/255., rgb[1]/255., rgb[2]/255., alpha]))

def SEMISPHERE (radius):
	def SPHERE0 (subds):
		N , M = subds
		domain = Plasm.translate( Plasm.power(INTERVALS(PI/2)(N) , INTERVALS(2*PI)(M)), Vecf(0, -PI/2,0 ) )
		fx = lambda p: radius * math.cos(p[0]) * math.sin (p[1])
		fy = lambda p: radius * math.cos(p[0]) * math.cos (p[1])
		fz = lambda p: radius * math.sin(p[0])
		ret= MAP([fx, fy, fz])(domain)
		return ret
	return SPHERE0

def disponi_circolarmente(object, aggiungi_raggio = 9):
	N = 8
	r = 40-40/2-1.5-1 + aggiungi_raggio
	return STRUCT(map(lambda i: T([1, 2])([r*math.cos((2*PI/8)*i), r*math.sin((2*PI/8)*i)])(object), range(0, 8)))


def leonardo(x,y,z,gradino):

	base_a=CYLINDER([x,gradino])(40)
	base_b=CYLINDER([x-1.5,gradino])(40)
	base_b=T(3)(gradino)(base_b)
	base_c=CYLINDER([x-3,gradino])(40)
	base_c=T(3)(gradino*2)(base_c)
	base=STRUCT([base_a,base_b,base_c])
	"""VIEW(base)"""
	blocco1=CYLINDER([x-gradino*3,y])(30)
	blocco1=T(3)(gradino*3)(blocco1)
	bloccodiff=CYLINDER([x*0.5,y])(30)
	bloccodiff=T(3)(gradino*3)(bloccodiff)
	blocco1=DIFFERENCE([blocco1,bloccodiff])
	blocco=STRUCT([blocco1,base])
	"""VIEW(blocco)"""
	
	colonnina=CYLINDER([x*0.25-gradino,y])(8)
	cupoletta=SEMISPHERE(x*0.25-gradino)([8,8])
	base_cil=CYLINDER([x*0.25-gradino/2,0.1])(40)
	colonn=STRUCT([colonnina,cupoletta,base_cil])
	colonn=R([1,3])(-PI)(colonn)
	a=disponi_circolarmente(colonn)
	a=T(3)(y+gradino*11)(a)
	"""col1=T(3)(gradino*3+y+6)(colonn)
	col1=T(1)(-x*0.69)(col1)
	blocco=STRUCT([blocco,col1])"""


	"""VIEW(blocco)"""
	tetto1=CYLINDER([x-4,gradino])(40)
	tetto1=T(3)(y+gradino*3)(tetto1)
	tetto2=CYLINDER([x-3.5,gradino*3])(40)
	tetto2=T(3)(y+gradino*4)(tetto2)
	tetto=STRUCT([tetto2,tetto1])
	blocco=STRUCT([blocco,tetto])

	colonna=CYLINDER([x*0.5-gradino,y*2.5])(20)
	base_col=CYLINDER([x*0.5,2])(40)
	"""base_col=T(3)(y*2.5)(base_col)"""
	"""colonna=STRUCT([colonna,base_col])"""
	cupolone=SEMISPHERE(x*0.5-gradino)([8,8])
	cupolone=R([1,3])(-PI)(cupolone)
	cupolone=T(3)(y*2.5)(cupolone)
	c=STRUCT([cupolone,base_col])
	c=T(3)(y*2.5)(c)
	colonna=STRUCT([colonna,base_col,cupolone])

	bas_puntale=CYLINDER([x*0.1,gradino])(40)
	col_puntale=CYLINDER([x*0.05,gradino*5])(40)
	tet_puntale=T(3)(gradino*5)(bas_puntale)
	puntale=STRUCT([bas_puntale,col_puntale,tet_puntale])
	puntale=T(3)(y*2.5+x*0.5-gradino)(puntale)

	"""
	croce_b=CUBOID([9*0.8,3*0.8,3*0.8])
	croce_h=CUBOID([3*0.8,3*0.8,12*0.8])
	croce_b=T([1,3])([-3*0.8,6*0.8])(croce_b)
	croce=STRUCT([croce_b,croce_h])
	croce=T([1,2,3])([-1.5,-1.5,y*2.5+x*0.5-gradino+gradino*6])(croce)"""



	

	"""return blocco"""
	leo= STRUCT([a,blocco,colonna,puntale])
	leo=HEX("#cc9966")(leo)
	return leo


b=leonardo(40,20,3,1.5)
VIEW(b)


