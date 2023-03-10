# BSig
The breast cancer prediction method BSig identifies circulating miRNA signatures to distinguishe breast cancer from healthy individuals.

## Input Data
miRNA expression with CSV format. User can put their in-house miRNA expression into csv file. 
[BSig_example_input.csv](input/BSig_example_input.csv)

## Getting start
```shell
git clone https://github.com/mingjutsai/BSig.git
cd BSig
```

build LIBSVM
```shell
cd libsvm
make
```

## Options of BSig
```shell
python BSig_main.py -h

BSig obtains a small set of miRNA biomarkers as a signature and establishes a panel of miRNAs to distinguish breast cancer
from healthy individuals.

optional arguments:
  -h, --help  show this help message and exit
  -i I        a set of miRNA gene expression for breast cancer
```

## Example of running CancerSig

```shell
python BSig_main.py -i input/BSig_example_input.csv
```

## Prediction Result
Normalized probabilities between 0 to 1, with higher scores more likely to be Pathogenic  and lower scores more likely     to be benign.

## Contact
- Srinivasulu Yerukala Sathipati: sathipathi.srinivasulu@marshfieldclinic.org
- Ming-Ju Tsai: mingjutsai@hsl.harvard.edu
