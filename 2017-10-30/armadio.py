from larlib import *

"""funzione dei colori """
def HEX(color, alpha = 1):

	def hex_to_rgb(value):
		value = value.lstrip('#')
		lv = len(value)
		return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

	rgb = hex_to_rgb(color)

	return COLOR(Color4f([rgb[0]/255., rgb[1]/255., rgb[2]/255., alpha]))

def ggpl_libreria(x,spx,y,spy,z,spz,nripiani,nante):
	

	"""parete2 consiste nella creazione di una parete sottilissima che serve a realizzare
	la libreria con due colori diversi uno per l'interno e uno per l'esterno"""
	parete = CUBOID([spx, y, z])
	parete2 = T(1)(-0.01)(parete)
	parete2=HEX("#8b4513")(parete2)
	parete=HEX("#ffdab9")(parete)

	parete=STRUCT([parete,parete2])
	tetto = CUBOID([x,spy,z])
	tetto=HEX("#8b4513")(tetto)
	base=T(2)(y)(tetto)
	base=HEX("##8b4513")(base)
	laterale = CUBOID([x,y,spz])
	laterale=HEX("##8b4513")(laterale)
	lat2=T(3)(z-spz)(laterale)
	ripiano=STRUCT([parete,tetto,base,laterale,lat2])
	app=ripiano 
	"""variabile d'appoggio per non modificare la struttura originale che richiamo nel ciclo"""
	i=0
	while(i<nripiani):
		"""per ripetere i ripiani"""
		c=y*i
		b=T(2)(c)(ripiano)
		app=STRUCT([app,b])
		i=i+1

	armadio=app
	"""varibile d'appoggio come sopra"""
	i=0
	while(i<nante):
		"""per ripetere le ante """
		c=z*i
		b=T(3)(c)(app)
		armadio=STRUCT([armadio,b])
		i=i+1

	armadio2=T(3)(z*nante+0.5)(armadio)
	armadios=STRUCT([armadio,armadio2])
	pavimento = HEX("#f4a460")(CUBOID([0, 3, z*nante*2+1]))
	paret = HEX("#f4a460")(CUBOID([4, 3,0]))
	parete2 = HEX("#f4a460")(CUBOID([4, 0,z*nante*2+1]))
	parete3 = T(3)(z*nante*2+1)(paret)

	arm= STRUCT([paret, pavimento, armadios,parete2,parete3])
	return arm


VIEW(ggpl_libreria(x=1.5,spx=0.041,y=0.5,spy=0.04,z=1.7,spz=0.1,nripiani=3,nante=4))

