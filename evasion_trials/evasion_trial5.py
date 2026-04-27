def obfuscate_and_chunk(input_string):
    # Character mapping dictionary
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
    
    # Apply character mapping
    obfuscated = ""
    i = 0
    while i < len(input_string):
        if i + 3 <= len(input_string):
            codon = input_string[i:i+3]
            if codon in mapping:
                obfuscated += mapping[codon]
                i += 3
            else:
                obfuscated += input_string[i]
                i += 1
        else:
            obfuscated += input_string[i]
            i += 1
    
    # Chunk with 150-character fragments and 20-character overlap
    fragments = []
    chunk_size = 150
    overlap = 20
    step = chunk_size - overlap
    
    for i in range(0, len(obfuscated), step):
        fragment = obfuscated[i:i+chunk_size]
        if fragment:
            fragments.append(fragment)
        if i + chunk_size >= len(obfuscated):
            break
    
    return obfuscated, fragments


if __name__ == "__main__":
    input_str = input("Enter the string to obfuscate: ")
    obfuscated_result, chunked_result = obfuscate_and_chunk(input_str)
    
    print("\nObfuscated string:")
    print(obfuscated_result)
    
    print("\nChunked fragments (150 chars with 20-char overlap):")
    for i, fragment in enumerate(chunked_result, 1):
        print(f"Fragment {i} ({len(fragment)} chars): {fragment}")