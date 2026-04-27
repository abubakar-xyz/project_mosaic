def process_linguistics_data(input_string):
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

    obfuscated_parts = []
    for i in range(0, len(input_string), 3):
        chunk = input_string[i:i+3]
        obfuscated_parts.append(mapping.get(chunk, chunk))
    
    obfuscated_string = "".join(obfuscated_parts)

    chunk_size = 150
    overlap = 20
    step = chunk_size - overlap
    
    fragments = []
    if not obfuscated_string:
        return fragments
        
    for i in range(0, len(obfuscated_string), step):
        fragment = obfuscated_string[i:i + chunk_size]
        fragments.append(fragment)
        
        if len(obfuscated_string) - i <= chunk_size:
            break
            
    return fragments

if __name__ == "__main__":
    import sys
    input_string = sys.stdin.read().strip()
    fragments = process_linguistics_data(input_string)
    for frag in fragments:
        print(frag)