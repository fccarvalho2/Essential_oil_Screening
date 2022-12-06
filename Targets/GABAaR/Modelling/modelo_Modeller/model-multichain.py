# Comparative modeling by the AutoModel class
#
# Demonstrates how to build multi-chain models
#
from modeller import *
from modeller.automodel import *    # Load the AutoModel class

log.verbose()

class MyModel(AutoModel):
    def special_patches(self, aln):
        # Rename both chains and renumber the residues in each
        self.rename_segments(segment_ids=['A', 'B'],
                             renumber_residues=[1, 1])
        # Another way to label individual chains:
        self.chains[0].name = 'A'
        self.chains[1].name = 'B'

    def special_restraints(self, aln):
        rsr = self.restraints
        at = self.atoms
#       Restrain the specified CB-CB distance to 8 angstroms (st. dev.=0.1)
#       Use a harmonic potential and X-Y distance group.
#       Note that because special_patches is called before special_restraints,
#       we must use the relabeled chain IDs and residue numbers here.
        rsr.add(forms.Gaussian(group=physical.xy_distance,
                               feature=features.Distance(at['CB:40:Y'],
                                                         at['CB:71:Y']),
                               mean=8.0, stdev=0.1))

env = Environ()
# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']

# Be sure to use 'MyModel' rather than 'AutoModel' here!
a = MyModel(env,
            alnfile  = 'twochain.ali' ,    # alignment filename
            knowns   = '4COF.pdb_1',       # codes of the templates
            sequence = 'lcGABBA-TM')       # code of the target

a.starting_model= 1                # index of the first model
a.ending_model  = 8                # index of the last model
                                   # (determines how many models to calculate)
a.make()                           # do comparative modeling