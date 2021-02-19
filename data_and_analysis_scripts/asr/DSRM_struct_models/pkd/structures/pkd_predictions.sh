#!/bin/bash

module add openbabel
module add R

basedr=/ufrc/bryankol/kaadland/analyses/DSRM_struct_models/pkd/structures

for i in struct.[0-9].pdb;	do
	#extract protein and ligand
	${basedr}/extractChain.py $i A   > $i.protein.pdb
	${basedr}/extractChain.py $i B C > $i.ligand.pdb
	#convert ligand to mol2
	babel -ipdb $i.ligand.pdb -omol2 $i.ligand.mol2
	#creates shortcuts for the required files
	ln -s ${basedr}/glm/GLM-Score-master/asa ./
	ln -s ${basedr}/glm/GLM-Score-master/R ./
	ln -s ${basedr}/glm/GLM-Score-master/hydrophobicity.param ./
	ln -s ${basedr}/glm/GLM-Score-master/tension.param ./

	#predict pKd 
	${basedr}/glm/GLM-Score-master/GLM-Score $i.protein.pdb $i.ligand.pdb $i.ligand.mol2 protein
done
