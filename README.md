# UCSCtable2bed
When getting a bed from UCSC we don't always get what we want. It often have exons with number 0 and includes UTRs. For us only coding exons is of interest. This script takes any of the NCBI RefSeq tables and make it to the bed we want. 

group: Genes and Gene Predictions
  track: NCBI RefSeq
    table: any
    
output format: all fields from selected table


The script is run with:
python ucsc2bed.py <ucsc_table.infile> <extra_bases>

ucsc_table.infile is the name of the table
extra_bases is the number of bases outside of the coding exon you want to include
