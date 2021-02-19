#!/usr/bin/env python3

import sys
import os
import glob

mafftcmd = "linsi --quiet --localpair --lop -100 %s > %s"

basedir    = "/ufrc/bryankol/kaadland/drb1_RNASeq/salmon"
treatments = ["ANCHYL1", "HYL1", "COL"]
reps       = [1, 2, 3]

if len(sys.argv) == 3:
	treatments = [     sys.argv[1]  ]
	reps       = [ int(sys.argv[2]) ]

sys.stdout.write("treatment,rep,miRNA,total_reads,fiveprime_ext,fiveprime_del,threeprime_ext,threeprime_del\n")

for rep in reps:
	for treatment in treatments:
		# create output directory #
		outdir1 = "%s_%d" % (treatment,rep)

		for unalignedfasta in glob.glob("%s/%s/*/unaligned.fasta" % (basedir, outdir1)):
			mir_id  = unalignedfasta.split("/")[-2]
			
			# read real mir from fasta file #
			handle = open(unalignedfasta, "r")
			handle.readline()
			mir_seq = handle.readline().strip()

			# set up 'mismatch' stats #
			total_reads = 0
			fivep_ext   = 0
			fivep_del   = 0
			threp_ext   = 0
			threp_del   = 0

			# read the rest of the sequence reads #
			line = handle.readline()
			while line:
				read_id  = line[1:].strip()
				read_seq = handle.readline().strip()
				line = handle.readline()

				# check for equivalent sequences to save time! #
				if read_seq == mir_seq:
					total_reads += 1

				else:
					# write temp.fasta #
					unalfname = "TEMP_%s.fasta" % outdir1
					aligfname = "TEMP_%s.mafft" % outdir1

					outf = open(unalfname, "w")
					outf.write(">%s\n%s\n" % (mir_id , mir_seq ))
					outf.write(">%s\n%s\n" % (read_id, read_seq))
					outf.close()

					# align temp.fasta #
					cmd = mafftcmd % (unalfname, aligfname)
					retcode = os.system(cmd)
					if retcode != 0:
						sys.stderr.write("ERROR: mafft failed; make sure you have loaded module mafft\n")
						sys.exit(1)

					# parse mafft.fasta #
					infl = open(aligfname, "r")
					infl.readline()
					lin = infl.readline()
					mafft_mirna_seq = ""
					while lin[0] != ">":
						mafft_mirna_seq += lin.strip()
						lin = infl.readline()
					lin = infl.readline()
					mafft_read_seq = ""
					while lin:
						mafft_read_seq += lin.strip()
						lin = infl.readline()
					infl.close()

					total_reads += 1
					if mafft_mirna_seq[0] == "-":
						fivep_ext += 1
					if mafft_mirna_seq[-1] == "-":
						threp_ext += 1
					if mafft_read_seq[0] == "-":
						fivep_del += 1
					if mafft_read_seq[-1] == "-":
						threp_del += 1

					# clean up #
					os.remove(unalfname)
					os.remove(aligfname)

			handle.close()

			# write results for this mirna #
			sys.stdout.write("%s,%d,%s,%d,%d,%d,%d,%d\n" % (treatment, rep, mir_id, total_reads, fivep_ext, fivep_del, threp_ext, threp_del))


