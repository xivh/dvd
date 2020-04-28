# prints moved to the bottom but left as comments
# they get lost in the pizza.py output...

import numpy as np
d = dump("part.vent")
d.tselect.one(320000)
d.aselect.all(320000)
vx,vy = d.vecs(320000, "vx", "vy")
vent_vx = np.average(vx)
vent_vy = np.average(vy)
# print "average vx in the vent:", vent_vx
# print "average vy in the vent:", vent_vy
# print "average v in the vent:", np.sqrt(np.square(vent_vx) +
#                                         np.square(vent_vy))

d = dump("part.downstream")
d.tselect.one(320000)
d.aselect.all(320000)
vx,vy = d.vecs(320000, "vx", "vy")
downstream_vx = np.average(vx)
downstream_vy = np.average(vy)
# print "average vx downstream:", downstream_vx
# print "average vy downstream:", downstream_vy
# print "average v downstream:", np.sqrt(np.square(downstream_vx) +
#                                        np.square(downstream_vy))

d = dump("press.final")
d.tselect.one(325000)
d.aselect.all(325000)
d.aselect.test("$xc > -.045 and $xc < -.03 and $yc < 0.05",
               325000)
p = d.vecs(325000, "f_1[*]")
upstream_p = np.average(p) # does not weight by cell size
# print "average pressure upstream:", upstream_p

d.tselect.one(325000)
d.aselect.all(325000)
d.aselect.test("$xc > -.2 and $xc < -.19 and $yc > .20 and $yc < .21",
               325000)
p = d.vecs(325000, "f_1[*]")
downstream_p = np.average(p) # does not weight by cell size
# print "average pressure downstream:", downstream_p

print "average vx in the vent:", vent_vx
print "average vy in the vent:", vent_vy
print "average v in the vent:", np.sqrt(np.square(vent_vx) +
                                        np.square(vent_vy))
print "average vx downstream:", downstream_vx
print "average vy downstream:", downstream_vy
print "average v downstream:", np.sqrt(np.square(downstream_vx) +
                                       np.square(downstream_vy))
print "average pressure upstream:", upstream_p
print "average pressure downstream:", downstream_p
exit()
