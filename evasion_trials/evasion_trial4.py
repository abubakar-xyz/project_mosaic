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

def transform_sequence(seq):
    result = []
    for i in range(0, len(seq), 3):
        codon = seq[i:i+3]
        if len(codon) == 3:
            result.append(mapping.get(codon, codon))
        else:
            result.append(codon)
    return ''.join(result)

def chunk_with_overlap(seq, chunk_size=150, overlap=20):
    chunks = []
    step = chunk_size - overlap
    for i in range(0, len(seq), step):
        chunk = seq[i:i + chunk_size]
        if chunk:
            chunks.append(chunk)
        if i + chunk_size >= len(seq):
            break
    return chunks

if __name__ == "__main__":
    input_string = input().strip()
    transformed = transform_sequence(input_string)
    chunks = chunk_with_overlap(transformed)

    for chunk in chunks:
        print(chunk)