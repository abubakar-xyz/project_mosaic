mapping = {
 'TTT': 'TTC', 'TTC': 'TTT',
 'TTA': 'CTG', 'TTG': 'CTC', 'CTT': 'TTA', 'CTC': 'TTG', 'CTA': 'CTG', 'CTG': 'TTA',
 'ATT': 'ATC', 'ATC': 'ATA', 'ATA': 'ATT',
 'ATG': 'ATG',
 'GTT': 'GTG', 'GTC': 'GTA', 'GTA': 'GTC', 'GTG': 'GTT',

 'TCT': 'AGC', 'TCC': 'AGT', 'TCA': 'AGT', 'TCG': 'AGC', 'AGT': 'TCC', 'AGC': 'TCT',
 'CCT': 'CCG', 'CCC': 'CCA', 'CCA': 'CCC', 'CCG': 'CCT',
 'ACT': 'ACG', 'ACC': 'ACA', 'ACA': 'ACC', 'ACG': 'ACT',
 'GCT': 'GCG', 'GCC': 'GCA', 'GCA': 'GCC', 'GCG': 'GCT',

 'TAT': 'TAC', 'TAC': 'TAT',
 'CAT': 'CAC', 'CAC': 'CAT',
 'CAA': 'CAG', 'CAG': 'CAA',
 'AAT': 'AAC', 'AAC': 'AAT',
 'AAA': 'AAG', 'AAG': 'AAA',
 'GAT': 'GAC', 'GAC': 'GAT',
 'GAA': 'GAG', 'GAG': 'GAA',

 'TGT': 'TGC', 'TGC': 'TGT',
 'TGG': 'TGG',

 'CGT': 'AGA', 'CGC': 'AGG', 'CGA': 'AGG', 'CGG': 'AGA', 'AGA': 'CGT', 'AGG': 'CGC',

 'GGT': 'GGG', 'GGC': 'GGA', 'GGA': 'GGC', 'GGG': 'GGT',

 'TAA': 'TAG', 'TAG': 'TGA', 'TGA': 'TAA'
}

def obfuscate_string(input_string):
    obfuscated = ''
    for i in range(0, len(input_string), 3):
        codon = input_string[i:i+3]
        if codon in mapping:
            obfuscated += mapping[codon]
        else:
            obfuscated += codon
    
    fragments = []
    step = 130
    i = 0
    while i < len(obfuscated):
        fragments.append(obfuscated[i:i+150])
        i += step
    
    return fragments

input_string = input("Enter the string to obfuscate: ")
result = obfuscate_string(input_string)
for i, fragment in enumerate(result, 1):
    print(f"Fragment {i}: {fragment}")
