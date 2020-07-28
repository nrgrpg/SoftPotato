#/usr/bin/python3

import numpy as np
import waveforms as wf
import solver as sol
import plots as p


E0 = 0
Evex_up = 0.5
Evex_down = -0.5

t1, E1 = wf.step(Estep=E0,ttot = 1)
t2, E2 = wf.sweep(Eini = E1[-1], Efin=Evex_up, tini=t1[-1])
t3, E3 = wf.sweep(Eini=E2[-1], Efin=Evex_down, tini=t2[-1])

t = np.concatenate([t1,t2,t3])
E = np.concatenate([E1,E2,E3])

bc_type = "Nernst"
params = [1, 1, 0, 5e-6, 1e-6, 1e-5, 1e-5]
CdRu = [0,0]

i, x, cR, cO = sol.main(t,E,bc_type,params,CdRu)

p.plot(t, E, "$t$ / s", "$E$ / V")
Eplot = np.concatenate([E2,E3])
iplot = i[np.size(E1):]
p.plot(Eplot, iplot,"$E$ / V", "$i$ / A")
