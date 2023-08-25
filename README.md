# BSig
Central to BSig's functionality is the integration of miRNA expression profile data from both breast cancer (BC) patients and healthy individuals. Using this feature, users can use miRNA expression profiles from unidentified samples. BSig then provides a prediction score for each input miRNA profile, ranging from 0 to 1. Higher scores suggest a greater likelihood of pathogenicity, while lower scores are indicative of a healthy status. This interactive capability underscores the practical utility of BSig in real-world diagnostic scenarios.

## Input Data
miRNA expression with CSV format. User can put their in-house miRNA expression into a CSV file. 
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

## Example of running BSig

```shell
python BSig_main.py -i input/BSig_example_input.csv
svm-predict exist:libsvm/svm-predict
svm-scale exist:libsvm/svm-scale
expression file:input/BSig_example_input.csv
model exist:model/BSig.model
prediction score:0.99666
```

## Prediction Result
Normalized probabilities between 0 to 1, with higher scores more likely to be Pathogenic and lower scores more likely to be healthy.

## Contact
- Srinivasulu Yerukala Sathipati: sathipathi.srinivasulu@marshfieldclinic.org
- Ming-Ju Tsai: mingjutsai@hsl.harvard.edu
