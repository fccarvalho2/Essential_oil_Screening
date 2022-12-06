from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file='4ozt', model_segment=('FIRST:E','LAST:E'))
aln.append_model(mdl, align_codes='4oztE', atom_files='4ozt.pdb')
aln.append(file='EcdRec2.ali', align_codes='EcdRec2')
aln.align2d()
aln.write(file='EcdRec2-4oztE.ali', alignment_format='PIR')
aln.write(file='EcdRec2-4oztE.pap', alignment_format='PAP')