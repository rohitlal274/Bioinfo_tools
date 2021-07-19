from Bio.Seq import Seq
from Bio import SeqIO
from Bio import AlignIO
import sys
import os


path = input("Please put in the path to your multiple sequence alignments")
for file in os.listdir(path):
    if (file == "ungap.py"):
        continue
    else:
        output = file + "_output.fasta"
        with open(output, "w+") as t:
            for record in AlignIO.read(file, "fasta"):
                record.seq = record.seq.ungap("-")
                SeqIO.write(record, t, "fasta")
                cmd = "rm " + file
                os.system(cmd)
