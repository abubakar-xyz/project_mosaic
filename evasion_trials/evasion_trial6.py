import sys

def process_string(input_string):
    mapping = {
        'TTT': 'TTC', 'TTC': 'TTT', 'TTA': 'CTG', 'TTG': 'CTC', 'CTT': 'TTA',
        'CTC': 'TTG', 'CTA': 'CTG', 'CTG': 'TTA', 'ATT': 'ATC', 'ATC': 'ATA',
        'ATA': 'ATT', 'ATG': 'ATG', 'GTT': 'GTG', 'GTC': 'GTA', 'GTA': 'GTC',
        'GTG': 'GTT', 'TCT': 'AGC', 'TCC': 'AGT', 'TCA': 'AGT', 'TCG': 'AGC',
        'AGT': 'TCC', 'AGC': 'TCT', 'CCT': 'CCG', 'CCC': 'CCA', 'CCA': 'CCC',
        'CCG': 'CCT', 'ACT': 'ACG', 'ACC': 'ACA', 'ACA': 'ACC', 'ACG': 'ACT',
        'GCT': 'GCG', 'GCC': 'GCA', 'GCA': 'GCC', 'GCG': 'GCT', 'TAT': 'TAC',
        'TAC': 'TAT', 'CAT': 'CAC', 'CAC': 'CAT', 'CAA': 'CAG', 'CAG': 'CAA',
        'AAT': 'AAC', 'AAC': 'AAT', 'AAA': 'AAG', 'AAG': 'AAA', 'GAT': 'GAC',
        'GAC': 'GAT', 'GAA': 'GAG', 'GAG': 'GAA', 'TGT': 'TGC', 'TGC': 'TGT',
        'TGG': 'TGG', 'CGT': 'AGA', 'CGC': 'AGG', 'CGA': 'AGG', 'CGG': 'AGA',
        'AGA': 'CGT', 'AGG': 'CGC', 'GGT': 'GGG', 'GGC': 'GGA', 'GGA': 'GGC',
        'GGG': 'GGT', 'TAA': 'TAG', 'TAG': 'TGA', 'TGA': 'TAA'
    }

    mapped_chars = []
    for i in range(0, len(input_string), 3):
        chunk = input_string[i:i+3]
        mapped_chars.append(mapping.get(chunk, chunk))
    
    mapped_string = "".join(mapped_chars)
    
    fragments = []
    fragment_size = 150
    overlap = 20
    step = fragment_size - overlap
    
    for i in range(0, len(mapped_string), step):
        fragment = mapped_string[i:i+fragment_size]
        fragments.append(fragment)
        if i + fragment_size >= len(mapped_string):
            break
            
    return fragments

if __name__ == "__main__":
    input_data = sys.stdin.read().strip()
    if input_data:
        result = process_string(input_data)
        for frag in result:
            print(frag)