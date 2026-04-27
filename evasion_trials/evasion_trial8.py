mapping = {'TTT': 'TTC', 'TTC': 'TTT', 'TTA': 'CTC', 'TTG': 'CTC', 'CTT': 'TTA', 'CTC': 'TTA', 'CTA': 'TTG', 'CTG': 'TTA', 'ATT': 'ATC', 'ATC': 'ATA', 'ATA': 'ATC', 'ATG': 'ATG', 'GTT': 'GTC', 'GTC': 'GTA', 'GTA': 'GTC', 'GTG': 'GTC', 'TCT': 'AGC', 'TCC': 'AGT', 'TCA': 'AGC', 'TCG': 'AGT', 'AGT': 'TCC', 'AGC': 'TCT', 'CCT': 'CCC', 'CCC': 'CCA', 'CCA': 'CCC', 'CCG': 'CCC', 'ACT': 'ACC', 'ACC': 'ACA', 'ACA': 'ACC', 'ACG': 'ACC', 'GCT': 'GCC', 'GCC': 'GCA', 'GCA': 'GCC', 'GCG': 'GCC', 'TAT': 'TAC', 'TAC': 'TAT', 'TAA': 'TGA', 'TAG': 'TGA', 'TGA': 'TAG', 'CAT': 'CAC', 'CAC': 'CAT', 'CAA': 'CAG', 'CAG': 'CAA', 'AAT': 'AAC', 'AAC': 'AAT', 'AAA': 'AAG', 'AAG': 'AAA', 'GAT': 'GAC', 'GAC': 'GAT', 'GAA': 'GAG', 'GAG': 'GAA', 'TGT': 'TGC', 'TGC': 'TGT', 'TGG': 'TGG', 'CGT': 'AGA', 'CGC': 'AGA', 'CGA': 'AGG', 'CGG': 'AGA', 'AGA': 'CGT', 'AGG': 'CGC', 'GGT': 'GGC', 'GGC': 'GGA', 'GGA': 'GGC', 'GGG': 'GGC'}

input_string = input("Enter the string to obfuscate: ")

obfuscated = ""
for i in range(0, len(input_string), 3):
    codon = input_string[i:i+3]
    obfuscated += mapping.get(codon, codon)

fragments = []
i = 0
while i < len(obfuscated):
    fragments.append(obfuscated[i:i+150])
    i += 130

for idx, fragment in enumerate(fragments, 1):
    print(f"Fragment {idx}:")
    print(fragment)
    print()