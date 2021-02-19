#!/usr/bin/python

import sys
import os

alnstr = """>P1;%s
sequence:%s:::::::0.00: 0.00
%s
/
%s
*

>P1;3adi_dimer
structure:3adi_dimer::A::C:::0.00: 0.00
HVFKSR-LQEYAQKYKLPTPVY-EIVKE-GPSHKSLFQSTVILDGVRYNSLPGFFNRKAAEQSAAEVALRELAK-
/
HVFKSR-LQEYAQKYKLPTPVY-EIVKE-GPSHKSLFQSTVILDGVRYNSLPGFFNRKAAEQSAAEVALRELAK-
*
"""

modelerpy = """#!/usr/bin/python

# Homology modeling with ligand transfer from the template
from modeller import *              # Load standard Modeller classes
from modeller.automodel import *    # Load the automodel class

#####------------        CONTROL VARIABLES       ------------ #####
##             you should only have to change these.             ##
ALNFILE = 'alignment.ali'      # alignment file
KNOWNS  = '3adi_dimer'         # name of template (known structure)
SEQ     = '%s'   # name of target (sequence of unknown structure)
NMODELS = 100                  # number of models to build
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
"""

alns = {
"334182203_At_DCL1_DSRM1__1578_ancDRB1_DRB6_DSRM1" : [
"---PVRELQERCQQQAEGLEYKASRSGNTA---TVEVFIDGVQVGVAQNPQKKMAQKLAARNALAALQPFTRQTL",
"-MYKSR-LQEYAQKSGLPTPVY-ETVNE-GPSHEPRFRSTVIVNGVRYDSPPGFPHRKAAEQSAAKVALEELAKK"],

"334182203_At_DCL1_DSRM1__1578_ancDRB1_DRB6_DSRM2" : [
"---PVRELQERCQQQAEGLEYKASRSGNTA---TVEVFIDGVQVGVAQNPQKKMAQKLAARNALAALQPFTRQTL",
"-GLCKNILQEYAQKMNYPLPTY-KCTKNEGEGRAPVFTSTVEIGGVTYTGDA--ARSKKEAEIKAARTAILAIQS"],

"334182203_At_DCL1_DSRM1__At_DRB1_DSRM1" : [
"---PVRELQERCQQQAEGLEYKASRSGNTA---TVEVFIDGVQVGVAQNPQKKMAQKLAARNALAALQPFTRQTL",
"HVFKSR-LQEYAQKYKLPTPVY-EIVKE-GPSHKSLFQSTVILDGVRYNSLPGFFNRKAAEQSAAEVALRELAK-"],

"334182203_At_DCL1_DSRM1__At_DRB1_DSRM2" : [
"---PVRELQERCQQQAEGLEYKASRSGNTA---TVEVFIDGVQVGVAQNPQKKMAQKLAARNALAALQPFTRQTL",
"HGLCKNLLQEYAQKMNYAIPLY-QCQKVETLGRVTQFTCTVEIGGIKYTGA--ATRTKKDAEISAGRTALLAIQS"],

"1308_ancPlant_DCL1_DSRM1__1578_ancDRB1_DRB6_DSRM1" : [
"---PVRELQERCQQQAEGLEYKASRAGNVA---TVEVYVDGVQIGSAQNAQKKMAQKLAARNALVILKEKEVTKE",
"-MYKSR-LQEYAQKSGLPTPVY-ETVNE-GPSHEPRFRSTVIVNGVRYDSPPGFPHRKAAEQSAAKVALEELAKK"],

"1308_ancPlant_DCL1_DSRM1__1578_ancDRB1_DRB6_DSRM2" : [
"---PVRELQERCQQQAEGLEYKASRAGNVA---TVEVYVDGVQIGSAQNAQKKMAQKLAARNALVILKEKEVTKE",
"-GLCKNILQEYAQKMNYPLPTY-KCTKNEGEGRAPVFTSTVEIGGVTYTGDA--ARSKKEAEIKAARTAILAIQS"]
}


def launchSeq(mydir,myid,myseq1,myseq2):
	if not os.path.exists("%s/%s" % (mydir,myid)):
		os.mkdir("%s/%s" % (mydir,myid))
	wrkdir = "%s/%s" % (mydir,myid)
	
	#write alignment file#
	handle = open("%s/alignment.ali" % wrkdir, "w")
	handle.write(alnstr % (myid,myid,myseq1,myseq2))
	handle.close()
	#write modeler run file#
	handle = open("%s/runModeller.py" % wrkdir, "w")
	handle.write(modelerpy % (myid))
	handle.close()
	os.system("chmod 775 %s/runModeller.py" % wrkdir)
	#copy other needed scripts#
	os.system("cp parseBestModel.py %s/" % wrkdir)
	sys.stderr.write("finished: %s %s\n" % (mydir,myid))

dr = "models"
for (name,seqs) in alns.items():
	myid = name
	se = seqs[0]
	se2 = seqs[1]
	launchSeq(dr,myid,se,se2)
