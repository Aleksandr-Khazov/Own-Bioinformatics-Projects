filename = str(input("What is the file name? (include .txt etc)"))

with open(filename, "r") as infile, open("infile genome count.txt", "w") as outfile:

    DNA = ""
    n = {"A":0, "C":0, "G":0, "T":0}
    
    lines = infile.readlines()

    for line in lines:
        if not line.startswith(">"):
            DNA += line.strip()

            bases = DNA.split()
            n = {"A":0, "C":0, "G":0, "T":0}

            for base in DNA:
                if base in n:
                    n[base] += 1

    print(n["A"], n["C"], n["G"], n["T"])
