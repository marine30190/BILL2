from statistics import mean
# Input and output files' paths
input_vcf_file = "/home/e20180009483/Documents/S3/BILL/merged_vcf.vcf"
output_file = "simplified_merged_sv.txt"

# Function to extract information from the INFO field and cut it into small parts
def extract_sv_info(info_field):
    sv_info = {}
    info_items = info_field.split(";")
    for item in info_items:
        parts = item.split("=")
        if len(parts) == 2:
            key, value = parts
            if key in ["SVTYPE", "SVLEN", "SUPPORT","COVERAGE", "AF"]:
                sv_info[key] = value
    return sv_info

# Read the lines of the input VCF file and write the output file
with open(input_vcf_file, "r") as vcf_file, open(output_file, "w") as simplified_file:
    simplified_file.write("CHROM\tPOS\tSV_type\tTaille\tLectures_totaux\tSLectures_supportes\tFréquence_allélique\n")
    
    for line in vcf_file:
        # Skip lines starting with "#"
        if line.startswith("#"):
            continue
        
        fields = line.strip().split("\t")
        chrom = fields[0]
        pos = fields[1]
        info = fields[7]
        format = fields[11]

        sv_info = extract_sv_info(info)
        if sv_info.get("AF","NA") == "NA":
            continue
        
        sv_type = sv_info.get("SVTYPE", "NA")
        sv_len = sv_info.get("SVLEN", "NA")
        
        tot_cal = format.split(":")
        last_num = tot_cal[-1]
        if (last_num  == "."):
            total_read_count = 0
        else :
            second_last_num = tot_cal[-2]
            last_num = int(last_num)
            second_last_num = int(second_last_num)
            tot = (last_num + second_last_num)
            total_read_count = tot
        supporting_read_count = sv_info.get("SUPPORT", "NA")
        
        allele_frequency = sv_info.get("AF", "NA")
        
        simplified_file.write(f"{chrom}\t{pos}\t{sv_type}\t{sv_len}\t{total_read_count}\t{supporting_read_count}\t{allele_frequency}\n")

print("Simplified SV data has been written to", output_file)