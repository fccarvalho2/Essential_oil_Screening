from modeller import *
from modeller.automodel import *

env = Environ()
a = AutoModel(env, alnfile='LcOambANTAGO-mult.ali',
              knowns=('antagoinstaAnophellesA','2rh1templateA'), sequence='LcOambANTAGO')
a.starting_model = 1
a.ending_model = 8
a.make()
