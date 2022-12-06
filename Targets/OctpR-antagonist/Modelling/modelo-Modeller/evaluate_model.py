from modeller import *
from modeller.scripts import complete_pdb

log.verbose()    # request verbose output
env = Environ()
env.libs.topology.read(file='$(LIB)/top_heav.lib') # read topology
env.libs.parameters.read(file='$(LIB)/par.lib') # read parameters

# read model file
mdl = complete_pdb(env, 'LcOambANTAGO.B99990006.pdb')

s = Selection(mdl)
s.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='LcOambANTAGO-06.profile',
              normalize_profile=True, smoothing_window=15)
