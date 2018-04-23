def to_rna(dna):
    return dna.translate(str.maketrans('GCTA','CGAU'))
print(to_rna('GCTA hahaha'))
print(to_rna('hihi CGG'))