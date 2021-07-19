import re

path = input("Please input the path to your ungapped msa files")
for file in os.listdir(path):
    if file == "codon_remover.py":
        continue
    else:
        t = open(file + "_final.fa", "w+")
        with open(file, "r") as f:
            for line in f:
                ln = line
                if ln[0] == ">":
                    t.write(ln)
                else:
                    for index in range(0, len(ln), 3):
                        codon = ln[index:index+3]
                        print(codon)

                        if codon == "TGA" or codon == "TAA" or codon == "TAG":
                            print("Found stop codon")
                            t.write("NNN")
                        else:
                            t.write(codon)
