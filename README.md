# UCSCtable2bed
When getting a bed from UCSC, we don't always get what we want. It often has exons with the number 0, not to mention numbers in the wrong order when on a negative strand, and includes UTRs. For us, only coding exons is of interest. This script takes any NCBI RefSeq tables and makes it to the bed we want. 

On the UCSC homepage, under Tools, you can find Table Browser (https://genome.ucsc.edu/cgi-bin/hgTables)

> group: Genes and Gene Predictions
> 
> track: NCBI RefSeq
> 
> table: any
>         
> output format: all fields from selected table



The script is run with the following:
```
python ucsc2bed.py <ucsc_table.infile> <extra_bases>
```

ucsc_table.infile is the name of the table
extra_bases is the number of bases outside of the coding exon you want to include
