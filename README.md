# QClus: Robust and reliable preprocessing method for human heart snRNA-seq

This is a novel nuclei filtering method targeted to human heart samples. We use specific metrics such as splicing, mitochondrial gene expression, nuclear gene expression, and non-cardiomyocyte and cardiomyocyte marker gene expression to cluster nuclei and filter empty and highly contaminated droplets. This approach combined with other filtering steps enables for flexible, automated, and reliable cleaning of samples with varying number of nuclei, quality, and contamination levels. The robustness of this method has been validated on a large number of heterogeneous datasets, in terms of number of nuclei, overall quality, and contamination. 

You can find the original preprint for this method at the link below:

https://www.biorxiv.org/content/10.1101/2022.10.21.513315v1

Any and all comments/criticisms/suggestions are enthusiastically received! :-)

## Required packages

- pandas
- loompy
- scanpy
- scikit-learn
- scrublet



## Installation

In the future we will be adding QClus to PyPI,  making it available via pip install.

Currently we recommend installing QClus from source. To do so, please follow the instructions below:

1. Clone this repository into a suitable location on your machine or server using the following command:

    ```git clone https://github.com/scHEARTGROUP/qclus.git```
    
2. In the root directory of the package, run the following command to install the required packages:

    ```pip install .```


## Quickstart guide

Below is a quickstart workflow for QClus. Please see the tutorials/tutorial.ipynb notebook for a more thorough guide on how to run the QClus algorithm.

QClus requires two files to run: a Cell Ranger generated filtered count matrix and a Velocyto generated loom file. 

Detailed instructions on how to generate the loom file can be found in the [Velocyto documentation](http://velocyto.org/velocyto.py/tutorial/cli.html#running-velocyto-on-10x-data).


```python
#import library
import qclus

#Define the path to an .h5 file of raw counts, as well as 
#the path to a .loom file containing the splicing information for those same counts
counts_path = "filtered_feature_bc_matrix_CB-X36.h5"
loompy_path = "counts_counts_CAD_CB-X36.loom"

#run QClus with default settings
adata = qclus.run_qclus(counts_path,  
                        loompy_path)
```


The code returns an AnnData object with your raw unfiltered counts as well as the following annotations in the adata.obs dataframe for each barcode: 

- fraction_unspliced
    - the fraction of unspliced reads for that barcode
- pct_counts_MT
    - percentage of reads aligning to the mitochondrial genome
- total_counts
    - total UMI counts for that barcode
- n_genes_by_counts
    - number of genes expressed
- qclus
    - results of the QClus algorithm
    - Cells are either tagged as "passed" or by the name of the filtering step that tagged that barcode to be removed

You can now evaluate the results, move forward with downstream analysis or save this object with adata.write().

Note: The "-1" suffix of the barcodes added by Cell Ranger has been removed and adata.var_names_make_unique() has been run to make the variable names unique.

For a more thorough guide please see the tutorials/tutorial.ipynb notebook.
