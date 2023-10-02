import sys
import matplotlib.pyplot as plt
from matplotlib_venn import venn3

#Arguments en entrée

vcf_file1 = sys.argv[1]
vcf_file2 = sys.argv[2]
vcf_file3 = sys.argv[3]


#Fonction parse qui permet de  lire les vcf, et calculer la taille des intervalles

def parse_vcf_with_intervals(vcf_file):
    variants = set()
    with open(vcf_file, "r") as file:
        for line in file:
            # Skip header lines
            if line.startswith("#"):
                continue
            fields = line.strip().split("\t")
            chrom = fields[0]
            pos = int(fields[1])
            ref = fields[3]
            alt = fields[4]
            # Calcule des intervalles (1 pour SNP, taille de l'insert ou del pour les indels)
            if len(ref) == 1 and len(alt) == 1:
                # SNP
                start = pos - 1
                end = pos + 1
            else:
                # Indel
                start = pos - len(ref)
                end = pos + len(alt)
            # ajouter tout dans un Set
            variants.add((chrom, start, end))
    return variants

# Parser les vcf
variants1 = parse_vcf_with_intervals(vcf_file1)
variants2 = parse_vcf_with_intervals(vcf_file2)
variants3 = parse_vcf_with_intervals(vcf_file3)

# Comparaison par intervalle
shared_variants = variants1.intersection(variants2, variants3)
unique_variants1 = variants1.difference(variants2, variants3)
unique_variants2 = variants2.difference(variants1, variants3)
unique_variants3 = variants3.difference(variants1, variants2)


#Diagramme de Venn via la librairie matplotlib_venn 

venn_labels = {
    "100": len(unique_variants1),
    "010": len(unique_variants2),
    "001": len(unique_variants3),
    "111": len(shared_variants),
}

venn = venn3(subsets=venn_labels, set_labels=('Sniffles', 'Sniffles2', 'Svim'))
plt.title("Venn Diagram of Variants")

# Output


output_file = "venn_diagram.png"
plt.savefig(output_file)

plt.close()
