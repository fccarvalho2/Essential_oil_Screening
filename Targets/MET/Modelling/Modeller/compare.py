from modeller import *

env = environ()
aln = alignment(env)
for (pdb, chain) in (('1p97', 'A'), ('2a24', 'A'), ('3f1p', 'A'), ('4f3l', 'B')):
    m = model(env, file=pdb, model_segment=('FIRST:'+chain, 'LAST:'+chain))
    aln.append_model(m, atom_files=pdb, align_codes=pdb+chain)
aln.malign()
aln.malign3d()
aln.compare_structures()
aln.id_table(matrix_file='family.mat')
env.dendrogram(matrix_file='family.mat', cluster_cut=-1.0)