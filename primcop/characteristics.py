"""
File with amino acid characteristics relevant to prion formation and propagation.
"""

# Single character IUPAC codes for all possible amino acids
AMINO_ACIDS = "ACDEFGHIKLMNPQRSTVWY"

# Names of amino acid residues
IUPAC_NAME = {
    "A": "Alanine",
    "C": "Cysteine",
    "D": "Aspartic acid",
    "E": "Glutamic acid",
    "F": "Phenylalanine",
    "G": "Glycine",
    "H": "Histidine",
    "I": "Isoleucine",
    "K": "Lysine",
    "L": "Leucine",
    "M": "Methionine",
    "N": "Asparagine",
    "P": "Proline",
    "Q": "Glutamine",
    "R": "Arginine",
    "S": "Serine",
    "T": "Threonine",
    "V": "Valine",
    "W": "Tryptophan",
    "Y": "Tyrosine",
}

# Propensity scores
PROPENSITY = {
    "A": -0.396490246,
    "C": 0.415164505,
    "D": -1.276997939,
    "E": -0.605023827,
    "F": 0.838732498,
    "G": -0.039220713,
    "H": -0.278573356,
    "I": 0.813697862,
    "K": -1.576748587,
    "L": -0.040005335,
    "M": 0.673729095,
    "N": 0.080295334,
    "P": -1.197447496,
    "Q": 0.069168387,
    "R": -0.405858577,
    "S": 0.133912418,
    "T": -0.11457038,
    "V": 0.813697862,
    "W": 0.666735081,
    "Y": 0.77865336,
}

# Hydrophobicity scores
HYDROPHOBICITY = {
    "A": 0.7,
    "C": 0.777777778,
    "D": 0.111111111,
    "E": 0.111111111,
    "F": 0.811111111,
    "G": 0.455555556,
    "H": 0.144444444,
    "I": 1,
    "K": 0.066666667,
    "L": 0.922222222,
    "M": 0.711111111,
    "N": 0.111111111,
    "P": 0.322222222,
    "Q": 0.111111111,
    "R": 0,
    "S": 0.411111111,
    "T": 0.422222222,
    "V": 0.966666667,
    "W": 0.4,
    "Y": 0.355555556,
}

# Amino acid charge states
CHARGE = {
    "A": 0,
    "C": 0,
    "D": -1,
    "E": -1,
    "F": 0,
    "G": 0,
    "H": 0,
    "I": 0,
    "K": 1,
    "L": 0,
    "M": 0,
    "N": 0,
    "P": 0,
    "Q": 0,
    "R": 1,
    "S": 0,
    "T": 0,
    "V": 0,
    "W": 0,
    "Y": 0,
}

# Maintenance scores
MAINTENANCE = {
    "A": 0.28,
    "C": 0.45,
    "D": -0.19,
    "E": 0.99,
    "F": 0.33,
    "G": 0.047,
    "H": -0.064,
    "I": -0.57,
    "K": 0,
    "L": -0.48,
    "M": -1.80,
    "N": 0.18,
    "P": 0.065,
    "Q": 0.11,
    "R": -0.88,
    "S": 0.18,
    "T": -0.059,
    "V": -0.35,
    "W": 1.40,
    "Y": 1.03,
}
