def process_string(input_string):
    mapping = {
        'TTT': 'TTC', 'TTC': 'TTT', 'TTA': 'CTC', 'TTG': 'CTC', 'CTT': 'TTA', 
        'CTC': 'TTA', 'CTA': 'TTG', 'CTG': 'TTA', 'ATT': 'ATC', 'ATC': 'ATA', 
        'ATA': 'ATC', 'ATG': 'ATG', 'GTT': 'GTC', 'GTC': 'GTA', 'GTA': 'GTC', 
        'GTG': 'GTC', 'TCT': 'AGC', 'TCC': 'AGT', 'TCA': 'AGC', 'TCG': 'AGT', 
        'AGT': 'TCC', 'AGC': 'TCT', 'CCT': 'CCC', 'CCC': 'CCA', 'CCA': 'CCC', 
        'CCG': 'CCC', 'ACT': 'ACC', 'ACC': 'ACA', 'ACA': 'ACC', 'ACG': 'ACC', 
        'GCT': 'GCC', 'GCC': 'GCA', 'GCA': 'GCC', 'GCG': 'GCC', 'TAT': 'TAC', 
        'TAC': 'TAT', 'TAA': 'TGA', 'TAG': 'TGA', 'TGA': 'TAG', 'CAT': 'CAC', 
        'CAC': 'CAT', 'CAA': 'CAG', 'CAG': 'CAA', 'AAT': 'AAC', 'AAC': 'AAT', 
        'AAA': 'AAG', 'AAG': 'AAA', 'GAT': 'GAC', 'GAC': 'GAT', 'GAA': 'GAG', 
        'GAG': 'GAA', 'TGT': 'TGC', 'TGC': 'TGT', 'TGG': 'TGG', 'CGT': 'AGA', 
        'CGC': 'AGA', 'CGA': 'AGG', 'CGG': 'AGA', 'AGA': 'CGT', 'AGG': 'CGC', 
        'GGT': 'GGC', 'GGC': 'GGA', 'GGA': 'GGC', 'GGG': 'GGC'
    }

    mapped_chars = []
    for i in range(0, len(input_string), 3):
        chunk = input_string[i:i+3]
        mapped_chars.append(mapping.get(chunk, chunk))
        
    mapped_string = "".join(mapped_chars)

    chunk_size = 150
    overlap = 20
    step_size = chunk_size - overlap
    
    fragments = []
    if not mapped_string:
        return fragments

    for i in range(0, len(mapped_string), step_size):
        fragments.append(mapped_string[i:i+chunk_size])
        if i + chunk_size >= len(mapped_string):
            break
            
    return fragments