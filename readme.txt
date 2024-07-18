hbond_parser : parse hbond output from VMD into a csv file
the structure of the output is donor/acceptor,occupancy
the average of repeats is taken, if a value is missing in a repeat, it's considered to be zero for the average

combine_results : combine hbond results for each individual ligand
all results are combined. First, the results for each ligand are combined individually, i.e. only receptor amino-acids are considered for the donor/acceptor parts, and they are labelled accordingly. Then, as there could be repeats in the aminoacids, they are combined, using either the 'largest' or 'sum' methods. Then, all the results for all ligands are combined into a single csv file.
