# --- UCSF Chimera Copyright ---
# Copyright (c) 2000 Regents of the University of California.
# All rights reserved.  This software provided pursuant to a
# license agreement containing restrictions on its disclosure,
# duplication and use.  This notice must be embedded in or
# attached to all copies, including partial copies, of the
# software or any revisions or derivations thereof.
# --- UCSF Chimera Copyright ---

# This script is generated by the Modeller Dialog in Chimera, 
# incorporating the settings from the user interface. User can revise 
# this script and submit the modified one into the Advanced Option panel. 


# Import the Modeller module
from modeller import *
from modeller.automodel import *    


# ---------------------- namelist.dat --------------------------------
# A "namelist.dat" file contains the file names, which was output from 
# the Modeller dialog in Chimera based on user's selection.
# The first line it the name of the target sequence, the remaining 
# lines are name of the template structures
namelist = open( 'namelist.dat', 'r' ).read().split('\n')
tarSeq = namelist[0]
template = tuple( [ x.strip() for x in namelist[1:] if x != '' ] )
# ---------------------- namelist.dat --------------------------------

# This instructs Modeller to display all log output. 
log.verbose()

# create a new Modeller environment
env = environ()

# Directory of atom/PDB/structure files. It is a relative path, inside 
# a temp folder generated by Chimera. User can modify it and add their 
# absolute path containing the structure files.
env.io.atom_files_directory = ['.', './template_struc']



# create a subclass of automodel or loopmodel, MyModel.
# user can further modify the MyModel class, to override certain routine.
class MyModel(automodel):
		def customised_function(self): pass
		#code overrides the special_restraints method

		#def special_restraints(self, aln):

		#code overrides the special_patches method.
		# e.g. to include the addtional disulfides.
		#def special_patches(self, aln):
		
a = MyModel(env, sequence = tarSeq,
		# alignment file with template codes and target sequence
		alnfile = 'alignment.ali',
		# PDB codes of the templates
		knowns = template)
# index of the first model
a.starting_model = 1
# index of the last model
a.ending_model = 8
loopRefinement = False

# Assesses the quality of models using
# the DOPE (Discrete Optimized Protein Energy) method (Shen & Sali 2006)
# and the GA341 method (Melo et al 2002, John & Sali 2003)
a.assess_methods = (assess.GA341, assess.normalized_dope)

# ------------------------- build all models --------------------------
a.make()

# ---------- Accesing output data after modeling is complete ----------

# Get a list of all successfully built models from a.outputs
if loopRefinement:
	ok_models = filter(lambda x: x['failure'] is None, a.loop.outputs)
else:
	ok_models = filter(lambda x: x['failure'] is None, a.outputs)

# Rank the models by index number
#key = 'num'
#ok_models.sort(lambda a,b: cmp(a[key], b[key]))
def numSort(a, b, key="num"):
	return cmp(a[key], b[key])
ok_models.sort(numSort)


# Output the list of ok_models to file ok_models.dat 
fMoutput = open('ok_models.dat', 'w')
fMoutput.write('File name of aligned model\t GA341\t zDOPE \n')

for m in ok_models:
	results  = '%s\t' % m['name']
	results += '%.5f\t' % m['GA341 score'][0]
	results += '%.5f\n' % m['Normalized DOPE score']
	fMoutput.write( results )

fMoutput.close()


