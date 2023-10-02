library(vcfR)

setwd <- "/home/e20170003883/Documents/"

tmp_vcf_P50<-readLines("/home/e20170003883/Documents/sniffles_output.vcf")
sniffles_output.vcf<-read.table("/home/e20170003883/Documents/sniffles_output.vcf", stringsAsFactors = FALSE)
sniffles_output.vcf<-(sniffles_output.vcf$V2) 

tmp_vcf_P30<-readLines("/home/e20170003883/Documents/cute_variants.vcf")
cute_variants.vcf<-read.table("/home/e20170003883/Documents/cute_variants.vcf", stringsAsFactors = FALSE)
cute_variants.vcf<-(cute_variants.vcf$V2)

tmp_vcf_P15<-readLines("/home/e20170003883/Documents/variants.vcf")
SVIM_variants.vcf<-read.table("/home/e20170003883/Documents/variants.vcf", stringsAsFactors = FALSE)
SVIM_variants.vcf<-(SVIM_variants.vcf$V2) 

set.seed(20190708)
genes <- paste("gene",1:1000,sep="")
x <- list(
  Sniffles2_cluster = sniffles_output.vcf, 
  cuteSV = cute_variants.vcf, 
  SVIM = SVIM_variants.vcf)

if (!require(devtools)) install.packages("devtools")
devtools::install_github("yanlinlin82/ggvenn")

library(ggvenn)
ggvenn(
  x, 
  fill_color = c("#0073C2FF", "#EFC000FF", "#868686FF", "#CD534CFF"),
  stroke_size = 0.5, set_name_size = 4
)
