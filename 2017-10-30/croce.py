from larlib import *
croce_b=CUBOID([1.5,0.5,0.5])
croce_h=CUBOID([0.5,0.5,2])
croce_b=T([1,3])([-0.5,1])(croce_b)
croce=STRUCT([croce_b,croce_h])
VIEW(croce)