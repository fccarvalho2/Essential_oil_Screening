from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file='5v13', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='5v13A', atom_files='5v13.pdb')
aln.append(file='AaJHbinding2.ali', align_codes='AaJHbinding2')
aln.align2d()
aln.write(file='AaJHbinding2-5v13A.ali', alignment_format='PIR')
aln.write(file='AaJHbinding2-5v13A.pap', alignment_format='PAP')