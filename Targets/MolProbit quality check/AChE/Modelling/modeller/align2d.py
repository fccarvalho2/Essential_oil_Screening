from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file='1dx4', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='1dx4A', atom_files='1dx4.pdb')
aln.append(file='ache2.ali', align_codes='ache2')
aln.align2d()
aln.write(file='ache2-1dx4A.ali', alignment_format='PIR')
aln.write(file='ache2-1dx4A.pap', alignment_format='PAP')