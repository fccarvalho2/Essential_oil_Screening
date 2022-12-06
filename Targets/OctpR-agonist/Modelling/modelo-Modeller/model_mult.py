from modeller import *
from modeller.automodel import *

env = Environ()
a = AutoModel(env, alnfile='LcOambAGO-mult.ali',
              knowns=('AgoinstaAnophellesA','3sn6templateR'), sequence='LcOambAGO')
a.starting_model = 1
a.ending_model = 8
a.make()
