import argparse
import os

parser = argparse.ArgumentParser(description='Run parse hbond results')

# Required arguments
parser.add_argument('-i','--input', help='Ligand name', required=True)

args = parser.parse_args()

dir = os.path.dirname(os.path.realpath(__file__))

os.system(f'python {dir}/hbond_parser.py -i {args.input}_R*_hbonds.dat -o {args.input}_hbonds_average.csv')