#!/usr/bin/python
import argparse
import os
import csv

def parse_arguments():
    str = 'BSig obtains a small set of miRNA biomarkers as a signature and establishes a panel of miRNAs to distinguish breast cancer from healthy individuals. '
    parser = argparse.ArgumentParser(prog='BSig_main.py', description=str)
    parser.add_argument("-i", required=True, help="a set of miRNA gene expression for breast cancer")

    return parser

def main(args=None):
    args = parse_arguments().parse_args(args)
    expression = args.i
    svmpredict = "libsvm/svm-predict"
    svmscale = "libsvm/svm-scale"
    if os.path.exists(svmpredict):
        print("svm-predict exist:" + svmpredict)
    else:
        print("svm-predict doesn't exist, please build it in libsvm folder")
        quit()
    if os.path.exists(svmscale):
        print("svm-scale exist:" + svmscale)
    else:
        print("svm-scale doesn't exist, please build it in libsvm folder")
        quit()
    print('cancer type:' + cancer_type)
    print('expression file:' + expression)
    svm_format = expression + ".svm"
    wfile = open(svm_format, "w")
    wfile.write('0 ')
    f_no = 1
    #efile = open(expression, "r")
    with open(expression, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for row in csvreader:
            miRNA_expression = row[1]
            wfile.write(str(f_no) + ":" + miRNA_expression + " ")
            f_no += 1
    
    wfile.close()
    model = "model/BSig.model"
    scale = "model/BSig.feature.scale"

    if os.path.exists(model):
        print("model exist:" + model)
    else:
        print("model doesn't exist:" + model)
        quit()
    svm_format_scl = svm_format + ".scl"
    svm_prediction_results = svm_format_scl + ".predict"
    cmd = svmscale + " -r " + scale + " " + svm_format + " > " + svm_format_scl
    os.system(cmd)
    cmd = svmpredict + " -b 1 -q " + svm_format_scl + " " + model + " " + svm_prediction_results
    os.system(cmd)
    rfile = open(svm_prediction_results,"r")
    for line in rfile:
        clean_line = line.rstrip('\r\n')
        ele = clean_line.split(' ')
        labels = ele[0]
        if labels == 'labels':
            continue
        prediction_score = ele[1]
    print("prediction score:" + prediction_score)

    

        


if __name__ == "__main__":
    main()
