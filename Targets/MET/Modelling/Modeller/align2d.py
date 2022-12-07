from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file='3f1p', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='3f1pA', atom_files='3f1p.pdb')
aln.append(file='MetTolLcuprina.ali', align_codes='MetTolLcuprina')
aln.align2d()
aln.write(file='MetTolLcuprina-3f1pA.ali', alignment_format='PIR')
aln.write(file='MetTolLcuprina-3f1pA.pap', alignment_format='PAP')