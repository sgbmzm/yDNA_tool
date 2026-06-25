from Bio.Seq import Seq

sequence = """
TGAGCCACCGTGCCCGGCCTGGCTGGTTGTTTTTTGTATATCAATTCTGTCAGGCGGACGCGCGTGAAAAATTCCAATGGAAGCTGTGACCACACACACGCCTGCGCAGTACAACTTACATAGCGGACTTCACTCTCTTAAAAGTGAATTGTTTTGCAGGTTTTACGACATGGACAGAGCTGTGCAGCCATCATCACGAGCTAATCCAAAGCAAGGTATTCGACTTAAAATTCAAATGCCATGAAACCTATCCTTTCAATGTTTACGGTACAGACGATTTTAGTACTTTCCCAAACCTATGAAATTGGCCCCAATCCTGAACAAGGAATGATTTGTCTCTGAAACAAATCATGATTTTGCAATCACAGCATGTCACAGTCACAAGGAATCATATAGGTTATTTCTCACGATTGGCATTTTTTTTTAAGGCTCCTAAATCGTGCTGTTTCAGGACTTTTGCTAAATATTTTGAAGGTCGGCGAAAGATAAGTTTAAGAGT
""".replace("\n", "").replace(" ", "").upper()

target_snp_location = 299

reference_allele = sequence[target_snp_location]
derived_allele = "?"

forward_inner_region = sequence[target_snp_location-27:target_snp_location]
forward_inner = forward_inner_region+derived_allele

reverse_inner_region = sequence[target_snp_location:target_snp_location+27]
reverse_inner = str(Seq(reverse_inner_region).reverse_complement())

# פריימר חיצוני קדמי
forward_outer = sequence[0:27]

# פריימר חיצוני רוורס
reverse_region = sequence[-27:]
reverse_outer = str(Seq(reverse_region).reverse_complement())

print("Forward Outer Primer")
print("מיקום:", 0, "-", 26)
print(forward_outer)

print()

print("Reverse Outer Primer")
print("מיקום ברצף המקורי:", len(sequence)-27, "-", len(sequence)-1)
print(reverse_outer)

print()

print("Forward Inner Primer")
#print("מיקום:", 0, "-", 26)
print(forward_inner)

print()

print("Reverse Inner Primer")
print("מיקום ברצף המקורי:", len(sequence)-27, "-", len(sequence)-1)
print(reverse_inner)