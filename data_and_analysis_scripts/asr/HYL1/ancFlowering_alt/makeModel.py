#!/usr/bin/python

# Homology modeling with ligand transfer from the template
from modeller import *              # Load standard Modeller classes
from modeller.automodel import *    # Load the automodel class

#####------------        CONTROL VARIABLES       ------------ #####
##             you should only have to change these.             ##
ALNFILE = 'ancFlowering_alignment.ali'      		# alignment file
KNOWNS  = '3ADJ'         	   		# name of template (known structure)
SEQ     = '1580_ancFlowering_DRB1'	# name of target (sequence of unknown structure)
NMODELS = 1                   		# number of models to build
##                                                               ##
#####------------      END CONTROL VARIABLES     ------------ #####

log.verbose()    # request verbose output
env = environ()  # create a new MODELLER environment to build this model in

# directories for input atom files
env.io.atom_files_directory = ['.','../..','../../..']

# Read in HETATM and water records from template PDBs
#env.io.hetatm = True
#env.io.water  = True

a = automodel(env,
              alnfile  = ALNFILE,  
              knowns   = KNOWNS,
              sequence = SEQ,
              assess_methods=(assess.DOPE, assess.DOPEHR)) # include assessment
a.starting_model= 1                 # index of the first model
a.ending_model  = NMODELS           # index of the last model
                                    # (determines how many models to calculate)
a.make()                            # do the actual homology modeling