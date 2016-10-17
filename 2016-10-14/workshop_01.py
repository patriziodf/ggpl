from larlib import * 

def edificio((px,py),(tz,ty),distanze, interpiano):
	
	""" realiazzazione piloni """

	"""creazione base piloni """
	piloni = [px]

	""" spaziatura dei piloni lungo x"""
	for value in distanze:
		piloni = piloni+[-value]+[px]

	""" altezza dei piloni ovvero distanza tra tutti gli interpiani"""
	altezza = []
	for value in interpiano:
		altezza = altezza+[value+tz]
	
	""" disegno lungo gli assi x,y,z e prodotto cartesiano per avere la struttura completa dei piloni """
	
	xpiloni = QUOTE(piloni)
	ypiloni = QUOTE([py])
	zpiloni = QUOTE(altezza)
	xypiloni= PROD([xpiloni, ypiloni])
	piloni_completi = PROD([xypiloni, zpiloni])


	""" realiazzazione travi """

	""" lunghezza travi sfruttando le distanze tra i piloni """
	trave = [ -x for x in piloni]

	""" distanza travi """
	spazio = []
	for value in interpiano:
		spazio = spazio+[-value]+[tz]
	
	""" disegno lungo gli assi x,y,z e prodotto cartesiano per avere la struttura completa delle travi """
	xtravi= QUOTE(trave)
	ytravi = QUOTE([ty])
	ztravi=QUOTE(spazio)
	xytravi = PROD([xtravi, ytravi])
	travi_complete = PROD([xytravi, ztravi])
	
	""" valori di ritorno della funzione in una struttura"""
	struttura_edificio = STRUCT([piloni_completi, travi_complete])
	return struttura_edificio
	


def main():
	VIEW(edificio((0.7,0.7),(0.8,0.7),[1,4,6,4,1],[4,2,3,2,1]))

if __name__=='__main__':
	main()
